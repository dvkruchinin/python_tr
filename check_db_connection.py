#!/usr/bin/env python
# coding:utf-8
"""
Name    : check_db_connection.py
Author  : Dmitry Kruchinin
Date    : 7/1/2021
Desc:   
"""

import pymysql

connection = pymysql.connect(host="localhost", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
