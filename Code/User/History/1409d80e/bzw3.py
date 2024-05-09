import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options() #Chrome settings

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(), #Download directory to here
    "download.prompt_for_download": False, #No dialogue
    "download.directory_upgrade": True, #Default
    "safebrowsing.enabled": True #Default
})

#Initalize chrome driver and go to imperva login page
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://management.service.imperva.com/')
input("Login and set time range for the reports")

projects_list = [
    {'name': 'mcdonalds', 'id': "1829881"},
    {'name': 'meshulam', 'id': "1824908"}
    ]

for project in projects_list:
    print("Reporting: " + project["name"])
    browser.get('https://management.service.imperva.com/?caid=' + project["id"])

    download_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "DownloadReportButtonWrapper")))
    download_button.click()

    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "DownloadReportButtonWrapper")))

while(True):
    pass
