#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_add_remove_contact_to_from_group.py
Author  : Dmitry Kruchinin
Date    : 7/2/2021
Desc:   
"""

import random
from model.group import Group
from model.contact import Contact


def test_add_remove_contact_to_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(firstname="firstname", lastname="lastname",
                                 homephone="homephone111", mobilephone="mobilephone222",
                                 workphone="workphone333", secondaryphone="secphone444", address="home",
                                 email="name@home.local", email2="name2@home.local", email3="name3@home.local"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    wd = app.wd
    app.contact.open_contact_page()
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    count_contact_in_group = len(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.select_contact_by_id(contact.id)
    to_group = wd.find_element_by_name("to_group")
    to_group.find_element_by_css_selector("option[value='%s']" % group.id).click()
    wd.find_element_by_name("add").click()
    wd.find_element_by_css_selector("a[href='./?group=%s']" % group.id).click()
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group + 1
    app.contact.select_contact_by_id(contact.id)
    wd.find_element_by_css_selector("input[value='Remove from \"%s\"']" % group.name).click()
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group
