def test_page_title(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert driver.title == "The Internet"