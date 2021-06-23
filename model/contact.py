#!/usr/bin/env python
# coding:utf-8
"""
Name    : contact.py
Author  : Dmitry Kruchinin
Date    : 6/18/2021
Desc:   
"""

class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, mobile=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile = mobile
        self.email = email
