
"""
Created on Mon Sep 30 08:30:25 2021

@author: bobtr
"""

import bs4 as bs
import urllib.request 

save_path = ''

sauce = urllib.request.urlopen('https://news.ycombinator.com/front').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav  
body = soup.body
text = soup.text
table= soup.table
div = soup.div
   
filename = "HackerDaily.txt"
f = open(filename, "w", encoding="utf-8")
nav = soup.nav  
body = soup.body
text = soup.text
table= soup.table
div = soup.div

for div in soup.find_all('a', attrs={"class" :  "titlelink"}): 
    f.write(div.text) 
    f.write('\n') 
    f.write(div.get("href"))
    f.write('\n') 
    f.write('\n') 

f.close()
