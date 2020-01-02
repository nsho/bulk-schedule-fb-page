# **Selenium Scripts To Bulk Schedule in Facebook page ** 
Selenium script that bulks schedules posts to one's FB page from a csv import.

New repository after initial fork from https://github.com/ColombiaPython/social-media-automation

This modifies and extends the functionality of the forked file in two ways:

1) Posting to a 'page' instead of 'group.' 
2) Enabling the scheduling of multiple posts. (Note: FB still limits scheduling to six months in the future.)

Currently only text and single image posts are supported. (links can be substituted for text without issue.)

### Facebook Bulk Scheduling Set Up

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

#User Customization Steps

User and password should be entered with arguments in command line. Alternatively these can be hardcoded directly into the script.

Modify path to trafficking spreadsheet where post information is stored. Spreadsheet should include four fields: schedule_date, message, image_path, image_type

Hardcode path to the scheduled posts page of your facebook page, of which you must be an owner.

Add folder path where images referenced in spreadsheet image are stored. (Line  and the link of facebook groups

* Run the script  
```
$ (venv) python fbposter.py
```



###to do: 
#validate csv file fields and encode format
#emojis
#add and process time of day field
#if/else logic for missing values in file columnns 
#video posts
#multi image posts/carousel
#allow notifications firefox popup avoidance
#page_link as input variable
#pics location folder as input variable
#traffic sheet file as input variable
#error messages
#relocate geckodriver
