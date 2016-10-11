#!/usr/bin/python2

print "content-type:text/html"

import commands,cgi

a=cgi.FormContent()

size=a['size'][0]


p=commands.getstatusoutput("sudo lvcreate --name lvblock --size "+size+"G vgblocks")

b=commands.getstatusoutput("sudo mkfs.ext4 /dev/vgblocks/lvblock")

commands.getstatusoutput("sudo service tgtd restart")

commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/blockstorage.tar.gz /var/www/cgi-bin/blockstoragecommand.py")

print "location:http://192.168.208.134/downloads/blockstorage.tar.gz"
print "\n"

