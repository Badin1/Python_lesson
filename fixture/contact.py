
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_new(self, new):
        wd = self.app.wd
        self.open_new_page()
        # fill new firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new.telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new.email)
        # submit new creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    # def test_delete_first_new(self):
    #     wd = self.app.wd
    #     # Выбрать первый контакт
    #     wd.find_element_by_name("selected[]").click()
    #     # Удалить контакт
    #     wd.find_element_by_value("Delete").click()
    #     self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
