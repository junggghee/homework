from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309",headers=headers
)

print(data)


