from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secrets
from time import sleep


#create a browser for eyefinity
def startEyeBrowser(): 
    eyeBrowser = webdriver.Chrome('C:/Users/jmorg/Downloads/chromedriver_win32/chromedriver')
    eyeBrowser.get(secrets.eyeUrl)
    sleep(3)
    return eyeBrowser
#end startEyeBrowser

#fill out username and password
def eyefinityLogIn(eyeBrowser):
    eyeUsrField = eyeBrowser.find_element_by_id('username')
    eyePassField = eyeBrowser.find_element_by_id('password')
    eyeUsrField.send_keys(secrets.eyeUser)
    eyePassField.send_keys(secrets.eyePass)

    eyeLogin = eyeBrowser.find_element_by_name('login').click()
    sleep(4)
#end eyefinityLogIn

#use search bar with patient name and DoB. The eyefinity database 
# will put the closest match as the top result
def patientSearch(eyeBrowser, patient, DoB):
    ptSearch = eyeBrowser.find_element_by_id('patientQuickSearch')
    ptSearch.send_keys(patient + ' ' + DoB) #TODO search with DoB combined with patient name. 
    sleep(3)
    ptSearch.send_keys(Keys.ENTER) #top match is auto highlighted so we only need to send ENTER
    sleep(3)
#end patientSearch

#Image management opens in a new tab so we save 
#the current handle before we switch to the new tab
def toggleBrowserHandle(eyeBrowser):
    eyeCurrHandle = eyeBrowser.window_handles[0]
    studyHandle = eyeBrowser.window_handles[1]
    eyeBrowser.switch_to_window(studyHandle)
    sleep(3)
#end toggleBrowserHandle


def uploadImage(eyeBrowser, imageList, num):
    studyButton = eyeBrowser.find_element_by_xpath('/html/body/app-mmiimagemanagement/app-initialview/div/div[1]/div[1]/app-studylistactions/div/div[2]/div[2]/button/span').click()
    sleep(3)

    selectFile = eyeBrowser.find_element_by_xpath('/html/body/app-mmiimagemanagement/app-initialview/div/app-imageuploader/div/div/div[3]/mat-grid-list/div/mat-grid-tile/figure/input')
    selectFile.send_keys(imageList[num])
    sleep(1)
    
    #ineraction with drop down menu to select test type
    testType = eyeBrowser.find_element_by_class_name('mat-select-placeholder').click()
    sleep(1)
    visualField = eyeBrowser.find_element_by_xpath("*//span[contains(text(), 'Visual Fields') and @class='mat-option-text']").click()
    sleep(1)

    uploadClick = eyeBrowser.find_element_by_xpath("*//span[contains(text(), 'Upload') and @class='mat-button-wrapper']").click()
    sleep(2)
#end uploadImage

def clickImageManagement(eyeBrowser):
    imageManagement = eyeBrowser.find_element_by_xpath('//*[@id="actions-tab"]/div[11]').click()


def main():

    
    patientFile = "C:/Users/jmorg/Downloads/" + patient
    patientFile = patientFile.replace(" ", "")

    #Create a list of all images to be uploaded
    imageList = []
    for num in range(numPhotos):
        imageList.append(patientFile + str(num + 1) + ".png")
        print (imageList[num]) #Remove
        uploadImage(eyeBrowser, num)


    print("Number of ordered photos: " + str(numPhotos))#Remove

if __name__ == "__main__":
    main()