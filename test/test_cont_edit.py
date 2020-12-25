# -*- coding: utf-8 -*-
from model.add_new import Add_New


def test_add_edit(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_edit_add(Add_New(firstname="Ivaniv", lastname="Ivan", address="Moscow", telephone="8-905-323-50-32", email="ivanov@yandex.ru"))
    app.session.logout()