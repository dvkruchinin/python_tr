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


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
