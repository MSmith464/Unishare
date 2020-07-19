#Morgan Smith
#application to export images from one of our patient
#databases and import them into another

from selenium import webdriver
import secrets
import urllib
import unified
import eyefinity
import time

class Patient:
    def __init__(self, firstName, lastName, DoB, numPhotos):
        self.firstName = firstName
        self.lastName = lastName
        self.DoB = DoB
        self.numPhotos = numPhotos

lastName = input("Enter the patient's last name and press ENTER: ")
firstName = input("Enter the patient's first name and press ENTER: ")

#only eyefinity.py will use DoB
DoB = input ("Enter the patient's DoB in the form of MM/DD//YYYY and press ENTER: ") 
numPhotos = int(input("How many photos are we sending?  "))

patient = Patient(firstName, lastName, DoB, numPhotos)
patientName = patient.lastName + ', ' + patient.firstName

##########################
##  Export From Unified ##
##########################

#initiate Browser
browser = unified.startBrowser()

#log in to unified
unified.uniLogin(browser)

unified.findPatient(browser, patientName)

unified.selectPatient(browser)

for x in range (1,numPhotos + 1):
    unified.selectImage(browser, patientName, x)
time.sleep(2)

browser.close()

#end export from unified

##########################
## Import to Eyefinity  ##
##########################

patientFile = "C:/Users/jmorg/Downloads/" + patientName
patientFile = patientFile.replace(" ", "")

#start browser for eyefinity
eyeBrowser = eyefinity.startEyeBrowser()

eyefinity.eyefinityLogIn(eyeBrowser)

eyefinity.patientSearch(eyeBrowser, patientName, DoB)

#navigate to image management system in patient profile
eyefinity.clickImageManagement(eyeBrowser)

#image management opens in a new tab. toggle handle
eyefinity.toggleBrowserHandle(eyeBrowser)

#Create a list of all images to be uploaded
imageList = []
for num in range(numPhotos):
    imageList.append(patientFile + str(num + 1) + ".png")
    print (imageList[num]) #Remove
    eyefinity.uploadImage(eyeBrowser, imageList, num)


#end Import to Eyefinity
