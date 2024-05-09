from selenium import webdriver
from selenium.webdriver.common.by import By

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

    browser.implicitly_wait(2) #Wait 2 seconds
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") #Scroll to the buttom
    browser.implicitly_wait(0.5) #Wait 0.5 seconds
    browser.execute_script("window.scrollTo(0, 0)") #Scroll to the top

    button = browser.find_element(By.ID, "DownloadReportButtonWrapper")
    button.click()
    print("Clicked download")

while(True):
    pass
