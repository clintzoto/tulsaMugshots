#!/usr/bin/python2.5

environ = 'dev'

if environ == "dev":
    import sys
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
            #local_file = open("../www/tulsa/mugs/" + file_name + ".jpg", "w" + file_mode)
            #local_file = open("/kunden/homepages/37/d282226577/htdocs/" + environ "/www/tulsa/mugs/" + file_name + ".jpg", "w" + file_mode)
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



def getInmateLinks():
    try:
        c.execute("SELECT id from %slatestPersonId" % (environDB))
        last_valid_person_id = c.fetchone()

        PERSON_ID_start = last_valid_person_id[0]
        #PERSON_ID_start = 1273918
        PERSON_ID_end = PERSON_ID_start + 500
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
                data['name'] = soup.find('span', {"id": "lblName"}).contents[0]
                print "\t" + data['name']
                data['gender'] = soup.find('span', {"id": "LblGender"}).contents[0]
                data['race'] = soup.find('span', {"id": "lblRace"}).contents[0]
                data['birthday'] = soup.find('span', {"id": "lblBirthDate"}).contents[0]
                data['feet'] = soup.find('span', {"id": "lblHeightFeet"}).contents[0]
                data['inches'] = soup.find('span', {"id": "lblHeightInches"}).contents[0]
                data['weight'] = soup.find('span', {"id": "lblWeight"}).contents[0]
                data['id'] = soup.find('span', {"id": "lblInmateID"}).contents[0]
                data['hair'] = soup.find('span', {"id": "lblHairColor"}).contents[0]
                data['eyes'] = soup.find('span', {"id": "lblEyeColor"}).contents[0]
                data['address'] = soup.find('span', {"id": "lblAddress"}).contents[0]
                data['city'] = soup.find('span', {"id": "lblCity"}).contents[0]
                data['state'] = soup.find('span', {"id": "lblState"}).contents[0]
                data['zip'] = soup.find('span', {"id": "lblzip"}).contents[0]
                data['arrestDate'] = soup.find('span', {"id": "lblArrestDate"}).contents[0]
                data['arrestTime'] = soup.find('span', {"id": "lblArrestTime"}).contents[0]
                data['arrestBy'] = soup.find('span', {"id": "lblArrestBy"}).contents[0]
                data['agency'] = soup.find('span', {"id": "lblAgency"}).contents[0]
                
                print data;

                temp_date = string.split(soup.find('span', {"id": "lblBookingDate"}).contents[0], "/")
                data['bookingDate'] = "%s-%s-%s" % (temp_date[2], temp_date[0], temp_date[1])
                #print data['bookingDate'] 
                data['bookingTime'] = soup.find('span', {"id": "lblBookingTime"}).contents[0]
                #cell = soup.find('span', {"id": "lblAssignedCellId"}).contents[0]
                tbody = soup.find("table", {"id": "GridOffenses"}).findNext("tr").findNext("tr").findAll("font")
                print tbody[0].string
                data['charge'] = tbody[0].string
                try:
                    if tbody[0].string:
                        data['charge'] = tbody[0].string
                    else:
                        data['charge'] = ""
                    if tbody[1].string:
                        data['charge2'] = tbody[1].string
                    else:
                        data['charge2'] = ""
                    if tbody[2].string:
                        data['charge3'] = tbody[2].string
                    else:
                        data['charge3'] = ""
                        #data['charge2'] = tbody[0].string
                        #data['charge3'] = tbody[0].string
                    if tbody[4].string:
                        data['bondAmt'] = tbody[4].string
                    else:
                        data['bondAmt'] = ""
                except Exception, e:
                    print "multiple charge issue:", e
                recordsBlank = 0
                save_record(data)

            else:
                print "empty holder"
                recordsBlank = recordsBlank + 1
        except Exception, e:
            print "there was an exception:", e
            #PERSON_ID_start = PERSON_ID_start + 1
        PERSON_ID_start = PERSON_ID_start + 1

getInmateLinks()
