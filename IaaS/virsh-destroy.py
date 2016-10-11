#!/usr/bin/python2
print "content-type: text/html"

import commands

commands.getoutput("sudo virsh destroy p")
print "location:http://192.168.208.134/cloudonfire/os-services.html"
print 
