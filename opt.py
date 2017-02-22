#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 21/02/2017
@author: Aelxandru Martinas
'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):

    """Web Client, for www.udl.Created
    Downloads www.udl.cat main page to parse
    for agenda items"""

    def get_web(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def search_test(self, html):
        """
        Parses an html page
        """
        

    def run(self):
        """
        Retrieves list of announces from
        www.packtpub.com/packt/offers/free-learning and prints it
        """
        html = self.get_web("http://www.packtpub.com/packt/offers/free-learning/")
        resultat = self.search_test(html)
        print resultat



if __name__ == "__main__":
    client = Client()
    client.run()