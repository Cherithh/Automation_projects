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
             employee_name = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[contains(@placeholder,'Type for hints')])[1]")))
             employee_name.send_keys("Cherith")

             driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("700969")

             employee_status = waits.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[1]")))
             employee_status.click()
             waits.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='listbox']")))
             employee_status.send_keys(Keys.ARROW_DOWN)
             employee_status.send_keys(Keys.ARROW_DOWN)
             employee_status.send_keys(Keys.ENTER)

             include = waits.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[2]")))
             include.click()
             waits.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='listbox']")))
             include.send_keys(Keys.ARROW_DOWN)
             include.send_keys(Keys.ENTER)

             supervisor_name = waits.until(EC.visibility_of_element_located((By.XPATH,"(//input[contains(@placeholder,'Type for hints')])[2]")))
             supervisor_name.send_keys("IronMan")

             job_title = waits.until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[3]")))
             job_title.click()
             waits.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='listbox']")))
             job_title.send_keys(Keys.ARROW_DOWN)
             job_title.send_keys(Keys.ARROW_DOWN)
             job_title.send_keys(Keys.ARROW_DOWN)
             job_title.send_keys(Keys.ENTER)

             sub_unit = waits.until(EC.visibility_of_element_located((By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[4]")))
             sub_unit.click()
             waits.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='listbox']")))
             sub_unit.send_keys(Keys.ARROW_DOWN)
             sub_unit.send_keys(Keys.ENTER)

             driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
            #  time.sleep(10)


obj1 = searching_employee()
obj1.search()