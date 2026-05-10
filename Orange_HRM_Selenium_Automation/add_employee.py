from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class searching_employee:
    def search(self):

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        waits = WebDriverWait(driver,20)
        username = waits.until(EC.visibility_of_element_located((By.NAME,"username")))
        username.send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        expected_page = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        waits.until(EC.url_to_be(expected_page))
        if expected_page == driver.current_url:
            add_button = waits.until(EC.presence_of_element_located((By.XPATH,"//span[text()='PIM']")))
            add_button.click()
            current_url = ("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
            waits.until(EC.url_to_be(current_url))
            if current_url == driver.current_url:
                add_button = waits.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Add']")))
                add_button.click()
                firstname = waits.until(EC.visibility_of_element_located((By.NAME,"firstName")))
                firstname.send_keys("Cherith")
                lastname = waits.until(EC.visibility_of_element_located((By.NAME,"lastName")))
                lastname.send_keys("L")
                emp_id = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")))
                emp_id.click()
                waits.until(EC.visibility_of_element_located((By.XPATH,"//input[@class='oxd-input oxd-input--focus']")))
                emp_id.clear()
                emp_id.send_keys("700969")
                create_login = waits.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")))
                create_login.click()
                user_name = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")))
                user_name.send_keys("Cherith21")
                pass_word = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[1]")))
                pass_word.click()
                pass_word.send_keys("Cherith007")
                confirm_password = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[2]")))
                confirm_password.send_keys("Cherith007")
                submit_button = waits.until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
                submit_button.click()
                time.sleep(10)

obj = searching_employee()
obj.search()