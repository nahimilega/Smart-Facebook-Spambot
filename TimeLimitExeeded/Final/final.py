import getpass
import calendar
import os
import platform
import sys
import urllib.request

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



















def find_all_posts_made():
    f1=open("link_of_all_the_post.txt","r")
    all_links=f1.readlines()
    for link in all_links:
        print(link)
        driver.get(link)
        





def main():
    ids = ["https://en-gb.facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]

    if len(ids) > 0:
        # Getting email and password from user to login into his/her profile
        email = 'aayan.agrawal1919@gmail.com'
        password = '9818962189'
        #getpass.getpass('Enter your Facebook Password: ')

        print("\nStarting Scraping...")

        login(email, password)
        #scrap_profile(ids)
        delay(10000)
        driver.close()
    else:
        print("Input file is empty..")





def login(email, password):
    '''
    This function is used to login using fake account details
    '''

    try:
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
        find_all_posts_made()

    except Exception as e:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit()



# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    # get things rolling
    main()