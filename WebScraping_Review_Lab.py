#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

# tag_object = soup.title
# print("tag object:", tag_object)

# print("tag object type:", type(tag_object))

# tag_object = soup.h3
# tag_object

# tag_child = tag_object.b
# tag_child

# parent_tag = tag_child.parent
# parent_tag

# tag_object
# #tag_object parent is the body element.
# tag_object.parent

# sibling_1 = tag_object.next_sibling
# print(sibling_1)

# sibling_2 = sibling_1.next_sibling
# print(sibling_2)

# sibling_3 = sibling_2.next_sibling
# print(sibling_3)

# print(tag_child['id'])

# print(tag_child.attrs)

# print(tag_child.get('id'))

# tag_string = tag_child.string
# print(tag_string)

# print(type(tag_string))

# unicode_string = str(tag_string)
# print(unicode_string)

# #Filters: Filters allow you to find complex patterns, 
# #the simplest filter is a string. In this section we will 
# #pass a string to a different filter method and Beautiful Soup 
# #will perform a match against that exact string.

# table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

# table_bs = BeautifulSoup(table, "html.parser")

# print(table_bs.prettify())

# table_rows = table_bs.find_all('tr')
# print(table_rows)

# first_row = table_rows[0]
# print(first_row)

# print(type(first_row))

# print(first_row.td)

# for i,row in enumerate(table_rows):
#     print("row",i,"is",row)
    
# for i,row in enumerate(table_rows):
#     print("row",i)
#     cells=row.find_all('td')
#     for j,cell in enumerate(cells):
#         print('colunm',j,"cell",cell)    

# list_input=table_bs .find_all(name=["tr", "td"])
# print(list_input)

# #Attributes: If the argument is not recognized it will be turned 
# #into a filter on the tag’s attributes. For example the id argument, 
# #Beautiful Soup will filter against each tag’s id attribute. 
# #For example, the first td elements have a value of id of flight, 
# #therefore we can filter based on that id value

# table_bs.find_all(id="flight")
# print(table_bs)

# list_input = table_bs.find_all(href = "https://en.wikipedia.org/wiki/Florida")
# print(list_input)

# print(table_bs.find_all(href=True))

# print(table_bs.find_all(href=False))

# soup.find_all(id="boldest")
# print(soup)

# table_bs.find_all(string="Florida")
# print(table_bs)

# two_tables = "<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

# two_tables_bs = BeautifulSoup(two_tables, 'html.parser')

# print(two_tables_bs.prettify())

# print(two_tables_bs.find("table"))

# print(two_tables_bs.find("table",class_='pizza'))



# url01 = "http://www.ibm.com"

# data01 = requests.get(url01).text 

# soup01 = BeautifulSoup(data01,"html.parser")  # create a soup object using the variable 'data'

# print(soup01.prettify())

# for link in soup01.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
#     print(link.get('href'))

# #Scrape all images Tags

# for link in soup01.find_all('img'):# in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))

#Scrape data from HTML tables

# #The below url contains an html table with data about colors and color codes.
# url02 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# # get the contents of the webpage in text format and store in a variable called data
# data02 = requests.get(url02).text

# soup02 = BeautifulSoup(data02,"html.parser")

# print(soup02.prettify())

# #find a html table in the web page
# table02 = soup02.find('table') # in html table is represented by the tag <table>
# print(table02)

# #Get all rows from the table
# for row in table02.find_all('tr'): # in html table row is represented by the tag <tr>
#     # Get all columns in each row.
#     cols = row.find_all('td') # in html a column is represented by the tag <td>
#     color_name = cols[2].string # store the value in column 3 as color_name
#     color_code = cols[3].string # store the value in column 4 as color_code
#     print("{}--->{}".format(color_name,color_code))

#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas

#The below url contains html tables with data about world population.
url03 = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data03 = requests.get(url03).text

soup03 = BeautifulSoup(data03,"html.parser")
#print(soup03.prettify())

#find all html tables in the web page
tables03 = soup03.find_all('table') # in html table is represented by the tag <table>
#print(tables03)

# we can see how many tables were found by checking the length of the tables list
print(len(tables03))

for index,table in enumerate(tables03):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables03[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables03[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)

#Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html

pd.read_html(str(tables03[5]), flavor='bs4')

population_data_read_html = pd.read_html(str(tables03[5]), flavor='bs4')[0]

print(population_data_read_html)

#Scrape data from HTML tables into a DataFrame using read_html

dataframe_list = pd.read_html(url03, flavor='bs4')
len(dataframe_list)
print(dataframe_list[5])

pd.read_html(url03, match="10 most densely populated countries", flavor='bs4')[0]







