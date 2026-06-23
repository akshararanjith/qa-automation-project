# from selenium import webdriver
from selenium.webdriver.common.by import By

def test_invalid_login(driver):

    # driver=webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID,"username").send_keys("wronguser")
    driver.find_element(By.ID,"password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()   

    assert "Your username is invalid!" in driver.page_source

    driver.quit()
