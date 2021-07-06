#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_mod_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from model.group import Group
from random import randrange


def test_modification_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="111", header="222", footer="333")
    group.id = old_groups[index].id
    app.group.modification_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modification_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modification_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modification_some_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="New header")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modification_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modification_some_group_footer(app, db, check_ui):
    app.group.create_group_if_missing()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(footer="New footer")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modification_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
