#!/usr/bin/env python
# coding:utf-8
"""
Name    : check_db_connection.py
Author  : Dmitry Kruchinin
Date    : 7/1/2021
Desc:   
"""

from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")

try:
    groups = db.get_groups_list()
    contacts = db.get_contacts_list()
    contacts_in_group = db.get_contacts_in_group(Group(id="248"))
    contacts_not_in_group = db.get_contacts_not_in_group(Group(id="248"))
    print("####### Groups")
    for group in groups:
        print(group)
    print(len(groups))
    print("####### Contacts")
    for contact in contacts:
        print(contact)
    print(len(contacts))
    print("####### Contacts in group")
    for contact_in_group in contacts_in_group:
        print(contact_in_group)
    print(len(contacts_in_group))
    print("####### Contacts NOT in group")
    for contact_not_in_group in contacts_not_in_group:
        print(contact_not_in_group)
    print(len(contacts_not_in_group))
finally:
    pass # db.destroy()
