#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.contact import Contact


def check_contact_count(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test name"))


def test_delete_first_contact(app):
    check_contact_count(app)
    app.contact.delete_first_contact()
