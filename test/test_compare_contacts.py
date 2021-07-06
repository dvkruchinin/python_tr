#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_compare_contacts.py
Author  : Dmitry Kruchinin
Date    : 6/28/2021
Desc:   
"""

import re
from random import randrange
from model.contact import Contact

create_contact_if_missing = Contact(firstname="firstname", lastname="lastname",
                                    homephone="homephone111", mobilephone="mobilephone222",
                                    workphone="workphone333", secondaryphone="secphone444", address="home",
                                    email="name@home.local", email2="name2@home.local", email3="name3@home.local")


def test_compare_contact_data_home_page_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(create_contact_if_missing))
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    for contact_from_home_page in contacts_from_home_page:
        for contact_from_db in contacts_from_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.firstname == contact_from_db.firstname
                assert contact_from_home_page.lastname == contact_from_db.lastname
                assert contact_from_home_page.address == contact_from_db.address
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


def test_compare_contact_data_view_edit_page(app):
    app.contact.create_contact_if_missing()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.fullname == "%s %s" % (contact_from_edit_page.firstname,
                                                         contact_from_edit_page.lastname)
    assert contact_from_view_page.address == contact_from_edit_page.address
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone,
                                                                                     contact.mobilephone,
                                                                                     contact.workphone,
                                                                                     contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email,
                                                             contact.email2,
                                                             contact.email3])))
