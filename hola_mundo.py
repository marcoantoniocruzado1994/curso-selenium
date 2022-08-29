from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
path='C:\Drivers\chromedriver_win32\chromedriver.exe'
service_obj = Service(path)
driver = webdriver.Chrome(service=service_obj)

driver.get('https://testingqarvn.com.es/')
print("Bienbenidos a Selenium")
print("estamos abriendo la pagina >>>>>> " + driver.title)

