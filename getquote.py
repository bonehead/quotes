#!/home/pi/berryconda3/bin/python
# conda execute
# env:
#  - python =3.6.1
#  - numpy

#* GetQuote.py                                   *#
#* Nicholas DiBari                               *#
#* Prints quote from brainyquote.com from author *# 
#* that user provides                            *#
#* --------------------------------------------- *#
#* Provides user interface for Get Quote         *#
#* DataBase Management                           *#
#* --------------------------------------------- *#

import sys # Get argument
import requests # Get HTML
import bs4 # Parsing HTML
import shelve # Database Management
from datetime import datetime # Date/Time Information
import random
import pandas as pd
import datetime
import csv

#1. Get Quote
def GetQuote():
    results = []
    cliche=[]
    topics=["fear","anger","spite","revenge","success","fearlessness","friends","love","India","World","Game of Thrones"]
    author = topics[random.randrange(0,len(topics),1)]
    print(author)

    #Open website with requests 
    HTML = requests.get('http://brainyquote.com/search_results.html?q=' + author )
    HTML.raise_for_status() #Check to ensure page was downloaded correctly

    #Create Beautiful Soup object to parse
    QuoteObject = bs4.BeautifulSoup(HTML.text, "html.parser")

    #Parse Beautiful Soup object for quote
    quotes = QuoteObject.select('#quotesList a') #Returns the element <a> located within class 'quotesList'

    for quote in quotes:
      if quote.get('title') == 'view quote':
          results.append(quote)
    num_quotes = len(results)
    for i in range(num_quotes):
        cliche.append(results[i].getText())

    pick = random.randrange(0,len(cliche),1)

    return cliche[pick],author

#2. Print Quote
def PrintQuotes(quotes):
    print(quotes)

#Main Function
def Main():
    


    quotes,author = GetQuote()
    PrintQuotes(quotes)
    fields=[0,quotes,datetime.datetime.now(),author]
    with open(r'D://abhishek_work//t1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)



if __name__ == '__main__':
    Main()