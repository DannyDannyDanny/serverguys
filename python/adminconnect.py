print('importing imports')
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#### HELPER METHODS

def update_file():
    file_creds = "status.txt"
    file = open(file_creds, "w")
    current_time = time.localtime()
    time_date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)
    n_users = get_users()
    file_contents = "Users " + str(n_users) + "\nlast updated: " + str(time_date)
    print(file_contents)
    file.write(file_contents)
    file.close()

def get_creds():
    eml = ""
    pwd = ""
    try:
        print("locating creds")
        file_creds = "/Users/DTH/Documents/Qub/qub_creds.txt"
        file = open(file_creds, "r")
        file_contents = file.read()
        print("extracting creds")
        eml = file_contents.split("\n")[0]
        pwd = file_contents.split("\n")[1]
        file.close()
    except FileNotFoundError as e:
        print("creds could not be located")
        print(e.strerror)
        print("shutting down")
        sys.exit("creds file could not be located")
        # TODO does this work when called from outside?
    print("creds extracted")
    return eml,pwd


def get_users():
    print('init driver')
    driver = webdriver.Firefox()
    n_users = -1
    try:
        print('entering admin module')
        print('go to website')
        #url = "http://0.0.0.0:8890/"
        url = "https://qub-test.firebaseapp.com/"
        driver.get(url)

        print('filling webform')
        field_eml = driver.find_element_by_id("txtEmail")
        field_pwd = driver.find_element_by_id("txtPassword")

        eml,pwd = get_creds()
        field_eml.send_keys(eml)
        field_pwd.send_keys(pwd)
        print('loggin in')
        driver.find_element_by_xpath("//*[@id=\"loginArea\"]/p/button").click()

        print("counting rows")
        rows = driver.find_elements_by_css_selector("tr")
        print("storing count")
        n_users = len(rows)

        #time.sleep(5)
        #print('driver close')
        #driver.close()
    except selenium.common.exceptions.NoSuchElementException as e:
        print("could not fill out webform")
        print(e)
        print("shutting down")
        sys.exit("creds file could not be located")
    return n_users

##### MAIN
update_file()
