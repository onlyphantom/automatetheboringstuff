from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Safari()
browser.get('https://xkcd.com')

try:
    # Works also:
    # a = browser.find_element_by_id('comic').find_element_by_tag_name('img')
    time.sleep(2)
    browser.execute_script('window.scrollTo(0, document.getElementById("comic").scrollHeight);')
    time.sleep(3)
    a = browser.find_element_by_xpath('//*[@id="comic"]/img')
    print("Image Source:", a.get_attribute('src'))
    # TODO: save the source into a txt file

    prev = browser.find_element_by_link_text("< Prev")
    # In other browsers: prev.click()
    prev.send_keys(Keys.RETURN)
    print("Navigated to previous entry.")
except:
    print('Unable to find comic image.')