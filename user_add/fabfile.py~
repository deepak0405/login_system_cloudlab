from __future__ import with_statement
from fabric.api import run,local,sudo,settings
def adding_user():
        os.system("python checkusers.py")
        groups=open('push_users.sh','r')
	errors=open('errors.txt','w+')
	for line in groups:
	    line=line.rstrip()
	    with settings(warn_only=True):      
	         result=sudo(line)
                 if result.failed:
		    errors.write(result+"\n")

def deleting_user():
        os.system("python checkusers.py")
        groups=open('delusers.sh','r')
	errors=open('errors.txt','w+')
	for line in groups:
	    line=line.rstrip()
	    with settings(warn_only=True):      
	         result=sudo(line)
                 if result.failed:
		    errors.write(result+"\n")

