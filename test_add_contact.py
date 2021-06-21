# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(first_name="fname",
                                        last_name="lname",
                                        address="home",
                                        phone="9999999999",
                                        email="name@home.local"))
        self.app.return_to_home_page()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
