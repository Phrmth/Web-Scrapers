'''
Scraping news articles on bankrupcy to identify the recent organizations filing for bankrupcy. 
This is a web scraper bot to search google news for bankrupcy related news articles, further clicking on each news articles and 
extracting the text under each news link for the top 5 pages.

Python 2.7
'''

# 1
#importing packages
import urllib
import mechanize
from bs4 import BeautifulSoup
import re

#Mechanizing chrome
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]

# 2
#Search term and the URL
term = "bankrupcy"
query ="http://www.google.co.in/search?num=10&q="+term+"&tbm=nws"     # CHANGING THE NUMBER TO 5 FOR TESTING 
htmltext = br.open(query).read()

# 3
#Extracting results using beautifulsoup with div and other tags
soup = BeautifulSoup(htmltext)
search = soup.findAll('div',attrs={'id':'search'})
searchtext = str(search[0])

soup1 = BeautifulSoup(searchtext)
list_items = soup1.findAll('a',href = True)  # to test the tags


# 4
# regular expression to get just the URL, for loop on the various tags under the search tag, to find the search results(links)
# URLs appended in X
regex = "q(?!.*q=).*?&amp"
pattern = re.compile(regex)

x = []
for tr in list_items:
    soup2 = BeautifulSoup(str(tr))
    links = soup2.findAll('a',href = True)
    sourcelinks = links
    sourceurl = re.findall(pattern,str(sourcelinks))
    if len(sourceurl)> 0 :
        x.append(str(sourceurl[0].replace("q=","").replace("&amp","")))
        
        
        
# 5
#Looping x URLS to get the <P> contents as text

regex = "(?!.*<p>).*?<\p"
pattern = re.compile(regex)
s= []
story= []
counter = 0
s1 = []
for url in x:
    try:
        text = br.open(url,timeout=5).read()
        soup3 = BeautifulSoup(text)
        search = soup3.findAll('p')
        for p in search:
            soup4 = BeautifulSoup(str(p),"html.parser")
            story.append(str(soup4))
            s.append(para.text)   
        if len(s) > 0:    
            s1.append(s)
    except:
        continue

# 6 
# joining all the list items togather 

text = " ".join(s).encode('utf-8')
len(text)

print "Extract complete"



## Identifying the organizations names listed under bankrupcy news text using Named Entity Recognition

stem_text = list()
stanford_classifier = 'c:\stanford\stanford-ner-2016-10-31\classifiers\english.all.3class.distsim.crf.ser.gz'
stanford_ner_path = 'C:\stanford\stanford-ner-2016-10-31\stanford-ner.jar'

# Creating Tagger Object
st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
stemmer = SnowballStemmer("english")

text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])


clean_text = re.sub('[^A-Za-z0-9\.]+', ' ', text)

tokenized_text = word_tokenize(clean_text)

classified_text = st.tag(tokenized_text)


# getting only the tokens tagged as Organization
check = []
for i,j in classified_text:
    if j == "ORGANIZATION":
        i.lower()
        check.append(i)

# removing common bankrupcy terms and websites names reporting bankrupcy news
check_clean = []

bankrupcy_terms = ["reuters" , "thestreet", "Bloomberg", "bennett", "Forbes","marklittle (little)","mlive" ,
                   "marketwatch", "Corp", "co", "Co.", "agency","Court", "customer", "District", "Federal","Financial",
                   "Inc.", "Inc","Ltd","Brunswick", "arbor", "Altair", "ann", "arizona" , "Bennett" , "claren road",
                   "claren", "Connecticut", "BIA", "Bankruptcy" ,"CMHC", "COFINA", "ERS", "ABI", "USA", "U.S.A","U.S.", "CBS4","CBS"]

check_clean = [i for i in check if i not in bankrupcy_terms]
print check_clean
