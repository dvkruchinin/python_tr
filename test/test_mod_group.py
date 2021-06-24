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
    app.group.create_group_if_missing()
    old_groups = app.group.get_group_list()
    group = Group(name="111", header="222", footer="333")
    group.id = old_groups[0].id
    app.group.modification_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modification_first_group_name(app):
    app.group.create_group_if_missing()
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modification_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modification_first_group_header(app):
    app.group.create_group_if_missing()
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.modification_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modification_first_group_footer(app):
    app.group.create_group_if_missing()
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.modification_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
