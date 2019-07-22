# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

table_ranking = soup.findAll('td',{'class':'column-1'})
table_titles = soup.findAll('td',{'class':'column-3'})  # table_titles list 객체

for ranking, title in zip(table_ranking, table_titles):
    print(ranking.get_text(), title.get_text())