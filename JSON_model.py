import argparse
import json
import urllib2
from zipfile import ZipFile
__author__ = 'Javier Chavez'


class ToJSON(object):
    def parse_kml(self, kml):
        import xml.dom.minidom
        doc = xml.dom.minidom.parse(kml)
        js = {"placemarks":[]}
        for pm in doc.getElementsByTagName('Placemark'):
            _current_obj = {}
            # get the point
            pnt = pm.getElementsByTagName("Point")[0]
            cortag = pnt.getElementsByTagName("coordinates")[0]
            ll = cortag.firstChild.nodeValue.strip(' ')

            # description
            desctag = pm.getElementsByTagName("description")[0]
            desc = desctag.firstChild.nodeValue

            # name
            namtag = pm.getElementsByTagName("name")[0]
            name = namtag.firstChild.nodeValue
            _current_obj = {"name": name, "description": desc, "coordinates": {"lng": ll.split(",")[0], "lat": ll.split(",")[1]}}
            js["placemarks"].append(_current_obj)

        return json.dumps(js)


class Data(object):
    def __init__(self, location='data/hello.json', kmz=False):

        if location[:4] == "http" and not kmz:
            # print location[:4]
            f = urllib2.urlopen(location).read()
            self.__json__ =  json.loads(ToJSON().parse_kml(f))
        elif location[:4] == "http" and kmz:

            f = urllib2.urlopen(location)
            data = f.read()

            with open("tmp.kmz", "wb") as code:
                code.write(data)

            self.kmz_file = ZipFile("tmp.kmz", 'r')
            self.kml_data = self.kmz_file.open('doc.kml', 'r')
            self.__clean_tmp__()
            self.__json__ =  json.loads(ToJSON().parse_kml(self.kml_data))
        else:
            self.__init_file__(location)
            self.__json__ = json.load(self.json_file)

    def get_json(self):
        return self.__json__

    def __init_file__(self, location):
        self.json_file = open(location)


    def __clean_tmp__(self):
        import os
        os.unlink("tmp.kmz")
