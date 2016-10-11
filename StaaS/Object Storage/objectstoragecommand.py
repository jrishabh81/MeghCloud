#!/usr/bin/python

import commands
#commands.getoutput("mkdir /media/freepack")

r=commands.getstatusoutput("sshfs tina@192.168.208.134:/freepack1 /media/freepack")
#print r
print "You storage is at /media/freepack"
raw_input("Press enter to continue..")
