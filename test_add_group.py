# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd
        self.Открытие_главной_страницы(wd)
        self.Введение_Логина_Пароля(wd)
        self.Открываем_страницу_со_списоком_Групп(wd)
        self.Создаем_и_Заполняем_форму_Группа(wd)
        self.Возвращаемся_на_страницу_со_списком_Групп(wd)
        self.Выходим_из_программы(wd)

    def Выходим_из_программы(self, wd: object) -> object:
        wd.find_element_by_link_text("Logout").click()

    def Возвращаемся_на_страницу_со_списком_Групп(self, wd):
        wd.find_element_by_link_text("group page").click()

    def Создаем_и_Заполняем_форму_Группа(self, wd):
        # Нажимаем_на_создание_Группы
        wd.find_element_by_name("new").click()
        #Заполняем_форму_Группа
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test")
        # Нажимаем_Создать_Группу
        wd.find_element_by_name("submit").click()

    def Открываем_страницу_со_списоком_Групп(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Введение_Логина_Пароля(self, wd: object) -> object:
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def Открытие_главной_страницы(self, wd: object) -> object:
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
