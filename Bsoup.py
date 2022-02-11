import requests
from bs4 import Beautifulsoup
url = "https//www.espncricinfo.com/series/ipl-2021-1249214/points-table-standings"

r = requests.get(url)
htmlcontent = r.text

soup = BeautifulSoup(htmlcontent, 'html.parser')

table = soup.find_all("table")

print(soup.find("table")['class'])
print(soup.find('table').get_text())