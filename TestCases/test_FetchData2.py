from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def test_FirstTestCase():
    driver = Firefox()
    driver.get("https://web.facebook.com/?_rdc=1&_rdr")
    driver.maximize_window()
    print("Text on link is :- " + driver.find_element(By.CLASS_NAME,"_8esh").text)
    # Fetching attribute value of element
    print("Value of button is " + driver.find_element(By.XPATH,"//button[@type='submit']").get_attribute("class"))