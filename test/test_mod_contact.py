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
                                                   phone="8888888888",
                                                   email="newname@newhome.local"))
    app.session.logout()
