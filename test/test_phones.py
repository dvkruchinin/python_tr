#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_phones.py
Author  : Dmitry Kruchinin
Date    : 6/28/2021
Desc:   
"""

import re


def test_phones_on_home_page(app):
    app.contact.create_contact_if_missing()
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)


def test_hones_on_contact_view_page(app):
    app.contact.create_contact_if_missing()
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)

