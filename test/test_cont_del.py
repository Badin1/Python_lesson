def test_delete_first_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_delete_first_new()
    app.session.logout()