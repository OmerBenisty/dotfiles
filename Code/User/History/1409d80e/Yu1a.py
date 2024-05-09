from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Initalize chrome driver and go to imperva login page
browser = webdriver.Chrome()
browser.get('https://management.service.imperva.com/')
input("Login and set time range for the reports")

projects_list = [
    {'name': 'mcdonalds', 'id': "1829881"}
    ]

for project in projects_list:
    print("Reporting: " + project["name"])
    browser.get('https://management.service.imperva.com/?caid=' + project["id"])

    download_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "DownloadReportButtonWrapper")))
    download_button.click()
while(True):
    pass
