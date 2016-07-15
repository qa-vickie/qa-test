from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 



browser = webdriver.Firefox()

browser.get('https://staging.joordev.com')
elem_login_btn = browser.find_element_by_css_selector('a.login-button')
elem_login_btn.click()

elem_username = browser.find_element_by_id ('login-name')
elem_username.send_keys('qa_test')

elem_pwd = browser.find_element_by_name('data[User][password]')
elem_pwd.send_keys('joorqaautomation')

elem_submit= browser.find_element_by_css_selector('input.gold-button.center.sign-in')
elem_submit.submit()

elem_messages = browser.find_element_by_css_selector ('li.j-dropdown-header.account.float_left.uppercase.messages.localizejs')
elem_messages.click()
time.sleep(1)

elem_send_message = browser.find_element_by_partial_link_text ('Send')

elem_send_message = browser.find_element_by_link_text ('Send a Message')
elem_send_message.click()
time.sleep(1)

elem_to_all_connections = browser.find_element_by_id ('MessageSendToAllConnections')
elem_to_all_connections.click() 

elem_subject= browser.find_element_by_id ('MessageSubject')
elem_subject.send_keys('test subject')

elem_body= browser.find_element_by_id ('MessageBody')
elem_body.send_keys ('test message body')


elem_send_btn = browser.find_element_by_css_selector('a.button.button-3.float_left.j-form-ajax-submit')
elem_send_btn.click()
time.sleep(1)

elem_confirmation= browser.find_element_by_class_name('jQueryMsg')
if elem_confirmation.text == 'Your message has been sent':
	print 'OK'
else:
	print 'Failed'

#time.sleep (60)
time.sleep (5)

browser.quit()

