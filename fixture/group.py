#!/usr/bin/env python
# coding:utf-8
"""
Name    : group.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_forms(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_forms(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modification_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # Select first group
        wd.find_element_by_name("selected[]").click()
        # Submit modification
        wd.find_element_by_name("edit").click()
        self.fill_forms(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


