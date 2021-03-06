class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Нажимаем_на_создание_Группы
        wd.find_element_by_name("new").click()
        # Заполняем_форму_Группа
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Нажимаем_Создать_Группу
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def test_edit(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Отмечаем группу для изменения
        wd.find_element_by_name("selected[]").click()
        # Нажимаем "Изменить"
        wd.find_element_by_name("edit").click()
        # Изменяем данные
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Сохраняем изменения
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        wd.find_element_by_name("selected[]").click()
        # Submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()



