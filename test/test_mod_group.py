#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_mod_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.group import Group


def check_group_count(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_modification_first_group(app):
    check_group_count(app)
    app.group.modification_first_group(Group(name="111", header="222", footer="333"))


def test_modification_first_group_name(app):
    check_group_count(app)
    app.group.modification_first_group(Group(name="New group"))


def test_modification_first_group_header(app):
    check_group_count(app)
    app.group.modification_first_group(Group(header="New header"))


def test_modification_first_group_footer(app):
    check_group_count(app)
    app.group.modification_first_group(Group(footer="New footer"))
