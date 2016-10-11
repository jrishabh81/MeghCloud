#!/usr/bin/python2

print "content-type : text/html"

import os
import cgi
import commands
p=cgi.FormContent()
user=p['u'][0]
pswd=p['p'][0]

u1=commands.getoutput("cat /etc/passwd | grep -w " +user +" | cut -d : -f 1")
if(user==u1):
	print "location:http://192.168.208.134/cloudonfire/login/loginA.html"
	print "\n"
else :
	a=commands.getstatusoutput("sudo useradd "+user)
	b=commands.getstatusoutput("sudo echo " + pswd + " | sudo passwd --stdin "+ user)
	print "location:http://192.168.208.134/cloudonfire/services/services.html"
	print "\n"

