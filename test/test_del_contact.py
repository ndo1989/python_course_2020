# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact


def test_delete_first_contact(app):
    app.contact.delete_first_contact()