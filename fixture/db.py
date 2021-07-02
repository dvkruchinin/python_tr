#!/usr/bin/env python
# coding:utf-8
"""
Name    : db.py
Author  : Dmitry Kruchinin
Date    : 7/1/2021
Desc:   
"""

import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, "
                           "email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname,
                                    lastname=lastname,
                                    address=address,
                                    homephone=home,
                                    workphone=work,
                                    mobilephone=mobile,
                                    secondaryphone=phone2,
                                    email=email,
                                    email2=email2,
                                    email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
