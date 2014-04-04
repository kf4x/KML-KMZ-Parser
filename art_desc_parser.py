__author__ = 'Javier Chavez'

from bs4 import BeautifulSoup
from JSON_model import *
import re


data = Data(location='http://data.cabq.gov/community/art/publicart/PublicArt.kmz', kmz=True)

data = data.get_json()

for i in data ['placemarks']:
    # remove weirdspacing and cddata
    desc = re.sub(r'<!\[CDATA\[(.*)\]\]>', "", i['description'])

    # print desc
    soup = BeautifulSoup(desc)
    # rows = [a.get_text() for a in soup.find("table", border=1).find_all("tr")]

    rows = soup.find("table", border=1).find_all("tr")
    new_desc = {}
    for row in rows:
        td = row.find_all("td")
        if len(td) == 2:
            new_desc.update({td[0].get_text().lower().replace(" ","_"): td[1].get_text()})
        else:
            new_desc = {}

    i['description'] = new_desc


print json.dumps(data, indent=2)