from pythoncourse2020.model.contact import Contact

def test_modify_first_contact_update_last_name(app):
    app.contact.modify_first_contact(Contact(last_name="test_last_name20000"))