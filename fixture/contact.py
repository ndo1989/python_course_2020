
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.midle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nikname)

    def change_field_value(self, fild_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_firstname).click()
            wd.find_element_by_name(fild_firstname).clear()
            wd.find_element_by_name(fild_firstname).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # init contact deletion
        self.choice_first_contact()
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def choice_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # init edit contact
        self.choice_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()