# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="edwded", header="dcsdw", footer="edwedw"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

