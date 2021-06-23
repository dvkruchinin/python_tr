#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""


def test_delete_first_contact(app):
    app.contact.delete_first_contact()
