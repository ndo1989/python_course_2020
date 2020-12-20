from pythoncourse2020.model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edwded1", header="dcsdw1", footer="edwedw1"))
    app.session.logout()