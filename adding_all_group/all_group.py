#!/usr/bin/python
import os 
os.system('python project.py')
target = open('all_groups.sh', 'w')
target.truncate()
gid_group=open('gid_group.txt','r')
for  gid_groups in gid_group:
     gid_groups=gid_groups.split()
     target.write("groupadd -g "+gid_groups[0]+" "+gid_groups[1]+"\n")

