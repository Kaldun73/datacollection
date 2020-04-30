from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['mailru']
collection = db.mailru

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://mail.ru/')
assert "Mail.ru" in driver.title

elem = driver.find_element_by_id('mailbox:login')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.ENTER)

elem = driver.find_element_by_id('mailbox:password')
elem.send_keys('NewPassword172')
elem.send_keys(Keys.ENTER)

# for i in range(15):
#     emails = driver.find_elements_by_css_selector('div.llc__content llc__content_pony-mode')
#     action = ActionChains(driver)
#     action.move_to_element(emails[-1])
#     action.perform()

driver.find_element_by_class_name('llc__content llc__content_pony-mode').send_keys(Keys.PAGE_DOWN)


emails = driver.find_elements_by_class_name('llc__content llc__content_pony-mode')

letter = {}
for email in emails:
    dict['sender'] = email.find_element_by_css_selector('span.ll-crpt').text
    dict['date'] = email.find_element_by_css_selector('div.llc__item llc__item_date').text
    dict['topic'] = email.find_element_by_css_selector('span.llc__subject').text
    dict['desc'] = email.find_element_by_css_selector('span.llc__snippet').text

    collection.update_one({'$set': letter}, upsert=True)

driver.quit()

