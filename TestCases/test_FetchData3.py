from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_FirstTestCase():
    driver=Firefox()
    driver.get("https://www.zendwallet.com/register")
    obj=Select(driver.find_element(By.NAME,"country"))
    obj.select_by_visible_text("Nigeria")
    # fetch selected option
    print(obj.first_selected_option.text)
    # fetch all available options
    for op in obj.options:
        print(op.text)