#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup

# ### Step 1: Send an HTTP request to the web page ###

# url01 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
# data01 = requests.get(url01).text
# #print(data01)

# # ## Step 2: Parse the HTML content ###

# # What is parsing?
# # In simple words, parsing refers to the process of analyzing a string of 
# # text or a data structure, usually following a set of rules or grammar, 
# # to understand its structure and meaning. Parsing involves breaking down a 
# # piece of text or data into its individual components or elements, and then 
# # analyzing those components to extract the desired information or to 
# # understand their relationships and meanings.

# soup01 = BeautifulSoup(data01, 'html5lib')

# # ### Step 3: Identify the HTML tags ###

# # netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# # #print(netflix_data)

# # # Working on HTML table 

# # # These are the following tags which are used while creating HTML tables.

# # # <table>: This tag is a root tag used to define the start and end of the table. 
# # # All the content of the table is enclosed within these tags.

# # # <tr>: This tag is used to define a table row. Each row of the table is defined 
# # # within this tag.

# # # <td>: This tag is used to define a table cell. Each cell of the table is defined 
# # # within this tag. You can specify the content of the cell between the opening and 
# # # closing tags.

# # # <th>: This tag is used to define a header cell in the table. The header cell is 
# # # used to describe the contents of a column or row. By default, the text inside a 
# # # tag is bold and centered.

# # # <tbody>: This is the main content of the table, which is defined using the tag. 
# # # It contains one or more rows of elements.

# # ### Step 4: Use a BeautifulSoup method for extracting data ###

# # # First we isolate the body of the table which contains all the information
# # # Then we loop through each row and find all the column values for each row
# # for row in soup01.find("tbody").find_all('tr'):
# #     col = row.find_all("td")
# #     date = col[0].text
# #     Open = col[1].text
# #     high = col[2].text
# #     low = col[3].text
# #     close = col[4].text
# #     adj_close = col[5].text
# #     volume = col[6].text
    
# #     # Finally we append the data of each row to the table
# #     netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

# # print(netflix_data)

# # ### Step 5: Print the extracted data ###

# # print(netflix_data.head())

# #Extracting data using pandas library

# # What is read_html in pandas library?

# # pd.read_html(url) is a function provided by the pandas library in Python 
# # that is used to extract tables from HTML web pages. It takes in a URL as 
# # input and returns a list of all the tables found on the web page.

# read_html_pandas_data = pd.read_html(url01)

# read_html_pandas_data = pd.read_html(str(soup01))

# #print(read_html_pandas_data)

url02 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'

html_data = requests.get(url02).text
#print(html_data)

soup02 = BeautifulSoup(html_data, 'html5lib') 
print(soup02.title)

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup02.find("tbody").find_all("tr"):
    col       = row.find_all("td")
    date      = col[0].text #ADD_CODE
    Open      = col[1].text #ADD_CODE
    high      = col[2].text #ADD_CODE
    low       = col[3].text #ADD_CODE
    close     = col[4].text #ADD_CODE
    adj_close = col[5].text #ADD_CODE
    volume    = col[6].text #ADD_CODE
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

print(amazon_data.head())
print(amazon_data.keys())
print(amazon_data['Open'][len(amazon_data['Open'])-1])






