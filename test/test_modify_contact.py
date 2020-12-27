from pythoncourse2020.model.contact import Contact

def test_modify_first_contact_update_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1", nikname="test_nikname1"))
    app.contact.modify_first_contact(Contact(last_name="test_last_name20000"))