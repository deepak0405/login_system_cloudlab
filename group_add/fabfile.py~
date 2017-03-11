from __future__ import with_statement
from fabric.api import run,local,sudo,settings
def main_function():
        groups=open('group_add.sh','r')
	errors=open('errors.txt','w+')
	for line in groups:
	    line=line.rstrip()
	    with settings(warn_only=True):      
	         result=sudo(line)
                 if result.failed:
		    errors.write(result+"\n")
