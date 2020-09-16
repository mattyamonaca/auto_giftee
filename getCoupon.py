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
    email = "facebook adress"
    password = "facebook pass"
    mail_form = driver.find_element_by_id("email")
    pass_form = driver.find_element_by_id("pass")

    mail_form.send_keys(email)
    pass_form.send_keys(password)
    
    login_btn = driver.find_element_by_id("loginbutton")
    
    login_btn.click()

    return driver
    
def work(driver):
    base_url = "https://giftee.co/account/mypage/sent/"
    url_list = []
    code_list = []
    #driver.get(url)

    i = 1
    while True:
        url = base_url + str(i)
        driver.get(url)
        coupon_items =  driver.find_elements_by_class_name("links")
        for item in coupon_items:
            coupon_url = item.find_elements_by_css_selector(".btn.btn_medium.white.fluid")[2].get_attribute("href")
            url_list.append(coupon_url)
        print(len(coupon_items))
        if len(coupon_items) != 8:
            break
        else:
            i += 1
        time.sleep(1)

    for coupon_url in url_list:
        code_urls = get_code_urls(coupon_url)
        for code_url in code_urls:
            time.sleep(1)
            code_list.append(get_code(code_url))
    df = pd.DataFrame({"code":code_list})
    df.to_csv("code_list.csv")
            


def get_code_urls(coupon_url):
    driver.get(coupon_url)
    code_items = driver.find_elements_by_class_name("ticket-content")
    code_urls = []
    for code_item in code_items:
        code_urls.append(code_item.get_attribute("href"))
    return code_urls

def get_code(code_url):
    driver.get(code_url)
    code = driver.find_element_by_id("copy_target0").text
    print(code)
    return code
    
        
        

    

    


driver = set_driver(debug=True)
login_url = "https://giftee.co/account/auth/facebook"
logined_driver = login(driver,login_url)


work(logined_driver)

#JS解析 developertool使え
