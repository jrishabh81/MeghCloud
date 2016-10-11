#!/usr/bin/python2

print "content-type:text/html"

import commands
a=commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/gedit.tar.gz /var/www/cgi-bin/gedit.py")

print "location:http://192.168.208.134/downloads/gedit.tar.gz"
print "\n"


