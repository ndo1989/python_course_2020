# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="edwded", header="dcsdw", footer="edwedw"))

