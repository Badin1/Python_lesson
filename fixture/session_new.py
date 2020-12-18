
class SessionHelperNew:
    def __init__(self, appn):
        self.appn = appn

    def login(self, username, password):
        wd = self.appn.wd
        self.appn.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.appn.wd
        wd.find_element_by_link_text("Logout").click()