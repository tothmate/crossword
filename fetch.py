import requests
import re
from datetime import datetime, timedelta
from time import sleep

links = []
remaining = 20
current_date = datetime.now()

while current_date >= datetime(2020, 9, 23) and remaining >= 0:
    resp = requests.get(
        f'https://www.newyorker.com/puzzles-and-games-dept/crossword/{current_date.strftime("%Y/%m/%d")}'
    )
    url = re.search('<iframe[^>]+?src="([^"]+?crossword[^"]+?)"', resp.text)
    title = re.search("<title>([^<]+?)<", resp.text)
    if url is not None:
        links.append(f'<a href="{url.group(1)}">{title.group(1)}</a>')
        remaining -= 1

    current_date -= timedelta(1)
    sleep(0.5)

html = f"""
<html>
<head>
    <title>The New Yorker crossword</title>
    <style>
        p a {{ margin: 0.5em 0; font-size: 2em; display: block }}
    </style>
</head>
<body>
    <h1>
        <a href="https://www.newyorker.com/crossword-puzzles-and-games">
            The New Yorker crossword
        </a> direct links
    </h1>
    <p>
        <i>Originals were not working on iOS 9</i>
    </p>
    <p>
        {"".join(links)}
    </p>
</body>
</html>
"""

if len(links) > 0:
    with open("index.html", "w") as index_file:
        index_file.write(html)
