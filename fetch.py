import requests
import re
from datetime import datetime, timedelta
from time import sleep

current = datetime(2020, 9, 23)
while current <= datetime.now():
    resp = requests.get(f'https://www.newyorker.com/puzzles-and-games-dept/crossword/{current.strftime("%Y/%m/%d")}')
    url = re.search('<iframe[^>]+?src="([^"]+?crossword[^"]+?)"', resp.text)
    title = re.search('<title>([^<]+?)<', resp.text)
    if url is not None:
        print(f'<a href="{url.group(1)}">{title.group(1)}</a><br>')
    current += timedelta(1)
    sleep(0.5)