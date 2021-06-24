#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

from random import randrange


def test_delete_some_group(app):
    app.group.create_group_if_missing()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
