#!/usr/bin/python2
print "content-type:text/html"
print "\n"

import commands
q=commands.getstatusoutput("sudo lvcreate --name  snapRHEL6 --size 2G -s /dev/vgIAAS/rhel6")
print "snapshot created successfully at /dev/vgIAAS/snapRHEL6"
