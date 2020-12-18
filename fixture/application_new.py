from selenium import webdriver
from fixture.session_new import SessionHelperNew
from fixture.add_new import ContactHelper


class ApplicationNew:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_new = SessionHelperNew(self)
        self.add_new = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")




    def destroy(self):
        self.wd.quit()







