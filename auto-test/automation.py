from selenium import webdriver
chrome_browser = webdriver.Chrome('.\chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')




assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')


