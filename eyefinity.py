from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secrets
from time import sleep

eyeBrowser = webdriver.Chrome('C:/Users/jmorg/Downloads/chromedriver_win32/chromedriver')
eyeBrowser.get(secrets.eyeUrl)
sleep(3)

#fill out username and password
eyeUsrField = eyeBrowser.find_element_by_id('username')
eyePassField = eyeBrowser.find_element_by_id('password')
eyeUsrField.send_keys(secrets.eyeUser)
eyePassField.send_keys(secrets.eyePass)

eyeLogin = eyeBrowser.find_element_by_name('login').click()
sleep(4)

#use search bar with patient name and DoB. The eyefinity database 
# will put the closest match as the top result
ptSearch = eyeBrowser.find_element_by_id('patientQuickSearch')
ptSearch.send_keys(secrets.patient)
sleep(2)
ptSearch.send_keys(Keys.ENTER) #top match is auto highlighted so we only need to send ENTER
sleep(3)

imageManagement = eyeBrowser.find_element_by_xpath('//*[@id="actions-tab"]/div[11]').click()

#Image management opens in a new tab so we save 
#the current handle before we switch to the new tab
eyeCurrHandle = eyeBrowser.window_handles[0]
studyHandle = eyeBrowser.window_handles[1]
eyeBrowser.switch_to_window(studyHandle)
sleep(3)

testFile = 'C:/Users/jmorg/Downloads/test.png'
studyButton = eyeBrowser.find_element_by_xpath('/html/body/app-mmiimagemanagement/app-initialview/div/div[1]/div[1]/app-studylistactions/div/div[2]/div[2]/button/span').click()
sleep(3)
selectFile = eyeBrowser.find_element_by_xpath('/html/body/app-mmiimagemanagement/app-initialview/div/app-imageuploader/div/div/div[3]/mat-grid-list/div/mat-grid-tile/figure/input')
selectFile.send_keys(testFile)