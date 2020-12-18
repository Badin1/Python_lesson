# -*- coding: utf-8 -*-
import pytest
from model.add_new import Add_New
from fixture.application_new import ApplicationNew

@pytest.fixture
def appn(request):
    fixture = ApplicationNew()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new(appn):
    appn.session_new.login(username="admin", password="secret")
    appn.add_new.create(Add_New(firstname="Petrov", lastname="Petr", address="Moscow", telephone="8-905-323-50-26", email="petrov@yandex.ru"))
    appn.session_new.logout()

