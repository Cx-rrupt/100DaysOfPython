# Day 51 of 100 Days of Python
# Project Name: Automated Internet Complaint Twitter Bot
# Things i implemented: Selenium, Time Module

# Import Modules
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Necessary Constants
DRIVER_PATH = 'C:/Users/matth/OneDrive/Documents/ProgrammingLanguagesLearning/Python/Development/chromedriver'
PROMISED_DOWNLOAD_SPEED = 25
PROMISED_UPLOAD_SPEED = 3.75
TWITTER_EMAIL = 'matthewadrianus@gmail.com'
TWITTER_PASSWORD = 'GB2rqLAvhemwUgH'

class InternetSpeedTwitterBot:
    # Constructor
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.upload_speed = 0
        self.download_speed = 0
    # Getting Internet Speed
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        speed_test = self.driver.find_element_by_class_name('start-text')
        speed_test.click() 
        sleep(45)
        download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.upload_speed = float(upload_speed.text.strip())
        self.download_speed = float(download_speed.text.strip())
    # Tweeting to Internet Service Provider
    def tweet_at_isp(self):
        # Go to Twitter Login Page
        self.driver.get('https://twitter.com/login') 
        sleep(3)
        # Input Username
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        # Input Password
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')  
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        # Input Tweet Message
        sleep(3)
        message_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message_box.click()
        message_box.send_keys(f"Salam sejahtera bagi @FirstMediaCares,\n\n Mengapa Internet Speed saya {self.download_speed}down/{self.upload_speed}up, ketika dijanjikan {PROMISED_DOWNLOAD_SPEED}down/{PROMISED_UPLOAD_SPEED}?")
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
    # Close Driver
    def terminate_driver(self):
        self.driver.quit()

# Driver Code
complaint_bot = InternetSpeedTwitterBot(DRIVER_PATH)
# Get Internet Speed
complaint_bot.get_internet_speed()
# If Speed not according to promise, tweet at Internet Service Provider
if complaint_bot.download_speed<PROMISED_DOWNLOAD_SPEED and complaint_bot.upload_speed<PROMISED_UPLOAD_SPEED:
    complaint_bot.tweet_at_isp()
# Terminate the Driver
complaint_bot.terminate_driver()
