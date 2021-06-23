#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.group import Group


def check_group_count(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_delete_first_group(app):
    check_group_count(app)
    app.group.delete_first_group()
