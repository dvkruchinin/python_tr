# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="fname",
                               last_name="lname",
                               address="home",
                               phone="9999999999",
                               email="name@home.local"))
    app.return_to_home_page()
    app.session.logout()
