from bs4 import BeautifulSoup
import urllib2
import unicodecsv as csv

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
signs=[]
nentry=0
for j in range(1,len(pages)):
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
        #emptydictionary["indpags"] = adr
        indpages.append(addr)
        print "Address"
        titl=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find("a").get_text()
        #emptydictionary["indtitle"] = title
        indtitl.append(titl)
        print "Petition Title"
        issues=pages[j].find_all("article",{"class":"node node-petition node-promoted node-teaser node-"+oddid})[i/2].find_all("h6")
        indissues.append([])
        for k in range(len(issues)):
            indissues[nentry-1].append(issues[k].get_text())
        print "Issue Categories"
        signs.append(pages[j].find_all("span",{"class":"signatures-number"})[i].get_text())
        print "Number of Signatures"


dates=[]
for i in range(len(indpages)):
    print "Adding dates for petition #"+str(i+1)
    page=BeautifulSoup(urllib2.urlopen("https://petitions.whitehouse.gov/"+indpages[i]).read())
    datetexton=page.find_all("h4")[0].get_text().find(" on ")+4
    dates.append(page.find_all("h4")[0].get_text()[datetexton:])

print "Writing as .csv file"

zipped=zip(indtitl,dates,indissues,signs)

with open ('jaerin.petitions.csv','wb') as f:
    write=csv.writer(f)
    write.writerow(["Title","Date","Issue Category","Signatures"])
    for i in range(len(indpages)):
        write.writerow(zipped[i])

print "Finished. The .csv file is in your working directory."
