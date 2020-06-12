**UniShare** - a program to automate our image exporting tasks.

**The Problem**

A special machine that we bring into our office once a month is used to take detailed scans of the patient's eyes.
Along with the scans, visual field testing is performed on the glaucoma suspects. The results of these tests are presented
as images on the testing devices.

Both the scans and the test images are then sent to a cloud database that we have access to. 
The problem this causes is that we also need these images in the patient's records which are on another online database.
This means the technicians have to login to database A, find the recent images sent from the testing devices, download the images,
login to database B, locate the same patient's records, and upload the images there.

**The Solution**

The goal is to take images that are already stored on Unified.gallery (those sent from the testing devices) and export
them to our cloud based patient data management system Eyefinity, automating the previously mentioned mundane tasks.
Launching this program should be the only task left to the user after patient testing is complete.

UniShare uses the Selenium library for Python.
Selenium makes it very easy to access and interact with HTML and CSS elements. 
All usernames, passwords, and patient test data are imported from a private file... So make ya own!
