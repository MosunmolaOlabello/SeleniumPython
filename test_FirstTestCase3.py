from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup(scope="modules"):
    global driver
    driver=Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.maximize_window()
    yield
    driver.close()


def test_all(environment_setup):
    driver.find_element(By.NAME,"emailAddress").send_keys("Mosunmolaolabello@gmail.com")
    driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Mosunmola")
    driver.find_element(By.NAME,"lastName").send_keys("Olabello")
    driver.find_element(By.NAME,"username").send_keys("Mosun")
    driver.find_element(By.NAME,"password").send_keys("Mosunbaby&9")
    # working on checkbox
    driver.find_element(By.XPATH,"//span[@class='chakra-checkbox__control css-1gtsxek']").click()
    # work on dropdown
    obj= Select(driver.find_element(By.NAME,"country0"))


    #obj.select_by_index(2)
    #obj.select_by_value("Nigeria")
    obj.select_by_visible_text("Nigeria")
    # work on button
    driver.find_element(By.XPATH,"//button[@class='chakra-button css-1wa7fdh']").click()
    assert driver.current_url == "https://www.zendwallet.com/register"

