import xmltodict
import os

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
            print section['HEAD']
    else:
        print data['HEAD']


with open(os.path.expanduser("~/Downloads/ECFR_data/ECFR-title49.xml")) as file:
    data = xmltodict.parse(file.read())

volumes = data['DLPSTEXTCLASS']['TEXT']['BODY']['ECFRBRWS']
for v in volumes:
    checkHigherDivs(v, 0, 8)


