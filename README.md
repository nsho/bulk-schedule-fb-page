# **Selenium based Python script To bulk schedule in Facebook page ** 
Selenium script that bulks schedules posts to one's FB page from a csv import.

### Overview 
New repository after initial fork from https://github.com/ColombiaPython/social-media-automation

This modifies and extends the functionality of the forked file in two ways:

1) Posting to a 'page' instead of 'group.' 
2) Enabling the scheduling of multiple posts. (Note: FB still limits scheduling to six months in the future.)

Scheduling posts for a Facebook page can be a very tedious task which requires clicking into many different pages and menus and manually entering information for each post. A user then has to wait for the page to reload to schedule another post. With large post volume, this task can take hours. 

A few paid applications exist that allow a user to bulk schedule posts in advance directly from spreadsheet data. These can range from $15 to $30 for the lowest tiers of service, which may also limit the number of posts. However, this script allows one to schedule virtually unlimited posts to any facebook page of which they are an owner, which makes it a pretty valuable tool.

### Set Up Notes

Currently only text and single image posts are supported. (links can be substituted for text without issue.) See 'To Do' list at bottom for expected future functionality.

An example spreadsheet with required fields is provided in example.csv

After the script begins running, a firefox window will open. After the initial facebook login the user will be prompted to block/allow notifications from facebook.com.
#### The user will then need to manually click to block notifications.
After clicking this the script will continue in the firefox window until all posts are scheduled. Sit back and enjoy.


### Facebook Bulk Scheduling Set Up Instructions

* Verify you have Python 3.6.x installed
* Install [pip](https://bootstrap.pypa.io/get-pip.py)
* Install python virtual environments   
```
$ pip install virtualenv
```
* Create your virtual environment  
```
$ virtualenv venv
```
* Activate your virtual environment  
```
$ source venv/bin/activate
```
* Install Python bindings for Selenium  
```
$ (venv) pip install selenium
```
* Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and put path in line 49.

#### User Customization Steps

1) Modify path to trafficking spreadsheet where post information is stored (line 27). Spreadsheet should include four fields: schedule_date, message, image_path, image_type
2) Hardcode path to the scheduled posts page of your facebook page, of which you must be an owner. (Line 24)
3) User and password should be entered with arguments in command line. Alternatively these can be hardcoded directly into the script.

* Run the script  
```
$ (venv) python FBautopost.py -u 'login email' -p 'password'
```


### to do: 
validate csv file fields and encode format
emojis
add and process time of day field
if/else logic for missing values in file columnns 
video posts
multi image posts/carousel
allow notifications firefox popup avoidance
page_link as input variable
pics location folder as input variable
traffic sheet file as input variable
error messages
relocate geckodriver
chrome extension
Currently the script clicks 'Share Now' button for scheduled posts, which loads the scheduler and doesn't actually share the post. If one instead clicks the initial schedule button, it doesn't save and when one clicks schedule FB loads the schedule post menu a second time. I think this is a bug on the Facebook side and will require monitoring to ensure this script doesn't break if facebook makes an update. Noted in the script on line 89-91 as well.
