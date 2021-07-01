#!/usr/bin/env python
# coding:utf-8
"""
Name    : contact.py
Author  : Dmitry Kruchinin
Date    : 7/1/2021
Desc:   
"""

import jsonpickle
import random
import string
import os.path
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    digits = string.digits
    return "".join([random.choice(digits) for i in range(10)])


def random_email():
    symbols = string.ascii_letters + string.digits
    user_name = mail_server = "".join([random.choice(symbols) for i in range(10)])
    return "%s@%s" % (user_name, mail_server)


testdata = [
    Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5),
                homephone=random_phone(), mobilephone=random_phone(),
                workphone=random_phone(), secondaryphone=random_phone(), address=random_string("address", 5),
                email=random_email(), email2=random_email(), email3=random_email())
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
