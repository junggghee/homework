import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 진행)

song_list = soup.select('table.list-wrap>tbody>tr')
rank = 0
for song in song_list:
    title = song.select('a.title.ellipsis')
    singer = song.select('a.artist.ellipsis')
    rank += 1
    title_el = title[0].text
    singer_el = singer[0].text
    print(rank, title_el.strip(), singer_el)








