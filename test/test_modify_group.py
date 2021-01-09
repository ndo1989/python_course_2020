from pythoncourse2020.model.group import Group

def test_modify_group_name(app):
    if app.group.count_group() ==0:
        app.group.create(Group(name="edwded100", header="dcsdw100", footer="edwedw100"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


# def test_modify_group_header(app):
    #   if app.group.count_group() ==0:
    #   app.group.create(Group(name="edwded100", header="dcsdw100", footer="edwedw100"))
    #app.group.modify_first_group(Group(header="New header"))