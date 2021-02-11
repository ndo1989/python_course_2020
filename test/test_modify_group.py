from pythoncourse2020.model.group import Group
import random
from random import randrange

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="edwded100", header="dcsdw100", footer="edwedw100"))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    group = Group(name="New group")
    #group.id = groupp.id
    app.group.modify_group_by_id(edit_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    edit_group.name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


