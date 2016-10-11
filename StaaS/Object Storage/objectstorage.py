#!/usr/bin/python2

print "content-type:text/html"
#print "\n"
import commands,cgi

a=cgi.FormContent()

size=a['size'][0]
#print size

p=commands.getstatusoutput("sudo lvcreate --name lvstorage --size "+size+"G vgstorage")

b=commands.getstatusoutput("sudo mkfs.ext4 /dev/vgstorage/lvstorage")

c=commands.getstatusoutput("sudo mount /dev/vgstorage/lvstorage /freepack1")

#commands.getoutput("scp 192.168.208.134:/var/www/cgi-bin/objectstoragecommand.py  192.168.208.130:/var/www/cgi-bin/objectstoragecommand.py")
#commands.getoutput("mkdir /var/www/html/downloads")
commands.getstatusoutput("sudo tar -zcvf /var/www/html/downloads/objectstorage.tar.gz /var/www/cgi-bin/objectstoragecommand.py")
#print "<a href='http://127.0.0.1/html/downloads/objectstorage.tar.gz 'download>click here</a>"

print "location:http://192.168.208.134/downloads/objectstorage.tar.gz"
print "\n"
