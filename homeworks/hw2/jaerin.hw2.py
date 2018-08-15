from bs4 import BeautifulSoup
import urllib2
import csv

mainpage="https://petitions.whitehouse.gov/petitions?page="
pages=[]
endpage=False
pagecount=0
while endpage==False:
    print "Opening page"+str(pagecount)
    page=BeautifulSoup(urllib2.urlopen(mainpage+str(pagecount)).read())
    if len(page.find_all("article"))==1: # If there is no petitionin this page
        endpage=True
        lastpagepetitions=len(pages[pagecount-1].find_all("article"))-1
    else:
        pages.append(page)
        pagecount+=1


indpages=[]
indtitl=[]

for j in range(0,len(pages)):
    if j==len(pages)-1:
        npetitions=lastpagepetitions
    else:
        npetitions=20
    for i in range(0,npetitions):
        oddid="even"
        if i%2==0:
            oddid="odd"
        addr=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find("a").attrs["href"]
        indpages.append(addr)
        titl=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find("a").get_text()
        indtitl.append(titl)


