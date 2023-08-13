import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    try:
        browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    finally:
        time.sleep(5)
        browser.quit()






