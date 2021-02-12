from pythoncourse2020.model.contact import Contact



def test_comparator_contact_on_home_page_and_db(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(first_name="test_name1", midle_name="test_midle_name1", last_name="test_last_name1",
                                   nikname="test_nikname1"))
    contacts_home_page = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    list_contacts_from_home_page = list(
        map(lambda y: (y.id, y.firstname, y.lastname), contacts_home_page))
    list_contacts_from_db = list(
        map(lambda y: (y.id, y.firstname, y.lastname), contacts_db))
    assert sorted(list_contacts_from_home_page) == sorted(list_contacts_from_db)
