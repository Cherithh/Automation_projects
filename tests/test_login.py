from pages.login_page import Loginpage
from Utils.data_reader import get_test_data

def test_login():
    data = get_test_data()
    login = Loginpage()
    
    username = data["Valid_user"]["username"]
    password = data["valid user"]["password"]
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

test_login()