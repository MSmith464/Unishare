#########################
#      UNIT TESTS       #
#########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secrets
import unittest
import eyefinity


DoB = ' 09/01/1964' #this will not change for test patient

class TestEyefinity(unittest.TestCase):
    
    def test_UploadOneImage(self):
        numPhotos = 1
        patient = 'Test, Test'
        patientFile = "C:/Users/jmorg/Downloads/" + patient
        patientFile = patientFile.replace(" ", "")


        eyeBrowser = eyefinity.startEyeBrowser()

        eyefinity.eyefinityLogIn(eyeBrowser)

        eyefinity.patientSearch(eyeBrowser, patient, DoB)

        eyefinity.clickImageManagement(eyeBrowser)

        eyefinity.toggleBrowserHandle(eyeBrowser)

        #Create a list of all images to be uploaded
        imageList = []
        for num in range(numPhotos):
            imageList.append(patientFile + str(num + 1) + ".png")
            print (imageList[num]) #Remove
            eyefinity.uploadImage(eyeBrowser, imageList, num)

    def test_UploadTwoImages(self):
        numPhotos = 2
        patient = 'Test, Test'
        patientFile = "C:/Users/jmorg/Downloads/" + patient
        patientFile = patientFile.replace(" ", "")


        eyeBrowser = eyefinity.startEyeBrowser()

        eyefinity.eyefinityLogIn(eyeBrowser)

        eyefinity.patientSearch(eyeBrowser, patient, DoB)

        eyefinity.clickImageManagement(eyeBrowser)

        eyefinity.toggleBrowserHandle(eyeBrowser)

        #Create a list of all images to be uploaded
        imageList = []
        for num in range(numPhotos):
            imageList.append(patientFile + str(num + 1) + ".png")
            print (imageList[num]) #Remove
            eyefinity.uploadImage(eyeBrowser, imageList, num)
    
    def test_UploadThreeImages(self):
        numPhotos = 3
        patient = 'Test, Test'
        patientFile = "C:/Users/jmorg/Downloads/" + patient
        patientFile = patientFile.replace(" ", "")


        eyeBrowser = eyefinity.startEyeBrowser()

        eyefinity.eyefinityLogIn(eyeBrowser)

        eyefinity.patientSearch(eyeBrowser, patient, DoB)

        eyefinity.clickImageManagement(eyeBrowser)

        eyefinity.toggleBrowserHandle(eyeBrowser)

        #Create a list of all images to be uploaded
        imageList = []
        for num in range(numPhotos):
            imageList.append(patientFile + str(num + 1) + ".png")
            print (imageList[num]) #Remove
            eyefinity.uploadImage(eyeBrowser, imageList, num)




