from pages.login_page import Loginpage

def test_login():
    login = Loginpage()
    login.enter_username("Admin123")
    login.enter_password("password")
    login.click_login()

test_login()