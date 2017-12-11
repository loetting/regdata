#!/usr/bin/python

import sys
import xmltodict
import os
from Graph import GraphConnection, RegulatorySection
from RegDataNLP import RegDataNLP

if len(sys.argv) != 4:
    print "Must include required arguments: [ host_location, password, path_to_dataset ]"
    sys.exit()

location = sys.argv[1]
password = sys.argv[2]
path = sys.argv[3]

graph = GraphConnection(location, password)
nlp = RegDataNLP()

def checkHigherDivs(data, current_div_number, target_div_number):
    if not data:
        return

    if current_div_number == target_div_number:
        getSectionData(data)
    
    for i in range(current_div_number + 1, target_div_number + 1):
        div = "DIV" + str(i)
        if div in data:
            subdata = data[div]
            if isinstance(subdata, list):
                for sd in subdata:
                    checkHigherDivs(sd, i, target_div_number)
            else:
                checkHigherDivs(subdata, i, target_div_number)


def getSectionData(data):
    if isinstance(data, list):
        for section in data:
            text = unicode(section['P']).encode("utf-8") if 'P' in section else ''
            node = RegulatorySection(section['HEAD'], text)
            print "HEAD"
            print section['HEAD']
            print "NER"
            print nlp.getNamedEntities(text)
            print "KEYWORDS"
            print nlp.getKeywords(text)
            print '\n'
    else:
        text = unicode(data['P']).encode("utf-8") if 'P' in data else ''
        node = RegulatorySection(data['HEAD'], text)
        print "HEAD"
        print data['HEAD']
        print "NER"
        print nlp.getNamedEntities(text)
        print "KEYWORDS"
        print nlp.getKeywords(text)
        print '\n'
    # graph.insert(node)


with open(os.path.expanduser(path)) as file:
    data = xmltodict.parse(file.read())

volumes = data['DLPSTEXTCLASS']['TEXT']['BODY']['ECFRBRWS']
for v in volumes:
    checkHigherDivs(v, 0, 8)



