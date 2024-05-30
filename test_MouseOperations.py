from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_FirstTestCase():
    driver=Firefox()
    driver.get("https://www.zendwallet.com")
    driver.find_element(By.XPATH,"//button[text()='Login']")
    act = ActionChains(driver)
    # Click operation (Left Click)
    #act.click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()
    # Context Click (Right Click)
    #act.context_click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()

# Double Click
#act.double_click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()

act.move_to_element(driver.find_element(By.XPATH,"//p[text()='About']")).perform()