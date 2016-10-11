#!/usr/bin/python2

print "content-type:text/html"

import cgi,commands
a=cgi.FormContent()

u=a['u'][0]
p=a['p'][0]


u1=commands.getoutput("cat /etc/passwd | grep -w " +u +" | cut -d : -f 1")



if(u1==u):
	print "location:http://192.168.208.134/cloudonfire/services/services.html"
	print "\n"
else :
	print "location:http://192.168.208.134/cloudonfire/errormsg.html"
	print "\n"
	
