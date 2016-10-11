#!/usr/bin/python2

print "content-type:text/html"

import commands
a=commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/firefox.tar.gz /var/www/cgi-bin/firefox.py")

print "location:http://192.168.208.134/downloads/firefox.tar.gz"
print "\n"


