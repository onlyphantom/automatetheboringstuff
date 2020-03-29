from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

MAX = 5

browser = webdriver.Safari()
browser.get('https://xkcd.com')

with open('img.txt', 'w') as f:

    for i in range(MAX):
        try:
            # Works also:
            # a = browser.find_element_by_id('comic').find_element_by_tag_name('img')
            time.sleep(1)
            browser.execute_script('window.scrollTo(0, document.getElementById("comic").scrollHeight);')
            time.sleep(3)
            a = browser.find_element_by_xpath('//*[@id="comic"]/img')
            src = a.get_attribute('src')
            print("Image Source:", src)
            f.write(src + '\n')

            prev = browser.find_element_by_link_text("< Prev")
            # In other browsers: prev.click()
            prev.send_keys(Keys.RETURN)
            print("Navigated to previous entry.")
        except:
            print('Unable to find comic image.')
