#!/usr/bin/python2

import commands
commands.getoutput("sudo service sshd restart")
commands.getoutput("ssh -X -l tina 192.168.208.134 firefox ")
raw_input("press enter to continue..")

