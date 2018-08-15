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
indissues=[]
nentry=0
for j in range(0,len(pages)):
    if j==len(pages)-1:
        npetitions=lastpagepetitions
    else:
        npetitions=20
    for i in range(0,npetitions):
        oddid="even"
        if i%2==0:
            oddid="odd"
        nentry+=1
        print "Working on entry #"+str(nentry)+":"
        addr=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find("a").attrs["href"]
        indpages.append(addr)
        print "Address"
        titl=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find("a").get_text()
        indtitl.append(titl)
        print "Petition Title"
        issues=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find_all("h6")
        indissues.append([])
        for k in range(len(issues)):
            indissues[j*20+i].append(issues[k].get_text())
        print "Issue Categories"

dates=[]
for i in range(len(indpages)):
    print "Adding dates for petition #"+str(i+1)
    page=BeautifulSoup(urllib2.urlopen("https://petitions.whitehouse.gov/"+indpages[i]).read())
    datetexton=page.find_all("h4")[0].get_text().find(" on ")+4
    dates.append(page.find_all("h4")[0].get_text()[datetexton:])



