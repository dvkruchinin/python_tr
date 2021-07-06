#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_mod_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.contact import Contact
from random import randrange

create_contact_if_missing = Contact(firstname="firstname", lastname="lastname",
                                homephone="homephone111", mobilephone="mobilephone222",
                                workphone="workphone333", secondaryphone="secphone444", address="home",
                                email="name@home.local", email2="name2@home.local", email3="name3@home.local")


def test_modification_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="newfname",
                       lastname="newlname",
                       address="newhome",
                       mobilephone="8888888888",
                       email="newname@newhome.local"))
    contact.id = old_contacts[index].id
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modification_some_contact_first_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New first name")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modification_some_contact_last_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="New last name")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modification_some_contact_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address="New address")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modification_some_contact_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(mobilephone="7777777777")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modification_some_contact_email(app, db, check_ui):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(email="name@newemail.local")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modification_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
