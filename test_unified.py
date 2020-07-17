#########################
#      UNIT TESTS       #
#########################

from selenium import webdriver
import time
import urllib.request
import secrets
import unittest
import unified

class TestUnified (unittest.TestCase):

    def test_DownloadSingleImage(self):
        patient = 'Test, Test'
        browser = unified.startBrowser()

        unified.uniLogin(browser)

        unified.findPatient(browser, patient)
        unified.selectPatient(browser)

        num = 1
        unified.selectImage(browser, patient, num)
        browser.close()

    def test_DownloadTwoImages(self):
        patient = 'Test, Test'
        browser = unified.startBrowser()

        unified.uniLogin(browser)

        unified.findPatient(browser, patient)
        unified.selectPatient(browser)

        num = 2
        unified.selectImage(browser, patient, num)
        browser.close()

    def test_DownloadThreeImages(self):
        patient = 'Test, Test'
        browser = unified.startBrowser()

        unified.uniLogin(browser)

        unified.findPatient(browser, patient)
        unified.selectPatient(browser)

        num = 3
        unified.selectImage(browser, patient, num)
        browser.close()
    
    

