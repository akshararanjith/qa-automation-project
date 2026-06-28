# from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout(driver):
    # driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "You logged into a secure area!" in driver.page_source

    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

    assert "You logged out of the secure area!" in driver.page_source

