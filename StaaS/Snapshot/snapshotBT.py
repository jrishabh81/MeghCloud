#!/usr/bin/python2
print "content-type:text/html"
print "\n"

import commands
q=commands.getstatusoutput("sudo lvcreate --name snapBT --size 2G -s /dev/vgIAAS/BT")
print "snapshot created successfully at /dev/vgIAAS/snapBT"
