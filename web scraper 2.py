'''
This is a web scraper which requires a one time login to a URL and post login can fetch the data from different links/buttons and write it back to a file on disk.

Note- advisable to run on jupyter notebook for easy access to outputs at different levels. 
Written in python 2.7
'''


# 1
from bs4 import BeautifulSoup
import urllib
import mechanize
import re
import cookielib
import pandas as pd
import csv

#Mechanizing chrome
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]


#2
#First time run to set the cookies with user name and password 

import cookielib 
import urllib2 
import mechanize 

# Browser 
br = mechanize.Browser() 

# Enable cookie support for urllib2 
cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

# Broser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 

# ?? 
br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'chrome' ) ] 

# authenticate 
br.open("https://www.xxx.com/Login.aspx") 
br.select_form("loginform") 
br["username"] = 'xxx'  # or read from json file
br["password"] = 'xxx'
res = br.submit() 

print "Success!\n"


#3
# getting the list of all the countries first to further get inside each country link and fetch the data inside each country listed

query ="http://country.xxx.com/AllCountries.aspx#"
htmltext = br.open(query).read()
soup = BeautifulSoup(htmltext)

regex = r'href=[\'"]?([^\'" >]+)'
pattern = re.compile(regex)
countries = []
li = soup.select("ul > li > ul > li > a")

for link in li:
    linkurl = re.findall(pattern,str(link))
    countries.append(linkurl[0])
len(countries)


#4
regex = r'href=[\'"]?([^\'" >]+)'
pattern = re.compile(regex)

Creditriskarticles = []
countries_list = []
for each in countries:
    url = "http://country.xxx.com"+each
    eachcountrytext = br.open(url).read()
    countrysoup = BeautifulSoup(eachcountrytext)

    for l2 in countrysoup1.findAll(attrs={'id' : 'ctl00_navMenu_ctrl4_divSub'}):
        countrysoup2 = BeautifulSoup(str(l2))

    li = countrysoup2.select("ul > li > a")

    souprisk = BeautifulSoup(str(li[0]))
    riskURL = souprisk.findAll('a',href = True)
    riskURL = str(riskURL).replace(" ","%20")      # for the countries with space, replaceing the space in thier URL with %20
    linkurlrisk = re.findall(pattern,str(riskURL))

    if len(linkurlrisk) > 0: 
        Creditriskarticles.append(linkurlrisk[0])
        countries_list.append(each)
        print len(Creditriskarticles),len(countries_list)


#5
scores = []
country = []
for i,j in enumerate(Creditriskarticles): 
    j_URL = "http://country.xxx.com"+j

    j_text = br.open(j_URL)
    j_soup = BeautifulSoup(j_text)
    for j1 in j_soup.findAll(attrs={'id' : 'ctl00_PageContent_ArticleContent'}):
        j_soup1 = BeautifulSoup(str(j1))

            
        table = j_soup1.findAll('tr')
        if table[2].isNull:
            scores.append("-")
            print "Table has Null value "
        else: 
            scores.append(table[2].text)
            country.append(countries_list[i])



#7  Writing output

counter = 0
result= []
for i in scores:
    tbl_contents = country[counter]+str(i).replace("\n",",")
    tbl_contents = tbl_contents.replace("/","")
    result.append(str(tbl_contents))


# Open File
resultFyle = open("output.csv",'wb')

# Create Writer Object
wr = csv.writer(resultFyle, dialect='excel')

# Write Data to File
for r in result:
    resultFyle.write(r + "\n")
resultFyle.close()
print('file written!')
