from selenium import webdriver

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



while(True):
    pass
