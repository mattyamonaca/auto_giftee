from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

from selenium.webdriver.support.select import Select

def set_driver(debug=True):
    if debug == False:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
        return driver
    else:
        driver = webdriver.Chrome(executable_path="./chromedriver")
        return driver


def login(driver,url):
    driver.get(url)
    email = "facebook addres"
    password = "facebook password"
    mail_form = driver.find_element_by_id("email")
    pass_form = driver.find_element_by_id("pass")

    mail_form.send_keys(email)
    pass_form.send_keys(password)
    
    login_btn = driver.find_element_by_id("loginbutton")
    
    login_btn.click()

    return driver
    
def work(driver):
    url = "https://giftee.co/gifts/detail/1395"
    password = "JCB password"
    driver.get(url)

    time.sleep(3)

    num = 5
    opt = driver.find_element_by_name("cart_form[number_of_orders]")
    select = Select(opt)
    select.select_by_index(num)

    check = driver.find_elements_by_class_name("sku_inner")
    print(check)
    check[1].click()

    time.sleep(3)

    make_card = driver.find_element_by_id("giftShowSubmitBtn")
    make_card.click()

    time.sleep(3)

    preview_btn = driver.find_elements_by_class_name("action-area")[0]
    preview_btn.click()

    time.sleep(3)

    cart_btn = driver.find_element_by_css_selector(".btn-rectangle.cyan-primary.fluid")
    cart_btn.click()

    time.sleep(3)

    order_btn = driver.find_element_by_id("submitOrder")
    order_btn.click()

    time.sleep(10)

    card_pass = driver.find_element_by_name("password")
    card_pass.send_keys(password)
    card_pass.submit()
    


driver = set_driver(debug=True)
login_url = "https://giftee.co/account/auth/facebook"
logined_driver = login(driver,login_url)

for i in range(0,25):
    work(logined_driver)

#JS解析 developertool使え
