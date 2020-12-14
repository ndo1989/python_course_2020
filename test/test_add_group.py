# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group
from pythoncourse2020.fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="edwded", header="dcsdw", footer="edwedw"))
    app.logout()

