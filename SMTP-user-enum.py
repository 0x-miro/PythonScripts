#!/usr/bin/python

import socket
import sys

if len(sys.argv) !=3 :
	print (f"[*] SMTP-users-enum script by Amir Shaban \n[*] Usage : {sys.argv[0]} <SMTP server> <user name>")
	exit(0)

ip =sys.argv[1]
user = sys.argv[2]

print ("Variables set successfully...")

try :
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect((ip,25))
	banner = s.recv(1024)
	print ("[*] Connection Successfully established .. ")
	print (banner)
except :
	print ("[!!] Error : couldn't connect to the server.....!")
	exit(0)

try :
    s.send(f'VRFY {user} \r\n')
    results = s.recv(1024)
    print (results)
except : 
    print ("[!!] Error Enumerating user")

s.close()
