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
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(first_name="newfname",
                                                   last_name="newlname",
                                                   address="newhome",
                                                   mobile="8888888888",
                                                   email="newname@newhome.local"))
    app.session.logout()


def test_modification_first_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(first_name="New first name"))
    app.session.logout()


def test_modification_first_contact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(last_name="New last name"))
    app.session.logout()


def test_modification_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(address="New address"))
    app.session.logout()


def test_modification_first_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(mobile="7777777777"))
    app.session.logout()


def test_modification_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification_first_contact(Contact(email="name@newemail.local"))
    app.session.logout()
