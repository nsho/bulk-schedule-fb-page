#!/usr/bin/python

from time import sleep
from datetime import date,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import pandas as pd
import argparse


#process terminal user and pwd input 
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", type=str, help="FB login")
ap.add_argument("-p","--pwd", type=str, help="password")
args = vars(ap.parse_args())

usr = args["user"] #alternatively, hardcode user email
pwd = args["pwd"] #altnernatively can hardcode pwd

#set link to page's publisher tool scheduled posts page
page_link = 'https://www.facebook.com/WeirdOffice/publishing_tools/?section=SCHEDULED_POSTS&sort[0]=scheduled_publish_time_ascending'

#read in post trafficking sheet as dataframe
infile = pd.read_csv('/Users/nsho/Desktop/WeirdOffice/FBPosts_test.csv', sep=',')
traffic_df = infile

def load_post_data(index,dataframe):
    'inputs and return column value for given index to set post field data as variables.'
    schedule_date, message, image_path, image_type = dataframe.iloc[index]
    return schedule_date,message,image_path,image_type
    
def schedule_post(page_link, traffic_df):
    'Schedules posts for facebook page up to 3 months in advance with spreadsheet data.'
    
    #load spreadsheet data as data frame
    schedule_date,message,image_path,image_type = load_post_data(0,traffic_df)
    
    #delete cache
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    # Path to geckodriver executable
    driver = webdriver.Firefox(executable_path='/anaconda3/bin/geckodriver')
    driver.implicitly_wait(5)
   
    #Login to facebook
    driver.get("http://www.facebook.com")
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    c = driver.find_element_by_id('loginbutton')
    c.click()

    # Go to the Facebook Page's Publisher Tools Schedule Posts Page
    driver.get(page_link)
    sleep(1)
    
    #get today's date
    today = date.today()
    date_today = today.strftime("%-m/%-d/%Y")
    
    for index in range(len(traffic_df)): #loop through each row in dataframe
        sleep(3) #wait to ensure proper page has loaded
        schedule_date,message,image_path,image_type = load_post_data(index,traffic_df) #load relevant row by index
        
        #click on +create new post button
        driver.find_element_by_xpath("//*[@data-testid='pages_publishing_tool_create_button']").click()
        sleep(1)
        
        #add message text to post
        post_box=driver.find_element_by_xpath("//*[@role='textbox']")
        post_box.send_keys(message)
        sleep(1)

        #add image if available
        if image_path != "" :
            addMediaMenu = driver.find_element_by_xpath("//*[@data-testid='photo-video-button']")
            addMediaMenu.click()
            driver.find_element_by_xpath("//*[@name='composer_photo']").send_keys(image_path)
            sleep(2)
            
        # Get the 'Share Now' button and click on it, which loads the scheduler and doesn't actually share the post.
        # FB loads the schedule post menu twice otherwise.
        # This is required and there is likely a bug on the Facebook side.
        Post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']") #gets share now button
        Post_button.click() #clicks on share now button
        sleep(2)
        
        #Get the date and reset 
        addDate = driver.find_element_by_xpath("//*[@placeholder='mm/dd/yyyy' and @value='{}']".format(date_today))
        addDate.click()
        sleep(1)
        addDate.clear() #clear current date
        addDate.send_keys(schedule_date) #add date to be scheduled
        sleep(1)
        
        #to do: customize time of day
        
        #submit post for scheduling
        driver.find_element_by_xpath("//*[@action='confirm' and @role='button' and @type='submit']").click()
        print('Post scheduled' + index + ' of ' + len(traffic_df))
        
        sleep(6) #allow page to reload to ensure button elements for creating next post are available
        
    print('Scheduling complete. Closing firefox.')
    driver.close() #close browser

schedule_post(page_link, traffic_df)
