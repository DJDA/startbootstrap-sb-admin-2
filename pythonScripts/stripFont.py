html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

inputFile = open('./1-input.html')
soup = BeautifulSoup(inputFile,'html.parser')

fontTags = soup.findAll("font")
for tag in fontTags:
    tag.unwrap()

tdTags = soup.findAll("td")
for tag in tdTags:
    tag.attrs.clear()

trTags = soup.findAll("tr")
for tag in trTags:
    tag.attrs.clear()

pTags = soup.findAll("p")
for tag in pTags:
    if tag.get_text().strip() == "":
        tag.decompose()
    else:
        tag.attrs.clear()

outputFile = open('./1-output.html',mode='w',encoding='UTF-8')
outputFile.write(soup.prettify())