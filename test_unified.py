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
    def test_StartBrowser(self):
        unified.StartBrowser()

    def test_UniLogin(self):
        unified.UniLogin()

    def test_findPatient(self):
        patient = 'test, test'
        #Acessing search bar once logged in
        searchBar = browser.find_element_by_id('search-input')
        searchBar.send_keys(patient)
        time.sleep(3)

    def test_selectMatchingPatient(self):
        #select matching patient
        ptSelect = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/li/a')
        ptSelect.click()
        time.sleep(3)

