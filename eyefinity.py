from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secrets
from time import sleep

eyeBrowser = webdriver.Chrome('C:/Users/jmorg/Downloads/chromedriver_win32/chromedriver')
eyeBrowser.get(secrets.eyeUrl)
sleep(3)

eyeUsrField = eyeBrowser.find_element_by_id('username')
eyePassField = eyeBrowser.find_element_by_id('password')

eyeUsrField.send_keys(secrets.eyeUser)
eyePassField.send_keys(secrets.eyePass)

eyeLogin = eyeBrowser.find_element_by_name('login').click()
sleep(4)

ptSearch = eyeBrowser.find_element_by_id('patientQuickSearch')
ptSearch.send_keys(secrets.patient)
sleep(2)
ptSearch.send_keys(Keys.ENTER)

sleep(3)

imageManagement = eyeBrowser.find_element_by_xpath('//*[@id="actions-tab"]/div[11]').click()

studyButton = eyeBrowser.find_element_by_text('upload new study').click()

selectFile = eyeBrowser.find_element_by_text('Select files').click()