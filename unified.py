from selenium import webdriver
import time
import urllib.request
import secrets

#function to export the image selected from unified
def downloadImage():
    moreOptions = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[8]')
    moreOptions.click()
    clickDownload = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[11]/i')
    clickDownload.click()

    currWindow = browser.window_handles[0]
    newTab = browser.window_handles[1]  #switch to new tab containg the .png
    browser.switch_to_window(newTab)

    imagePath = browser.find_element_by_xpath('/html/body/img')
    imageSrc = imagePath.get_attribute('src')
    print(imageSrc) #remove this after testing
    urllib.request.urlretrieve(imageSrc, 'C:/Users/jmorg/Downloads/test.png')
    browser.close()
    browser.switch_to_window(currWindow)

#unified needs to unselect the current photo to select the next. 
# To download another photo, reset must be called 
def reset():
        #clicks the first square to bringphoto thumbnails back
        square = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/button/i').click() 
        unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]/div[2]').click()


browser = webdriver.Chrome('C:/Users//jmorg/Downloads/chromedriver_win32/chromedriver')
browser.get('http://unified.gallery')
windowHandler = browser.window_handles

time.sleep(6)
#Variables for the username,password, and login elements
userField = browser.find_element_by_xpath('//*[@id="login-container"]/div/div[2]/div/div/form/div[1]/input')  
passField = browser.find_element_by_xpath('//*[@id="login-container"]/div/div[2]/div/div/form/div[2]/input') 
loginButton = browser.find_element_by_class_name('login-button.ng-scope')

#enter username and password
userField.send_keys(secrets.uniUser)
passField.send_keys(secrets.uniPass)
loginButton.click()

time.sleep(6)
#Acessing search bar once logged in
searchBar = browser.find_element_by_id('search-input')
searchBar.send_keys(secrets.patient)
time.sleep(3)

#select matching patient
ptSelect = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/li/a')
ptSelect.click()
time.sleep(3)

#select left most photo
firstSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]/img')
firstSelect.click()
time.sleep(4)
downloadImage()
reset()




