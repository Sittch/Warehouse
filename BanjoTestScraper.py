from bs4 import BeautifulSoup
import requests

##from urllib.request import urlopen
##html = urlopen("http://www.google.com/").read()
##print(html)
##
##soup.find("b", text='Throws:').next_sibling.strip()
##u'Right'


##Starting Player ID: Beginning at #1 will loop over full database
playerid = "aardsm001da"

result = requests.get("https://www.baseball-reference.com/search/search.fcgi?search=" + str(playerid))

##result.status_code
##result.headers
##
content=result.content
soup=BeautifulSoup(content, features="html")

samples = soup.select("meta > div:nth-child(2) > p:nth-child(3)")

print(soup.prettify())


##<strong>Bats: </strong>Right
##        &nbsp;•&nbsp;
##	<strong>Throws: </strong>Right



#samples = soup.select("a")
##samples = soup.select("html head a")
##samples = soup.select("html > head > a")
##sample_id = soup.select("#id")
##sample_class = soup.select(".class")
##samples = soup.find_all("a")
##samples = soup.find_all(id="specific_id")
##samples = soup.find_all("a", "specific_css_class")
##samples = soup.find_all("a", class_="specific_css_class")
##samples = soup.find_all("a", attrs={"class": "specific_css_class"})












#Old Baseball Reference Prelim. Code
##result = requests.get("https://www.baseball-reference.com/play-index/")
##
##result.status_code
##result.headers
##
##content=result.content
##soup=BeautifulSoup(content, features="lxml")
##
##print(soup.prettify())
##
###samples = soup.select("a")
##samples = soup.select("html head a")
##samples = soup.select("html > head > a")
##sample_id = soup.select("#id")
##sample_class = soup.select(".class")
##samples = soup.find_all("a")
##samples = soup.find_all(id="specific_id")
##samples = soup.find_all("a", "specific_css_class")
##samples = soup.find_all("a", class_="specific_css_class")
##samples = soup.find_all("a", attrs={"class": "specific_css_class"})
