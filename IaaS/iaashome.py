#!/usr/bin/python2
print "content-type: text/html"
#print "\n"

import cgi
import commands as c
import os
p=cgi.FormContent()

name=p['nam'][0]
variant=p['variant'][0]
ram=p['ram'][0]
size=p['size'][0]
cpu=p['cpu'][0]
#print name
#print variant
#print  size
#print ram
#print cpu

commands.getoutput("sudo iptables -F")	
commands.getoutput("sudo setenforce 0")
commands.getoutput("sudo service httpd restart")
commands.getoutput("chown qemu /var/ftp/")
commands.getoutput("sudo service vsftpd restart")
commands.getoutput("sudo yum install virt-manager")
commands.getoutput("sudo yum install qemu-kvm")
commands.getoutput("suo service libvirtd restart")
commands.getstatusoutput("sudo chmod 755 /var/ftp/ -R")
#print a
#commands.getoutput("sudo chmod 777 /var/ftp/pub -R"
#commands.getoutput("sudo service vsftpd restart")
#commands.getoutput("sudo service libvirtd restart")

if (variant=="RHEL-6.4") :
	q=c.getstatusoutput("sudo virt-install --name="+ name +" --os-type=linux  --vcpus=" + cpu + 
	" --ram=" + ram +" --disk=/dev/vgIAAS/rhel6,size=" + size +" --location=ftp://192.168.208.134/pub/rhel6.4/"+ 
	 " --extra-args='ks=ftp://192.168.208.134/pub/ks.cfg' " + " --graphics vnc,port=7325,listen=0.0.0.0")
	p=c.getstatusoutput("sudo /var/www/cgi-bin/websockify-master/run -D 5647 192.168.208.134:7325")
#	print p
elif (variant=="Backtrack") :
	w=c.getstatusoutput("sudo virt-install --name="+ name + " --os-type=linux --vcpus="+cpu+ " --ram=" +ram+ 
	 " --disk=/dev/vgIAAS/BT,size="+size +" --cdrom=/BT5-KDE-32.iso" " --graphics vnc,port=9324,listen=0.0.0.0")
#	print w
#	c.getstatusoutput("sudo service vsftpd restart")
	c.getstatusoutput("sudo /var/www/cgi-bin/websockify-master/run -D 6132 192.168.208.134:9324")

print "location:http://192.168.208.134/cloudonfire/osgallery.html"
print "\n"

