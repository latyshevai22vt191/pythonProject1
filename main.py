from datetime import datetime, date
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def settingData(filename, date):
    f = open(filename, 'w')
    f.write(date)
    f.close()


def isEmptyFile(filemane):
    f = open(filemane, 'r')
    if f.read() == '':
        return True
    else:
        return False


def getDateFromFile(filename):
    f = open(filename, 'r')
    return f.read()


def getDate(str):
    dateElem = str.split('.')
    return date(int(dateElem[2]), int(dateElem[1]), int(dateElem[0]))


def actionsMoveOffset(driver, elem, xof, yof):
    actions = ActionChains(driver)
    actions.move_to_element(to_element=elem).move_by_offset(xoffset=xof, yoffset=yof).click()
    time.sleep(4)
    actions.perform()
    actions.reset_actions()
    time.sleep(3)


# open url
browser = webdriver.Chrome()
browser.get('http://bi.gks.ru/biportal/contourbi.jsp?allsol=1&solution=Dashboard&project=%2FDashboard%2FPrices_week')
browser.maximize_window()
time.sleep(3)

# move to table
browser.find_element(By.CSS_SELECTOR, '#x-auto-29__x-auto-25 .x-tab-strip-text').click()
time.sleep(3)

# move to filter region
fo = browser.find_element(By.ID, 'x-auto-155')
actionsMoveOffset(browser, fo, 60, 0)

list_region = browser.find_elements(By.CSS_SELECTOR, '.x-view-item-checkbox')

# pick all_regions
list_region[0].click()
time.sleep(3)

# pick цфо
list_region[2].click()
time.sleep(3)

# pick OK
browser.find_element(By.CSS_SELECTOR, '#x-auto-196 .x-btn-text').click()
time.sleep(5)

# pick filter data
data = browser.find_element(By.ID, 'x-auto-208')
actionsMoveOffset(browser, data, 30, 0)

# pick sorted date
browser.find_element(By.ID, 'x-auto-226').click()
time.sleep(3)

# pick actual data
actual_data = browser.find_elements(By.CSS_SELECTOR, '.x-view-item-checkbox')
current_data = browser.find_element(By.XPATH,
                                    '/html/body/div[4]/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]').text
if isEmptyFile("date.txt"):
    settingData("date.txt", current_data)
else:
    if getDate(getDateFromFile('date.txt')) < getDate(current_data):
        settingData('date.txt', current_data)
    else:
        exit()
actual_data[1].click()
time.sleep(3)

# pick Ok
browser.find_element(By.CSS_SELECTOR, '#x-auto-232 .x-btn-text').click()
time.sleep(3)

# pick settings
browser.find_element(By.CSS_SELECTOR, '#x-auto-134').click()
time.sleep(5)

# pick expirt excel
browser.find_element(By.CSS_SELECTOR, '#x-auto-284 .x-btn-image').click()
time.sleep(10)

# download
browser.find_element(By.LINK_TEXT, 'Скачать').click()
time.sleep(10)
