from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_FirstTestCase():
    driver=Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.find_element(By.NAME,"emailAddress").send_keys("Hello@gmail.com")
    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
    time.sleep(10)