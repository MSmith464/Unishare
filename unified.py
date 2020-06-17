from selenium import webdriver
import time
import urllib.request
import secrets

lastName = input("Enter the patient's last name and press ENTER: ")
firstName = input("Enter the patient's first name and press ENTER: ")
DoB = input ("Enter the patient's DoB in the form of MM/DD//YYYY and press ENTER: ")
numPhotos = int(input("How many photos are we sending?  "))

patient = lastName + ', ' + firstName

#function to export the image selected from Unified
def DownloadImage(num):
    moreOptions = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[8]')
    moreOptions.click()

    #trying to find the OD/OS tag
    test = browser.find_element_by_css_selector('body > div.navbar.navbar-fixed-bottom.transparent.ng-scope > div > div > div > ng-transclude > div.gallery-slider.ng-scope.ng-isolate-scope.ng-hide > div:nth-child(1) > a.gallery-item.noselect.ng-scope.selected > div.caption.noselect > span.right.ng-binding')
    test1 = test.text
    
    print(test1)
    clickDownload = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/button[11]/i')
    clickDownload.click()

    #create file name for right and left eye
    imageName = patient + str(num) + '.png'
    
    imageName = imageName.replace(' ', '')

    currWindow = browser.window_handles[0]#save current browser tab before we switch to new tab
    newTab = browser.window_handles[1]  #switch to new tab containg the .png
    browser.switch_to_window(newTab)

    imagePath = browser.find_element_by_xpath('/html/body/img')
    imageSrc = imagePath.get_attribute('src')
    urllib.request.urlretrieve(imageSrc, 'C:/Users/jmorg/Downloads/'+ imageName)   #save image to drive

    browser.close() #close newTab after we collect the image. Switch back to original tab.
    browser.switch_to_window(currWindow)
#end DownloadImage

#Unified needs to unselect the current photo to select the next. 
#To download another photo, reset must be called 
def reset(num):
    #clicks the first square to bringphoto thumbnails back
    square = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/button/i').click() 

    if num == 1:
        unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]/div[2]')
    elif num == 2:
        unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[2]')
    elif num == 3: 
        unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[3]')
    elif num == 4:
        unselect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[4]')

    unselect.click()
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
def SelectImage(num):

    if num == 1:
        imageSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[1]')
    elif num == 2:
        imageSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[2]')
    elif num == 3:
        imageSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[3]')
    elif num == 4: 
        imageSelect = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ng-transclude/div[1]/div[1]/a[4]')
    else:
        return
    
    time.sleep(1)
    imageSelect.click()
    DownloadImage(num)
    reset(num)
#end SelectImage()
for x in range (1,numPhotos + 1):
    SelectImage(x)
time.sleep(2)
#visual fields and gluacoma suspects will have 2 images per patient.
#Mac Degen patients will only have one. Find a way to select images by dates?

browser.close()



