#!/usr/bin/python
import os
systems=open('systems.txt','r')
error=open('errors.txt','w')
for key in systems:
     key=key.split()
     if len(key)==2:
       if key[1] == 'useradd':
       os.system("fab -H "+ key[0] +" adding_user")
       if key[1] == 'userdel':
       os.system("fab -H "+ key[0] +" deleting_user")
     else:
       error.write("Less number of input given in system.txt"+"\n") 
