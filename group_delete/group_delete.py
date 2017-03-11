#!/usr/bin/python
import os
error = open('error.txt', 'w')
target = open('group_delete.sh', 'w')
target.truncate()
error.truncate()
group_delete=open('group_delete.txt','r')
for group in group_delete:
    group=group.split()
    target.write("groupdel "+ group[0] +"\n")
    
