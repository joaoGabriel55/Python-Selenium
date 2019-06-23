import getpass
import time

from selenium import webdriver
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

print("1-Happy path")
print("2-Test without email")
print("3-Test without password")
print("4-Test without anything")
print("5-Test both wrong")
print("=======================")
opInput = input("Chose the test: ")

op = int(opInput)

# Version 75 ChromeDriver
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.get(
    "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")


def inputEmail(email):
    fieldEmail = driver.find_element_by_id("username")
    fieldEmail.send_keys(email)


def inputPassword(password):
    fieldPass = driver.find_element_by_id("password")
    fieldPass.send_keys(password)


if(op == 1):
    # Inform the correct email and password for happy path test
    # -------------------------------------------------------------------------------------
    email = input('Enter your email: ')
    password = getpass.getpass('Enter your password: ')
    # --------------------------------------------------------------------------------------
    inputEmail(email)
    inputPassword(password)

if(op == 2):
    inputPassword("123456")

if(op == 3):
    inputEmail("j.quaresmasantos@hotmail.com")

if(op == 4):
    print("Nothing")

if(op == 5):
    inputEmail("j.quaresmasantos78@hotmail.com")
    inputPassword("123456")

if(op != 1):
    submit = driver.find_element_by_class_name("btn__primary--large").click()
    time.sleep(5)
    driver.quit()


wait = WebDriverWait(driver, 5)
