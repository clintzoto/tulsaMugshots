#!/usr/bin/python2.5
import sys

environ = 'prod'

if environ == "dev":
    environDB = "dev"
    print "##################################################################"
    print "##########-----------This is development------------##############"
    print "##########               environ = %s                 ############" % (environ)
    print "##################################################################"
#    proceed = raw_input("Type Yes >")
#    if proceed != "Yes":
#        print "Nothing processed"
#        sys.exit()
else:
    environ = 'prod'
    environDB = ""
import re
import string
import urllib2
import urllib
import MySQLdb
import pprint
import os
import subprocess
import md5
import shutil
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import time
from urllib2 import Request, urlopen, URLError, HTTPError


# this saves the binary image to /tulsa/mugs
def stealStuff(file_name,file_mode,base_url):

        #create the url and the request
        url = base_url
        req = Request(url)

        # Open the url
        try:
            f = urlopen(req)
            print "downloading " + url
            # Open our local file for writing
            local_file = open("/kunden/homepages/37/d282226577/htdocs/%s/www/tulsa/mugs/%s.jpg" % (environ, file_name), "w" + file_mode)
            #Write to our local file
            local_file.write(f.read())
            local_file.close()

        #handle errors
        except HTTPError, e:
            print "HTTP Error:",e.code , url
        except URLError, e:
            print "URL Error:",e.reason , url

    

def soupCatch(soup, soup_attr_val, soup_el="span", soup_attr="id"):
    try:
        return soup.find(soup_el, {soup_attr: soup_attr_val}).contents[0]
    except Exception, e:
        print "soup catch exception: %s for %s" % (e, soup_attr_val)
        return "None"

def image_check(PERSON_ID):
    BASE_URL = "http://iic.tulsacounty.org/InmateDetails.aspx?" 
    
    try:
        page = urllib2.urlopen("%sid=%d" % (BASE_URL, PERSON_ID))
        soup = BeautifulSoup(page)
        if soup('img', {"id" : "InmatePhoto"}):
            data={}
            print "Hit:\tPERSON_ID = %d" % PERSON_ID
            imgEl = soup.find('img', {"id": "InmatePhoto"})
            if imgEl['src']:
                inmate_name = soupCatch(soup, "lblName")
                print "Image source found: " + imgEl['src']
                print "for " + str(PERSON_ID) + " " + inmate_name 
                stealStuff(str(PERSON_ID), "b", imgEl['src'])
            else:
                print "sorry, no image source."
                sys.exit()
        else:
            print "sorry, no image tag on the page."
            sys.exit()
    except Exception, e:
        print "there was an exception:", e


image_check(int(sys.argv[1]))
