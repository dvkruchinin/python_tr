#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_mod_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.contact import Contact


def test_modification_first_contact(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(first_name="newfname",
                       last_name="newlname",
                       address="newhome",
                       mobile="8888888888",
                       email="newname@newhome.local"))
    contact.id = old_contacts[0].id
    app.contact.modification_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_first_contact_first_name(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="New first name")
    contact.id = old_contacts[0].id
    app.contact.modification_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_first_contact_last_name(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="New last name")
    contact.id = old_contacts[0].id
    app.contact.modification_first_contact(Contact(last_name="New last name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modification_first_contact_address(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    app.contact.modification_first_contact(Contact(address="New address"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modification_first_contact_phone(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    app.contact.modification_first_contact(Contact(mobile="7777777777"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modification_first_contact_email(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    app.contact.modification_first_contact(Contact(email="name@newemail.local"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
