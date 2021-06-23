# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="fname",
                       last_name="lname",
                       address="home",
                       mobile="9999999999",
                       email="name@home.local"))
    app.session.logout()
