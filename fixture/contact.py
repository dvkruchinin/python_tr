#!/usr/bin/env python
# coding:utf-8
"""
Name    : contact.py
Author  : Dmitry Kruchinin
Date    : 6/21/2021
Desc:   
"""


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_forms(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_forms(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def modification_first_contact(self, contact_new_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_forms(contact_new_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_contact_page(self):
        wd = self.app.wd
        # End with "/addressbook" and button "Send e-Mail" are presents
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//*[@id='content']/form["
                                                                                          "2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))
