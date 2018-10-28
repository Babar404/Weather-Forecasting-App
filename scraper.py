import requests
from bs4 import BeautifulSoup
import re
karachi='https://darksky.net/forecast/24.8668,67.0311/uk212/en'
lahore='https://darksky.net/forecast/31.5165,74.3295/uk212/en'
islamabad='https://darksky.net/forecast/33.6938,73.0652/uk212/en'
balochistan="https://darksky.net/forecast/28,66/uk2"
 #Now the code begins

class DataExtraction(object):

    def __init__(self, site):
        self.site = site

    def create_page_handler(self):
        try:
            html = requests.get(self.site).content
        except:
            print("check your internet connection ")
            html = None
        if html:
            self.page = BeautifulSoup(html, 'html.parser')
        else:
            self.page = None
        return
class handel(DataExtraction):
    def __init__(self,site):
        DataExtraction.__init__(self, site)
    def extract_data_from_page(self):
        labels = self.page.findAll(class_='label swip')
        label_value = self.page.findAll(class_='val swap')
        self.extracted_values = {}

        if len(labels) == len(label_value):

            for i in range(len(labels)):
                self.extracted_values[labels[i].text.replace('\n', '')] = label_value[i].get_text().replace('\n', '')

            self.extracted_values['temperature'] = self.page.find('span', {'class': 'temp'}).get_text().replace('\n',
                                                                                                                '')

        self.extracted_values['summary'] = self.page.find('span', {"class": 'summary swap'}).get_text().replace('\n',
                                                                                                                '')
        self.extracted_values['next summary'] = self.page.find('span', {"class": 'next swap'}).get_text().replace('\n',
                                                                                                                  '')
        return self.extracted_values

    def start(self):
        self.create_page_handler()
        if self.page:
            return self.extract_data_from_page()
#x=karachi
#y='coordinates'

#site = 'https://darksky.net/forecast/'+str(y)+'/ca12/en'
#x=input('gps')
a=input("enter the city which u want to search,(karachi)(islamabad)(lahore)(balochistan)?")
if a=='karachi':
    site=karachi
elif a=='islamabad':
    site=islamabad
elif a=="balochistan":
    site=balochistan
elif a=="lahore":
    site=lahore
else:
    assert False,"Please enter appropriate data"

handler = handel(site)
print(handler.start())
