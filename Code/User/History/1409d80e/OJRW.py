import os
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

today_date = datetime.now().strftime("%d-%m-%Y") # Today
last_week_date = (datetime.now() - timedelta(days = 7)).strftime("%d-%m-%Y") # Lastweek

script_directory = os.getcwd()
chrome_options = Options() # Chrome settings

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": script_directory, #Download directory to here
    "download.prompt_for_download": False, #No dialogue
    "download.directory_upgrade": True, #Default
    "safebrowsing.enabled": True #Default
})

#Initalize chrome driver and go to imperva login page
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://management.service.imperva.com/')
input("Login and set time range for the reports, than press enter")

#All projects we want to generate a report for
projects_list = [
    {'name': 'mcdonalds', 'id': "1829881"},
    {'name': 'meshulam', 'id': "1824908"},
    {'name': 'azrieli', 'id': "1832330"}
    ]

for project in projects_list:
    print("Reporting: " + project["name"])

    #You can access a website dashboard by passing the variable caid with the project ID to the imperva url
    browser.get('https://management.service.imperva.com/?caid=' + project["id"]) #

    #Finds the download button and wait for it to be clickable
    download_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "DownloadReportButtonWrapper"))) 
    download_button.click() #Click it!

    #Wait for the button to be avaliable again (meaning the file has been downloaded)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "DownloadReportButtonWrapper")))

    #Rename the fine when it exists
    file_found = True
    while file_found:
        for file in os.listdir(script_directory):
            if "Homepage" in file:
                os.rename(script_directory + "/" + file, "imperva_" + project['name'] + "_weekly_report_" + last_week_date + "-" + today_date + ".pdf")
                file_found = False
                break
                