from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.firefox.options import Options
from time import sleep

driver = webdriver.Firefox()

def findNewGroups(keyWord, state="Delhi"):    
    driver.get("https://www.facebook.com/search/groups/?q={} {}&epa=SERP_TAB".format(state, keyWord))
    listOfJoinLinks = driver.find_elements_by_link_text("Join")
    for i in range(5):
        sleep(5)
        listOfJoinLinks[i].click()


def login(user = "aayan.agarwal1919@gmail.com", pwd = "9818962189"):
    driver.get("http://www.facebook.com")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.send_keys(user)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    sleep(5)





#findNewGroups("sports")
def post(content = "test content", link = "https://www.facebook.com/groups/1569538110008193/?fref=nf"):
    driver.get(link)
    #driver.find_element_by_xpath('//input[@pathholder="Write something..."]').send_keys("hihih")
    driver.find_element_

    sleep(5)

login()


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

driver.close()
