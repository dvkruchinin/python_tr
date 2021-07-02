#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

import random
from model.contact import Contact


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(firstname="firstname", lastname="lastname",
                                homephone="homephone111", mobilephone="mobilephone222",
                                workphone="workphone333", secondaryphone="secphone444", address="home",
                                email="name@home.local", email2="name2@home.local", email3="name3@home.local"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
