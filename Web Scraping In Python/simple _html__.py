# HTML - Hyper Text Markup Language

"""
Web Scraping : Is accessing a website, getting its content then trying to understand with python.

body means body of html
# h means header
# p means 
ul means undefined list
li means list

"""

from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
<head></head>
<body>
<h1> TITLE </h2>      
<p class="subtitle"> Hello My Name Is Vishal.  </p>
<p> Another p Without Class </p>
<ul>
    <li>Harsh</li>
    <li>Manthan</li>
    <li>Sahil</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup)
print(simple_soup.find('p'))
print(simple_soup.find('p').string)  # Hello My Name Is Vishal.
print(simple_soup.find('ul'))

print(simple_soup.find('p', {'class': 'subtitle'}).string)  # Hello My Name Is Vishal.

def find_list_items():
    list_items = simple_soup.find_all('li')
    list_content = [l.string for l in list_items]
    print(list_content)   #['Harsh', 'Manthan', 'Sahil']


find_list_items()

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]   # attrs means attributes
    print(paragraphs)
    print(other_paragraph[0].string)


find_other_paragraph()