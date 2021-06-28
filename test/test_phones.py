#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_phones.py
Author  : Dmitry Kruchinin
Date    : 6/28/2021
Desc:   
"""


def test_phones_on_home_page(app):
    app.contact.create_contact_if_missing()
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.secondaryphone == contact_from_edit_page.secondaryphone
