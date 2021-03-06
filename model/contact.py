#!/usr/bin/env python
# coding:utf-8
"""
Name    : contact.py
Author  : Dmitry Kruchinin
Date    : 6/18/2021
Desc:   
"""

from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, homephone=None,
                 workphone=None, mobilephone=None, secondaryphone=None, email=None, email2=None, email3=None, id=None,
                 all_phones_from_home_page=None, fullname=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.fullname = fullname
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s-%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
