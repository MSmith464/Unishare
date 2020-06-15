from selenium import webdriver
import time
import urllib.request
import secrets

lastName = input("Enter the patient's last name and press ENTER: ")
firstName = input("Enter the patient's first name and press ENTER: ")
DoB = input ("Enter the patient's DoB in the form of MM/DD//YYYY and press ENTER: ")
numPhotos = input("How many photos are we sending?  ")

patient = lastName + ', ' + firstName

#function to export the image selected from Unified
def DownloadImage():
    moreOptions = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[8]')
    moreOptions.click()
    clickDownload = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[11]/i')
    clickDownload.click()

    currWindow = browser.window_handles[0]#save current browser tab before we switch to new tab
    newTab = browser.window_handles[1]  #switch to new tab containg the .png
    browser.switch_to_window(newTab)

    imagePath = browser.find_element_by_xpath('/html/body/img')
    imageSrc = imagePath.get_attribute('src')
    urllib.request.urlretrieve(imageSrc, 'C:/Users/jmorg/Downloads/test.png')   #save image to drive

    browser.close() #close newTab after we collect the image. Switch back to original tab.
    browser.switch_to_window(currWindow)
#end DownloadImage

#Unified needs to unselect the current photo to select the next. 
#To download another photo, reset must be called 
def reset():
    #clicks the first square to bringphoto thumbnails back
    square = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/button/i').click() 
    unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]/div[2]').click()
#end reset

#webdriver to be used for exporting images from Unified
browser = webdriver.Chrome('C:/Users//jmorg/Downloads/chromedriver_win32/chromedriver')
browser.get('http://unified.gallery')
time.sleep(6)

#Login to Unified.gallery
def UniLogin():
    #Variables for the username,password, and login elements
    userField = browser.find_element_by_xpath('//*[@id="login-container"]/div/div[2]/div/div/form/div[1]/input')  
    passField = browser.find_element_by_xpath('//*[@id="login-container"]/div/div[2]/div/div/form/div[2]/input') 
    loginButton = browser.find_element_by_class_name('login-button.ng-scope')

    #enter username and password
    userField.send_keys(secrets.uniUser)
    passField.send_keys(secrets.uniPass)
    loginButton.click()
    time.sleep(4)
#end UniLogin

UniLogin()

#Acessing search bar once logged in
searchBar = browser.find_element_by_id('search-input')
searchBar.send_keys(patient)
time.sleep(3)

#select matching patient
ptSelect = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/li/a')
ptSelect.click()
time.sleep(3)

#select left most photo
firstSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]/img')
firstSelect.click()
time.sleep(4)

DownloadImage()
reset()
time.sleep(2)
#visual fields and gluacoma suspects will have 2 images per patient.
#Mac Degen patients will only have one. Find a way to select images by dates?

browser.close()



