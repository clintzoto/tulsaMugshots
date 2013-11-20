#!/usr/bin/python2.5
import sys
environ = 'dev'
environDB = "dev"
#environ = 'prod'
#environDB = ""
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
from datetime import datetime
import time
from urllib2 import Request, urlopen, URLError, HTTPError
#1/4/2011
#this is used to update tulsa mugshots databese with the images md5 hash. I already had the files being updated
# with profileId as the filename. This won't do. All future cron updates are recorded correctly

conn = MySQLdb.connect(host='', user='', passwd='', db='')
c = conn.cursor()
cur_dir = os.path.dirname( os.path.realpath( __file__ ) )

def warning():
    print "##################################################################"
    print "##########-----------This is development------------##############"
    print "##########               environ = %s                 ############" % (environ)
    print " MAKE SURE YOU ARE IN MUGSHOTS FOLDER WITH IMAGES and a subdirectory"
    print "##################################################################"
    proceed = raw_input("Type Yes >")
    if proceed != "Yes":
        print "Nothing processed"
        sys.exit()

    
def updateDatabase():
    warning()
    file_array = [f for f in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, f))]
    dict_id_hash = {}
    for fi in file_array:
        jpgcheck = string.split(fi, ".")
        if jpgcheck[1] == "jpg":
            tmp = string.split(fi, "-")
            strProfileId = tmp[0]
            strMugshotHashPlusDotJpg = string.split(tmp[1], ".")
            strMugshotHash = strMugshotHashPlusDotJpg[0]
            dict_id_hash[strProfileId] = strMugshotHash
    #print dict_id_hash
    save_record(dict_id_hash)

    
def save_record(dict_id_hash):
    try:
        for key, value in dict_id_hash.iteritems():
            print "key:" + key + "  value: " + value
            #c.execute("update " + environDB + "records set mugshotHash = " + value + " where personId = " + key)
            c.execute("update %srecords set mugshotHash='%s' where personId = %d" % (environDB, value, int(key)))
            #x[key]="update %srecords set mugshotHash='%s' where personId = %d" % (environDB, value, int(key))
            #x = """update """ + environDB + """records set mugshotHash=""" + value + """ where personId=""" + key
    except Exception, e:
        print "db error: ", e

updateDatabase()

