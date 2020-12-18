# -*- coding: utf-8 -*-
import pytest
from add_new import Add_New
from application_new import ApplicationNew

@pytest.fixture
def appn(request):
    fixture = ApplicationNew()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new(appn):
    appn.login(username="admin", password="secret")
    appn.create_new(Add_New(firstname="Petrov",lastname="Petr", address="Moscow", telephone="8-905-323-50-26", email="petrov@yandex.ru"))
    appn.logout()

