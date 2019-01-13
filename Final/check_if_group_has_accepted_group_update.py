import getpass
import calendar
import os
import platform
import sys
import urllib.request
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# -------------------------------------------------------------
# -------------------------------------------------------------


# Global Variables

driver = None

# whether to download photos or not
download_uploaded_photos = True
download_friends_photos = True

# whether to download the full image or its thumbnail (small size)
# if small size is True then it will be very quick else if its false then it will open each photo to download it
# and it will take much more time
friends_small_size = True
photos_small_size = True

total_scrolls = 5000
current_scrolls = 0
scroll_time = 5

old_height = 0




#def get_list_of_groups(info):
#to do string parsing
'''
def transfer_pending_groups(still_pending):
    f2=open("pending.txt","w")
    for i in still_pending:
        f2.write(i+"\n")
    f2.close()
       
'''

def find_in_file(list_of_current):
    '''
    name 
    genure
    link
    '''
    f1=open("pending.txt","r")
    lines = f1.read().split("\n")
    i=0
    j=0
    still_pending=[]
    transfer_links=[]
    while(i<len(lines)):
        if(i):
            transfer_links.append(lines[i+1])
            transfer_links.append(lines[i+2])
        else:
            still_pending.append(lines[i])
            still_pending.append(lines[i+1])
            still_pending.append(lines[i+2])

        i=i+3
        f1.close()
        #transfer_pending_groups(still_pending)

def get_current_groups():
    '''
    Assumption subne description dala hai
    '''
    html_string=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]")
    #html_string=driver.find_element_by_class_name("uiList _153e _509- _4ki")
    info_about_present_group=html_string.text
    print(info_about_present_group)
    list_of_current=info_about_present_group.split("\n")
    find_in_file(list_of_current)
    #get_list_of_groups(info_about_present_group)
    






def main():
    ids = ["https://en-gb.facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]

    if len(ids) > 0:
        # Getting email and password from user to login into his/her profile
        email = 'aaruuraa91@gmail.com'
        password = '9999975654'
        #getpass.getpass('Enter your Facebook Password: ')

        print("\nStarting Scraping...")

        login(email, password)
        #scrap_profile(ids)
        #person_detail()
        sleep(7) 
        driver.close()
    else:
        print("Input file is empty..")





def login(email, password):
    '''
    This function is used to login using fake account details
    '''

    #try:
    global driver

    options = Options()

    #  Code to disable notifications pop up of Chrome Browser
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    # options.add_argument("headless")

    try:
        platform_ = platform.system().lower()
        if platform_ in ['linux', 'darwin']:
            driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
        else:
            driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
    except:
        print("Kindly replace the Chrome Web Driver with the latest one from"
                "http://chromedriver.chromium.org/downloads"
                "\nYour OS: {}".format(platform_)
                )
        exit()

    driver.get("https://en-gb.facebook.com")
    driver.maximize_window()

    # filling the form
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('pass').send_keys(password)

    # clicking on login button
    driver.find_element_by_id('loginbutton').click()

    ##################The work starts
    driver.get("https://www.facebook.com/bookmarks/groups/")
    sleep(10)
    get_current_groups()

    '''
    except Exception as e:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit()
    '''    
    


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    # get things rolling
    main()