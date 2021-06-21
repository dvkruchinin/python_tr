#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
