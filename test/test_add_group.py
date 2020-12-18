# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="edwded", header="dcsdw", footer="edwedw"))
    app.session.logout()

