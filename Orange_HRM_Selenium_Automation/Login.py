from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login:
    def loginpage(self):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        waits = WebDriverWait(driver,10)
        username = waits.until(EC.visibility_of_element_located((By.NAME,"username")))
        username.send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        expected_page = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        waits.until(EC.url_to_be(expected_page))
        if expected_page == driver.current_url:
            print("Login Successful")
        else:
            print("Login Unsuccessful")


obj = login()
obj.loginpage()