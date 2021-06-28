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


def test_modification_some_contact(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="newfname",
                       lastname="newlname",
                       address="newhome",
                       mobilephone="8888888888",
                       email="newname@newhome.local"))
    contact.id = old_contacts[index].id
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_some_contact_first_name(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New first name")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_some_contact_last_name(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="New last name")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_some_contact_address(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address="New address")
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()


def test_modification_some_contact_phone(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(mobilephone="7777777777")
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()


def test_modification_some_contact_email(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(email="name@newemail.local")
    app.contact.modification_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
