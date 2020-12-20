from pythoncourse2020.model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1", nikname="test_nikname1"))
    app.session.logout()