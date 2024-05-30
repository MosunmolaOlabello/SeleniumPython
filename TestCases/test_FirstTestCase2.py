from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

def test_FirstTestCase():
    driver=Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.maximize_window()
    #Enter the textbox
    driver.find_element(By.NAME,"emailAddress").send_keys("helloworld@gmail.com")
    driver.find_element(By.NAME, "firstName").send_keys("Mosunmola")
    driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("Joy")
    driver.find_element(By.NAME,"username").send_keys("Testing")
    driver.find_element(By.NAME,"emailAddress").clear()
    driver.find_element(By.NAME,"emailAddress").send_keys("himof@gmail.com")