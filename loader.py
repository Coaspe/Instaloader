from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,urllib.request
import requests
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("./chromedriver.exe")


driver.get("https://www.instagram.com/")

def check_exists_by_xpath(xpath) -> bool:
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_css_selector(check_exists_by_css_selector):
    try:
        driver.find_element_by_css_selector(check_exists_by_css_selector)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_class_name(check_exists_by_class_name):
    try:
        driver.find_element_by_class_name(check_exists_by_class_name)
    except NoSuchElementException:
        return False
    return True

time.sleep(3)
username = driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")
login = driver.find_element_by_css_selector("button[type='submit']").click()

time.sleep(5)
notnow = driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()
time.sleep(3)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()
flag = True
nextBtn = driver.find_element_by_class_name("glyphsSpriteChevron_circle_shadow_right")
name = ""

all_user = driver.find_elements_by_class_name("OE3OK ")
all_user[0].click()
for k in range(len(all_user)):
    time.sleep(2)
    if check_exists_by_css_selector("svg[aria-label='일시 정지']"):
        driver.find_element_by_css_selector("svg[aria-label='일시 정지']").click()
    num = len(driver.find_elements_by_class_name("_7zQEa"))
    print(num)
    for i in range(num):
        shortcode = driver.current_url.split("/")[-2]
        if check_exists_by_css_selector("svg[aria-label='일시 정지']"):
            driver.find_element_by_css_selector("svg[aria-label='일시 정지']").click()
        if not check_exists_by_class_name("OFkrO"):
            print("no video")
            download_img_url = driver.find_element_by_xpath(
                "//*[@id='react-root']/section/div[1]/div/div[5]/section/div/div[1]/div/div/img").get_attribute('srcset').split(" ")[0]
            print(download_img_url)
            urllib.request.urlretrieve(download_img_url, '{}.jpg'.format(shortcode))
            driver.find_element_by_xpath(
                "//*[@id='react-root']/section/div[1]/div/div[5]/section/div/button[2]/div").click()
            continue
        print("yes video")
        download_url = driver.find_element_by_tag_name('source').get_attribute('src')
        print(download_url)
        urllib.request.urlretrieve(download_url, '{}.mp4'.format(shortcode))
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='react-root']/section/div[1]/div/div[5]/section/div/button[2]/div").click()
