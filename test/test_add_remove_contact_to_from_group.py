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

create_contact_if_missing = Contact(firstname="firstname", lastname="lastname",
                                homephone="homephone111", mobilephone="mobilephone222",
                                workphone="workphone333", secondaryphone="secphone444", address="home",
                                email="name@home.local", email2="name2@home.local", email3="name3@home.local")

create_group_if_missing = Group(name="test")


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(create_group_if_missing)

    if len(db.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(Group(id=[_id for _id in db.get_group_list()][0].id))) == 0:
        app.contact.create(create_contact_if_missing)

    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.create(create_contact_if_missing)
        contacts = orm.get_contacts_not_in_group(Group(id=group.id))

    contact = random.choice(contacts)

    count_contact_in_group = len(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_contact_to_group(contact.id, group.id)
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group + 1


def test_remove_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(create_group_if_missing)

    if len(db.get_contact_list()) == 0:
        app.contact.create(create_contact_if_missing)

    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)

    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:
        app.contact.add_contact_to_group(contact.id, group.id)

    count_contact_in_group = len(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.remove_contact_from_group(group.id)
    assert len(orm.get_contacts_in_group(Group(id=group.id))) == count_contact_in_group - 1

