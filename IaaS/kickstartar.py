#!/usr/bin/python2

print "content-type:text/html"

import commands
a=commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/kickstart.tar.gz /var/www/cgi-bin/kickstart.py")

print "location:http://192.168.208.134/downloads/kickstart.tar.gz"
print "\n"


