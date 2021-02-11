# -*- coding: utf-8 -*-
from pythoncourse2020.model.group import Group

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    #group = Group(name="edwded", header="dcsdw", footer="edwedw")
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count_group()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)