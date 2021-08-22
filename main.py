from selenium import webdriver
import time, urllib.request
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("./chromedriver.exe")
def check_exists_by_xpath(xpath) -> bool:
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_css_selector(css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_class_name(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True


def story_loader():
    driver.get("https://www.instagram.com/")

    time.sleep(3)
    username = driver.find_element_by_css_selector("input[name='username']")
    password = driver.find_element_by_css_selector("input[name='password']")

    username.clear()
    password.clear()
    username.send_keys("")
    password.send_keys("")
    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()

    all_user = driver.find_elements_by_class_name("OE3OK ")
    all_user[0].click()

    while (check_exists_by_xpath(
            "//*[@id='react-root']/section/div[1]/div/div[5]/section/div/button[2]/div")):
        shortcode = driver.current_url.split("/")[-2]
        if check_exists_by_css_selector("svg[aria-label='일시 정지']"):
            driver.find_element_by_css_selector("svg[aria-label='일시 정지']").click()
        if not check_exists_by_class_name("OFkrO"):
            print("no video")
            download_img_url = driver.find_element_by_xpath(
                "//*[@id='react-root']/section/div[1]/div/div[5]/section/div/div[1]/div/div/img").get_attribute(
                'srcset').split(" ")[0]
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

def get_photo_from_profile(account_name : str) :
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://www.instagram.com/")

    time.sleep(3)
    username = driver.find_element_by_css_selector("input[name='username']")
    password = driver.find_element_by_css_selector("input[name='password']")

    username.clear()
    password.clear()
    username.send_keys("")
    password.send_keys("")
    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(), '나중에 하기')]").click()
    driver.get("https://www.instagram.com/"+account_name)
    time.sleep(2)

    download_img_url = driver.find_elements_by_class_name("FFVAD")

    for i in range(len(download_img_url)):
        shortcode = driver.current_url.split("/")[-2] + str(i)
        print(download_img_url[i].get_attribute('src'))
        urllib.request.urlretrieve(download_img_url[i].get_attribute('src'), '{}.jpg'.format(shortcode))
