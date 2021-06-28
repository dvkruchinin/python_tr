# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", lastname="lastname",
                                homephone="homephone111", mobilephone="mobilephone222",
                                workphone="workphone333", secondaryphone="secphone444", address="home",
                                email="name@home.local", email2="name2@home.local", email3="name3@home.local")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
