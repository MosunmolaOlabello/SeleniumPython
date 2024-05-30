from selenium.webdriver import Firefox

def test_FirstTestCase():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.maximize_window()
    # Fetching Title
    print("The title of the page is " + driver.title)
    # Fetch URL of Page
    print("Page URL is " + driver.current_url)
    # Fetch complete page HTML
    print("**********************************************************************")
    print(driver.page_source)
