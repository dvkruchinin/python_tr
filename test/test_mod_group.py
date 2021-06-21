#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_mod_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.group import Group


def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first_group(Group(name="111", header="222", footer="333"))
    app.session.logout()
