import getpass
import calendar
import os
import platform
import sys
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from time import sleep


def MAIN():
    driver =webdriver.Chrome()
    def upload():
            link="https://www.facebook.com/groups/390195291754122/"
            driver.get(link)
            file = open("myfile.txt", "r")
            description=file.readline()
            print(description)
            driver.find_element_by_name('xhpc_message_text').send_keys(description)
            path=file.readline()
            print(path)
            
            driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]/span[1]").send_keys(path)
            sleep(5)
            #elem = driver.find_element_by_link_text("Share")
    def findNewGroups(keyWord, state="Delhi"):    
        driver.get("https://www.facebook.com/search/groups/?q={} {}&epa=SERP_TAB".format(state, keyWord))
        listOfJoinLinks = driver.find_elements_by_link_text("Join")
        for i in range(5):
            sleep(5)
            listOfJoinLinks[i].click()


    def login(user = "aayan.agarwal1919@gmail.com", pwd = "9818962189"):
        driver.get("http://www.facebook.com")
        assert "Facebook" in driver.title
        
        options=Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        elem = driver.find_element_by_id("email")
        elem.send_keys(user)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        upload()
        sleep(5)


    #findNewGroups("sports")
    def post(content = "test content", link = "https://www.facebook.com/groups/1569538110008193/?fref=nf"):
        driver.get(link)
        driver.find_element_
        sleep(5)

    login()
    
    
if __name__== "__main__":
    MAIN()

