__author__ = 'Javier Chavez'

from bs4 import BeautifulSoup
from JSON_model import *
import re



class Abq_Data_Parse():
    def __init__(self, location, kmz=False):
        self.__data__ = Data(location=location, kmz=kmz)
        self.__json__ = self.__data__.get_json()

    def get_json_dumps(self, indent):
        return self.__data__.get_json_dumps(indent)

    def get_json_parsed_desc(self, indent):
        return json.dumps(self.__parse_desc__(), indent=indent)

    def __parse_desc__(self):
        import copy
        # not modifying the original json obj
        tmp_json = copy.deepcopy(self.__json__)

        for i in tmp_json['placemarks']:
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
        return tmp_json


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Turn KML/KMZ files to JSON. You can ">>" to output to file')
    parser.add_argument('--l', help='path/or/url/to json | kml | kmz', required=True, dest='loc')
    parser.add_argument('--kmz', help='Flag for KMZ (KML assumed if not given)', dest='is_kmz', default=False, action='store_true')
    parser.add_argument('--d', help='Flag to parse description (not parsed if not given)', dest='parse_desc', default=False, action='store_true')
    parser.add_argument('--i', help='spaces to indent json OPTIONAL', required=False, dest='indent_l', default=0, type=int)
    args = parser.parse_args()

    data = Abq_Data_Parse(location=args.loc, kmz=args.is_kmz)

    if args.parse_desc:
        print data.get_json_parsed_desc(indent=args.indent_l)
    else:
        print data.get_json_dumps(indent=args.indent_l)