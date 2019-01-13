import getpass
import calendar
import os
import platform
import sys
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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




def person_detail():
    f1=open("potential_users.txt","r")
    all_links=f1.readlines()
    for link in all_links:
        try:
            driver.get(link)
            driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]").click()
            sleep(4)
            driver.find_element_by_xpath("//a[@class='_5pwr _Interaction__ProfileSectionEducation']").click()
            
            sleep(2)
            a=driver.find_element_by_id("pagelet_eduwork")
            
            l=a.text

            i=0
            sl=[]
            nl=l.split("\n")
            a=nl
            while(i<len(a)):
                
                if(a[i]=="EDUCATION" or a[i]=="No schools/universities to show"):
                    i=i+1
                    
                elif(a[i]=="WORK"):
                    
                    while(a[i]=="EDUCATION"):
                        i=i+1
                else:
                    sl.append(a[i])
                    i=i+1
                   
                
            i=0
            f5=open("college_of_potential_users.txt","a")        
            while(i<len(sl)):
                
                if(i%2==0):
                    f5.write(sl[i]+"\n")
                i=i+1    
            f5.close()    
        except:
            pass
            
        
          
        

def find_people_intrested_in_the_post():
    '''
    This part is completed
    '''
    
    a=driver.find_element_by_id("reaction_profile_browser1")
    
    html=a.get_attribute('innerHTML')
    soup=BeautifulSoup(html,"html.parser")
    array=[]
    i=0
    for link in soup.find_all('a'):
        a=link.get('href')
        if(a[0:5]=="https"):
            i=i+1 
            if(i%2==0 ):
                array.append(link.get('href'))
    
    f1=open("potential_users.txt","a")
    for i in array:
        f1.write(i+"\n")
   
    

def find_all_posts_made():
    '''
    This is done

    '''
    f1=open("link_of_all_the_post.txt","r")
    all_links=f1.readlines()
    for link in all_links:
        
        driver.get(link)
        sleep(10)
        try:
            driver.find_element_by_xpath("/html[1]/body[1]/div[9]/div[2]/div[1]/a[1]/i[1]").click()
        except:     
            continue
        finally:    
            driver.find_elements_by_xpath("//i[@class='_3j7l _2p78 _9-- _hly']")[0].click()
            sleep(7)
            
            #To find the people who have liked the post
            find_people_intrested_in_the_post()
        




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
    ########################Here we have logged it


    find_all_posts_made()



    '''
    except Exception as e:
        print("There's some error in log in.")
        print(sys.exc_info()[0])
        exit()
    '''    

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------    

def main():
    ids = ["https://en-gb.facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]

    if len(ids) > 0:
        # Getting email and password from user to login into his/her profile
        email = 'aaruuraa91@gmail.com'
        password = '9999975654'
        #getpass.getpass('Enter your Facebook Password: ')

        print("\nStarting Scraping...")
        #############################For login
        login(email, password)
        ############################For findind the details of the users who hae liked the post
        person_detail()
        sleep(10) 
        driver.close()
    else:
        print("Input file is empty..")




if __name__ == '__main__':
    # get things rolling
    main()