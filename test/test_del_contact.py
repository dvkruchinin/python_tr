#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from random import randrange


def test_delete_some_contact(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
