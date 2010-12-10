#!/usr/bin/python2.5
import sys

environ = 'prod'

if environ == "dev":
    environDB = "dev"
    print "##################################################################"
    print "##########-----------This is development------------##############"
    print "##########               environ = %s                 ############" % (environ)
    print "##################################################################"
    proceed = raw_input("Type Yes >")
    if proceed != "Yes":
        print "Nothing processed"
        sys.exit()
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

#start_time = datetime.now();

conn = MySQLdb.connect(host='db2536.perfora.net', user='dbo336192140', passwd='tulsafoobar', db='db336192140')
c = conn.cursor()

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

    
def save_record(d):
    try:
        c.execute("""insert ignore into """ + environDB + """records (personId, name, gender, race, birthday, feet, inches, weight, id, hair, eyes, address, city, state, zip, arrestDate, arrestTime, arrestBy, agency, bookingDate, bookingTime, charge, charge2, charge3, bondAmt) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (d['personId'], d['name'], d['gender'], d['race'], d['birthday'], d['feet'], d['inches'], d['weight'], d['id'], d['hair'], d['eyes'], d['address'], d['city'], d['state'], d['zip'], d['arrestDate'], d['arrestTime'], d['arrestBy'], d['agency'], d['bookingDate'], d['bookingTime'], d['charge'], d['charge2'], d['charge3'], d['bondAmt']))

    except Exception, e:
        print "db error: ", e

def soupCatch(soup, soup_attr_val, soup_el="span", soup_attr="id"):
    try:
        return soup.find(soup_el, {soup_attr: soup_attr_val}).contents[0]
    except Exception, e:
        print "soup catch exception: %s for %s" % (e, soup_attr_val)
        if soup_attr_val == "zip" or soup_attr_val == "feet" or soup_attr_val == "inches" or soup_attr_val == "weight":
            return 0
        else:
            return "None"

def getInmateLinks():
    try:
        c.execute("SELECT id from %slatestPersonId" % (environDB))
        last_valid_person_id = c.fetchone()

        PERSON_ID_start = last_valid_person_id[0]
#        PERSON_ID_start = 1275993################
        PERSON_ID_end = PERSON_ID_start + 100
    except Exception, e:
        print "get_id_range error: ", e

    BASE_URL = "http://iic.tulsacounty.org/InmateDetails.aspx?" 
    
    recordsBlank = 0;
    while  PERSON_ID_start < PERSON_ID_end:
        print PERSON_ID_start
        print "recordsBlank", recordsBlank
        if recordsBlank == 10:
            #after 10 blank records its safe to assume that the last entry was the last arrest for now
            #update latestPersonId to the last records entry that will be the next PERSON_ID_start
            c.execute("""UPDATE """ + environDB + """latestPersonId set id=(select max(personId + 1) from """ + environDB + """records)""")
            sys.exit()
        try:
            page = urllib2.urlopen("%sid=%d" % (BASE_URL, PERSON_ID_start))
            soup = BeautifulSoup(page)
            if soup('img', {"id" : "InmatePhoto"}):
                data={}
                print "Hit:\tPERSON_ID = %d" % PERSON_ID_start
                imgEl = soup.find('img', {"id": "InmatePhoto"})
                stealStuff(str(PERSON_ID_start), "b", imgEl['src'])
                data['personId'] = PERSON_ID_start
                data['name'] = soupCatch(soup, "lblName")
                print data['name']
                data['gender'] = soupCatch(soup, "LblGender")
                data['race'] = soupCatch(soup, "lblRace")
                data['birthday'] = soupCatch(soup, "lblBirthDate")
                data['feet'] = soupCatch(soup, "lblHeightFeet")
                data['inches'] = soupCatch(soup, "lblHeightInches")
                data['weight'] = soupCatch(soup, "lblWeight")
                data['id'] = soupCatch(soup, "lblInmateID")
                data['hair'] = soupCatch(soup, "lblHairColor")
                data['eyes'] = soupCatch(soup, "lblEyeColor")
                data['address'] = soupCatch(soup, "lblAddress")
                data['city'] = soupCatch(soup, "lblCity")
                data['state'] = soupCatch(soup, "lblState")
                data['zip'] = soupCatch(soup, "lblzip")
                data['arrestDate'] = soupCatch(soup, "lblArrestDate")
                data['arrestTime'] = soupCatch(soup, "lblArrestTime")
                data['arrestBy'] = soupCatch(soup, "lblArrestBy")
                data['agency'] = soupCatch(soup, "lblAgency")

                temp_date = string.split(soup.find('span', {"id": "lblBookingDate"}).contents[0], "/")
                data['bookingDate'] = "%s-%s-%s" % (temp_date[2], temp_date[0], temp_date[1])
                print data['bookingDate'] 

                data['bookingTime'] = soupCatch(soup, "lblBookingTime")
                #cell = soup.find('span', {"id": "lblAssignedCellId"}).contents[0]
                #tbody = soup.find("table", {"id": "GridOffenses"}).findNext("tr").findNext("tr").findAll("font")
                gridofoffenses = soup.find("table", {"id": "GridOffenses"}).findAll("tr")
                #get rid of the first one, it is just column header
                del gridofoffenses[0]
                data['charges'] = []
                totalBond = 0

                for offense in gridofoffenses:
                    off = offense.find("font").find(text=True)
                    try:
                        #get bond amount and drop change
                        bnd = offense.findAll("font")[4].contents[0].split('.')
                        #remove all nondigits and cast
                        bond = int(re.sub("\D", "", bnd[0]))
                        totalBond = totalBond + bond

                        data['charges'].append(off)
                    except Exception, e:
                        print "crap: ", e

                data['bondAmt'] = str(totalBond)
                print data['bondAmt']
                try:
                    data['charge'] = data['charges'][0]
                   # data['bondAmt'] = float(data['bondAmts'][0])
                except Exception, e:
                    print "oops: ", e
                    data['charge'] = ""

                try:
                    data['charge2'] = data['charges'][1]
                except Exception, e:
                    print "oops: ", e
                    data['charge2'] = ""

                try:
                    data['charge3'] = data['charges'][2]
                except Exception, e:
                    print "oops: ", e
                    data['charge3'] = ""
                    
                
                recordsBlank = 0
                save_record(data)
                print "foobarshit"
            else:
                recordsBlank = recordsBlank + 1
        except Exception, e:
            print "there was an exception:", e
            #PERSON_ID_start = PERSON_ID_start + 1
        PERSON_ID_start = PERSON_ID_start + 1

getInmateLinks()
