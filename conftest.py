#!/usr/bin/env python
# coding:utf-8
"""
Name    : conftest.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""

import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
