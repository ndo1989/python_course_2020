from pythoncourse2020.model.group import Group


def test_delete_first_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="edwded100", header="dcsdw100", footer="edwedw100"))
    app.group.delete_first_group()