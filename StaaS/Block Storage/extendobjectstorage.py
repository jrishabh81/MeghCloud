#!/usr/bin/python2

print "content-type:text/html"


import commands,cgi
s=cgi.FormContent()
size=s['size'][0]

a=commands.getstatusoutput("sudo lvextend --size "+size+"G /dev/vgstorage/lvstorage")

b=commands.getstatusoutput("sudo resize2fs  /dev/vgstorage/lvstorage")
#commands.getstatusoutput("umount /media/freepack")

#commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/objectstorage.tar.gz /var/www/cgi-bin/objectstoragecommand.py")
print "location:http://192.168.208.134/cloudonfire/msg.html"
print "\n"
