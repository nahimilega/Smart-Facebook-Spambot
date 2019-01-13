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
    def upload(link="https://www.facebook.com/groups/390195291754122/"):
            
            
            file = open("myfile.txt", "r")
            description=file.readline()
             
            driver.get(link)
            
            print(description)
            driver.find_element_by_name('xhpc_message_text').send_keys(description)
            imageToBeUploadedPath = "C:\\Users\\Archit\\Desktop\\timetable.png"
            print(imageToBeUploadedPath)
            sleep(5)
            try:
                elem = driver.find_element_by_link_text("Add photo/video")
                sleep(5)
                elem.click()
                sleep(2)
                elem = driver.find_element_by_link_text("Upload Photos/Videos")
                sleep(2)
                elem.find_element_by_xpath("..").find_elements_by_tag_name("div")[1].find_element_by_tag_name("input").send_keys(imageToBeUploadedPath)
                driver.implicitly_wait(10)
                elem = driver.find_element_by_xpath('//span[contains(text(), "Post")]')
                driver.implicitly_wait(10)
                elem1 = elem.find_element_by_xpath("..")
                id = elem1.get_attribute("id")
                sleep(5)
                elem = driver.find_element_by_link_text("Share")
            except:
                pass
            #elem = driver.find_element_by_link_text("Share")




    def login(user = "aaruuraa91@gmail.com", pwd = "9999975654"):
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







    
    














    login()
    
    
if __name__== "__main__":
    MAIN()
