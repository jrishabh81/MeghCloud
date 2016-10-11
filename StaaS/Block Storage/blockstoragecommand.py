#!/usr/bin/python2

import commands
commands.getoutput("yum install iscsiadm")
commands.getoutput("iptables -F")
#commands.getoutput("service tgtd restart")
commands.getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.208.134 --discover")
commands.getstatusoutput("iscsiadm --mode node --targetname cloudSpace --portal 192.168.208.134:3260 --login")
print "drive created successfully at /dev/sdb"
o=commands.getoutput("lsblk")
print o
raw_input("press enter to continue..")
