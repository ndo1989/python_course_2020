# -*- coding: utf-8 -*-
from pythoncourse2020.model.contact import Contact
from pythoncourse2020.fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="test_name", midle_name="test_midle_name", last_name="test_last_name", nikname="test_nikname"))
    app.logout()
