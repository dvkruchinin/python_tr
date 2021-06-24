#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_del_group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
