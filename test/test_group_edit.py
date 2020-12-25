# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.test_edit(Group(name="edit_test", header="edit_test", footer="edit_test"))
    app.session.logout()


