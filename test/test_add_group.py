# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group

def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    #group = Group(name="edwded", header="dcsdw", footer="edwedw")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)