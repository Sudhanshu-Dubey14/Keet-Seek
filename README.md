# Grand Challenge Submission for MtM 2020

This project was developed as part of [Master the Mainframe 2020](http://masterthemainframe.com/)'s Grand Challenge.
When I was doing the challenges myself, I found that most of the people get stuck when an error occurs.
They usually don't know where to find the error code and how to search the web for solution even if they do get the error code.
*Debugging is an art after all!!!*

So for the Grand Challenge, I decided to make a project which will find the error code for the user and use that error code to search the IBM documentation to get relevant debugging info.
For this I use the [Zowe Python SDK](https://zowe-client-python-sdk.readthedocs.io/en/latest/) and other python packages mentioned below.

## Pre-requisites

Please install the below mentioned packages before using this project:

1. [Zowe Python SDK](https://zowe-client-python-sdk.readthedocs.io/en/latest/usage/installation.html)
1. [Selenium](https://pypi.org/project/selenium/)
1. [Geckodriver](https://github.com/mozilla/geckodriver/releases) (cause we use Selenium with Firefox)
1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
1. [lxml parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)
1. [Google Python SDK](https://pypi.org/project/google/)

## Usage

1. You need to have a valid [Zowe profile](https://docs.zowe.org/stable/user-guide/ze-profiles.html). If you have used Zowe before, especially the Zowe plugin for VS Code, then it will be easier. Open `config.py` and replace `<profile_name>` with the name of your Zowe profile. For example, if the name of your profile is "mtm2020" then your `config.py` will look like this:
	connection = {
	    "plugin_profile": "mtm2020"
	}
1. Now you just need to submit the job using `jobs.py`:
	- If the JCL file is on the mainframe, run the command as: `python jobs.py mainframe "<file_path>"` where `<file_path>` is the path of the JCL file on mainframe. For example:
	`python jobs.py mainframe "Z99999.JCL(HLOWRLD)"`

If the job is completed successfully, that's great! But if an error occurs then the script will do it's work. ;-)
