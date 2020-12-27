from selenium import webdriver
from pythoncourse2020.fixture.session import SessionHelper
from pythoncourse2020.fixture.group import GroupHelper
from pythoncourse2020.fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()

