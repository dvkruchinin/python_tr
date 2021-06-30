# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
