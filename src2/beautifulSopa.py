from bs4 import BeautifulSoup # Import BeautifulSoup from bs4 to parse the html in webscrap
import requests # Import requests to get the html from the website

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Parse the html
soup = BeautifulSoup(html, 'html5lib')

tag_object=soup.title


print(soup.prettify())

print("tag object:",tag_object)
print("tag object type:",type(tag_object))

tag_object=soup.h3
tag_object
print("tag object:",tag_object)

tag_child =tag_object.b
tag_child
print("tag child:",tag_child)

parent_tag=tag_child.parent
parent_tag
print("parent tag:",parent_tag)

sibling_1=tag_object.next_sibling
sibling_1
print("sibling_1:",sibling_1)

print(tag_object.next_sibling)

sibling_3=tag_object.next_sibling.next_sibling
print("sibling_3:",sibling_3)

print(tag_child['id'])
print(tag_child.get('id'))
print(tag_child.attrs)
print(tag_child.string)

tag_string=tag_child.string
tag_string
print(type(tag_child.string))

unicode_string = str(tag_string)
print(unicode_string)

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')

table_rows=table_bs.find_all('tr')

first_row =table_rows[0]
first_row

print(type(first_row))

print(first_row.td)


for i,row in enumerate(table_rows):
    print("row",i,"is",row)

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
print(list_input)

table_bs.find_all(id="flight")
print(table_bs.find_all(id="flight"))

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)


list_input=table_bs.find_all(href=False)
print(list_input)


data = requests.get("http://www.ibm.com").text # Get the html from the website
#print(data) # Print the html of the website ibm.com

soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'