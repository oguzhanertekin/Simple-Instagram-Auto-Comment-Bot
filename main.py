
import time
import pyautogui
from selenium import webdriver
import itertools
import pandas as pd



file=open("FILE NAME","r")  # ENTER FILE PATH - comments.txt
nameList=[]

for name in file.readlines():
    name=name.strip("\n ")
    nameList.append(name)
combinationList=list(itertools.combinations(nameList,2))


''' username=input("Kullanıcı adını girin: ")
password=input("Şifrenizi girin: ") '''
username="username"  # enter username
password="password"  # enter password

driver=webdriver.Chrome(executable_path="...../AppData/Local/Temp/Rar$DRa16152.19119/chromedriver.exe")  # Find this location and copy paste here
driver.get("https://www.instagram.com")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
time.sleep(3)
driver.find_element_by_xpath("//button[text()='Şimdi Değil']").click()
time.sleep(2)

driver.get("URL")  # Instagram post URL


for name in combinationList:
    driver.find_element_by_class_name('Ypffh').click()
    driver.find_element_by_class_name('Ypffh').send_keys("{} {}".format(name[0],name[1]))
    driver.find_element_by_xpath("//button[text()='Paylaş']").click()
    time.sleep(5)
    driver.refresh()
   

