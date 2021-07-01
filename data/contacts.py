#!/usr/bin/env python
# coding:utf-8
"""
Name    : contacts.py
Author  : Dmitry Kruchinin
Date    : 7/1/2021
Desc:   
"""

from model.contact import Contact

testdata = [
    Contact(firstname="firstname1", lastname="lastname1",
            homephone="homephone1", mobilephone="mobilephone1",
            workphone="workphone1", secondaryphone="secphone1", address="home1",
            email="name1@email.local", email2="name1@emai2.local", email3="name1@email3.local"),
    Contact(firstname="firstname2", lastname="lastname2",
            homephone="homephone2", mobilephone="mobilephone2",
            workphone="workphone2", secondaryphone="secphone2", address="home2",
            email="name2@email.local", email2="name2@emai2.local", email3="name2@email3.local"),

]