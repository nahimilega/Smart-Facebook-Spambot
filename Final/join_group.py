from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
#from selenium.webdriver.firefox.options import Options
from time import sleep



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










def findNewGroups(keyWord='art', state="Delhi"):  
    '''
    made some changes here
    '''  
    driver.get("https://www.facebook.com/search/groups/?q={} {}&epa=SERP_TAB".format(state, keyWord))
    listOfJoinLinks = driver.find_elements_by_link_text("Join")
    for i in range(5):
        sleep(5)
        try:
            listOfJoinLinks[i].click()
        except:
            driver.find_element_by_class_name("_20-e").click()
            driver.find_element_by_link_text("Leave this page").click()
            continue    



def find_art_Groups_of_school():
    f5=open("college_of_potential_users.txt","r")
    lines = f5.read().split("\n")
    for i in lines:
        findNewGroups(i+"art")

def find_dance_Groups_of_school():
    f5=open("college_of_potential_users.txt","r")
    lines = f5.read().split("\n")
    for i in lines:
        findNewGroups(i+"dance")        

def find_generic_Groups_of_school():
    f5=open("college_of_potential_users.txt","r")
    lines = f5.read().split("\n")
    for i in lines:
        findNewGroups(i,"")




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
    
    
    
    aaa=input("Please enter the genre of group:  ")
    findNewGroups(aaa)
    

    '''
    except Exception as e:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit()
    '''    
if __name__ == '__main__':
    # get things rolling
    main()




#findNewGroups("sports")
'''
def post(content = "test content", link = "https://www.facebook.com/groups/1569538110008193/?fref=nf"):
    driver.get(link)
    #driver.find_element_by_xpath('//input[@pathholder="Write something..."]').send_keys("hihih")
    driver.find_element_

    sleep(5)
'''
login()
#findNewGroups("sports")

'''
#driver.find_element_by_link_text("Facebook").click()
driver.get("https://www.facebook.com/aayan.agarwal.14224")
sleep(5)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]/div[1]/span[1]/a[1]/div[2]/input[1]").send_keys("/home/noisymime/Pictures/Screenshot from 2018-09-03 16-11-19.png")
sleep(5)
#"/home/noisymime/Pictures/Screenshot from 2018-09-03 16-11-19.png"
sleep(5)
#driver.find_element_by_xpath("//div[text()='Upload Photos/Video']/following-sibling::div/input").sendKeys("/home/noisymime/Pictures/Screenshot from 2018-09-03 16-11-19.png")
    
#elem = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/span[1]/button[1]")
elem = driver.find_element_by_link_text("Share")
sleep(5)
elem.click()
sleep(10)
    


#driver.get("https://www.facebook.com/groups/payment.gateway.for.tech.support/?fref=nf")
#sleep(10)
#driver.get("https://www.facebook.com/groups/2038569416423458/?notif_id=1547316615801993&notif_t=group_r2j_approved")
#sleep(10)
#try:
    #elem = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]/input[1]")
#except:
#elem = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
#elem = driver.find_element_by_class_name("_4a0a img sp_OGGLuxGda8S_1_5x sx_d677b6").click()
sleep(15)

    

#elem.send_keys("hihih")
#sleep(10)
'''
driver.close()