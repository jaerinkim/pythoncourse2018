## Go to https://polisci.wustl.edu/faculty/specialization
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import urllib2
import csv 

web_address = 'https://polisci.wustl.edu/faculty/specialization'

web_page=urllib2.urlopen(web_address)
soup=BeautifulSoup(web_page.read())
profs=soup.find_all('a')[14:58]
prodict=[]
proname=[]
proemail=[]
for i in range(len(profs)):
    prodict.append('https://polisci.wustl.edu'+profs[i].attrs['href'])
    if i in [7,16,33]:
        prodict[i]=profs[i].attrs['href']
        proname.append(str(BeautifulSoup(urllib2.urlopen(prodict[i]).read()).find('h1',{'class':"pane-title"}))[23:-5])
    if i not in [7,16,33]:
        email=str(BeautifulSoup(urllib2.urlopen(prodict[i]).read()).find('div', {'class':"field field-name-field-person-email field-type-email field-label-inline clearfix"}).find('div',{'class':"field-items"}).find('div',{'class':"field-item even"}))[45:-10]
        proemail.append(email[:len(email)/2-1])
        title=str(BeautifulSoup(urllib2.urlopen(prodict[i]).read()).find('div',{'class':"field
                                                                                field-name-field-person-titles
                                                                                field-type-text field-label-hidden"}).find('div',{'class':"field-items"}).find('div',{'class':"field-items
                                                                                                                                                     even"})
                                                                         
    else:
        proemail.append(None)

