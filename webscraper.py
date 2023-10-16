import requests
from bs4 import BeautifulSoup

f = open('veterans_history_project_names.txt', 'a')
i = 1
while i <= 4000:
    r = requests.get(f'https://www.loc.gov/collections/veterans-history-project-collection/?sp={i}')
    content = r.content
    soup = BeautifulSoup(content, features='html.parser')
    classes = soup.find_all('span', {'class': 'item-description-title'})
    for item in classes:
        txt = item.get_text(strip=True)
        final_txt = txt.replace('Collection', '')
        f.write(final_txt)
        f.write('\n')
    i += 1
f.close()

