# ---1---
# initial step
from bs4 import BeautifulSoup
import urllib
import mechanize
import re
import cookielib

#Mechanizing chrome
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]


query ="http://www.coface.com/Economic-Studies-and-Country-Risks/Comparative-table-of-country-assessments"
htmltext = br.open(query).read()
soup = BeautifulSoup(htmltext)
#print soup



# ---2---
# Extracting table data
import pandas
import csv

li = soup.select("div > div > div > table > tr ")
coface = []
stringnew = []
#print li
for i in li:
    rating = str(i.text).replace(",","")
    rating = rating.replace("\n",",")
    rating = rating.replace('/\s\s+/g', ' ')
       
    coface.append(rating)



# ---3---
# Cleaning the extracted html table

stringnew_all = []

for i in coface:
    print i
    string_split = i.split(",")
    #print string_split
    stringnew = ""
    for j in string_split:
        j = j.replace("   ","")
        j = j.replace("'","")
        if len(j) > 0:
            stringnew = stringnew+","+j
    print stringnew
    stringnew_all.append(str(stringnew))

# ---4---
# Copying to CSV
# Open File
cofacerating = open("coface.csv",'wb')

# Create Writer Object
wr = csv.writer(cofacerating, dialect='excel')

# Write Data to File
for r in stringnew_all:
    cofacerating.write(r + "\n")
cofacerating.close()
print('file written!')
