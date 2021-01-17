from pythoncourse2020.model.contact import Contact

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
        self.сontact_cache = None

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

    def choice_contact_by_index(self, index):
        wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.choice_contact_by_index(index)
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.сontact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        # init contact deletion
        self.choice_first_contact()
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.сontact_cache = None


    def choice_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def choice_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_contact_by_index(self, index, contact_new):
        wd = self.app.wd
        # init edit contact
        self.choice_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_element_by_name("update")
        self.fill_contact_form(contact_new)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.сontact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # init edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("update")
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.сontact_cache = None

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("add")) > 0:
            wd.find_element_by_link_text("home").click()

    сontact_cache = None

    def get_contact_list(self):
        if self.сontact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.сontact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text_of_cells = element.find_elements_by_tag_name("td")
                last_name = text_of_cells[1].text
                first_name = text_of_cells[2].text
                self.сontact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.сontact_cache)
