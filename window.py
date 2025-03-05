import json

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


l = []

driver = webdriver.Chrome(options=chrome_options)
table = driver.find_element(by=By.ID,value='manualArrangeCourseTable')
content = table.find_elements(by=By.TAG_NAME,value='tr')
for i in content:
    td = i.find_elements(by=By.TAG_NAME,value='td')

    tmp = []
    for j in td:
        if j.get_attribute('title'):
            curricular = j.get_attribute('title')
        # print(curricular)
        # if curricular:
            tmp.append(curricular)
        else:
            tmp.append(" ")
    l.append(tmp)
l = l[1:9]
for i in range(len(l[0])):
    for j in range(len(l)):
        if l[i][j] != ' ':
            l[i+1].insert(j,' ')
dict = {'星期一':[],'星期二':[],'星期三':[],'星期四':[],'星期五':[],'星期六':[],'星期日':[]}
for i in range(len(l)):
    for j in range(len(l)):
        if j == 1:
            dict['星期一'].append(l[i][j])
        elif j == 2:
            dict['星期二'].append(l[i][j])
        elif j == 3:
            dict['星期三'].append(l[i][j])
        elif j == 4:
            dict['星期四'].append(l[i][j])
        elif j == 5:
            dict['星期五'].append(l[i][j])
        elif j == 6:
            dict['星期六'].append(l[i][j])
        elif j == 7:
            dict['星期日'].append(l[i][j])
for i,j in dict.items():
    print(i,j)