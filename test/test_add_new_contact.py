# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="test_name", midle_name="test_midle_name", last_name="test_last_name", nikname="test_nikname"))
    app.session.logout()
