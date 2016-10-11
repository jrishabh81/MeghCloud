#!/usr/bin/python2

print "content-type:text/html"

import commands,cgi
s=cgi.FormContent()
size=s['size'][0]

a=commands.getstatusoutput("sudo lvextend --size "+size+"G /dev/vgblocks/lvblock")
b=commands.getstatusoutput("sudo resize2fs  /dev/vgblocks/lvblock")
print "location:http://192.168.208.134/downloads/blockstorage.tar.gz"
print "\n"
