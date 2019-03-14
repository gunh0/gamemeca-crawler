# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://trees.gamemeca.com/gamerank/#1521881342690-f60aa3c1-8642')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'tr'
    #'tr > td'
    )
# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))


#<tr class="row-2 even" role="row">
#	<td class="column-1">1<p style="font-size:5px; color:#f84203;">(-)</p></td><td class="column-2"><a target="_blank" href="/leagueoflegends"><img src="/data/monthlyrank/pc/leagueoflegends.png" class="rankimg"></a></td><td class="column-3"><a target="_blank" href="/leagueoflegends">리그 오브 레전드</a></td><td class="column-4">라이엇 게임즈</td><td class="column-5">AOS</td>
#</tr>