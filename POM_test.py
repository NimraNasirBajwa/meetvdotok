import smtplib
from email.message import EmailMessage
import clipboard
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class login:
    Username_xpath= "//input[@id='username']"
    JoinRoom_button = "//button[normalize-space()='Join room']"
    copyURL = "//button[normalize-space()='Copy Room URL']"

    def __init__(self, driver):
        global wait
        self.driver = driver
        wait = WebDriverWait(self.driver, 20)


    def task1(self,User_Name1):
        name = self.driver.find_element(By.XPATH, self.Username_xpath)
        name.send_keys(User_Name1)
        btnclik = self.driver.find_element(By.XPATH, self.JoinRoom_button)
        btnclik.click()

    def copyurl(self):
        copy_url = self.driver.find_element(By.XPATH, self.copyURL)
        copy_url.click()

    def paste_url(self):
        global message
        message = clipboard.paste()


