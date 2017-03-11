#!/usr/bin/python
import os 
os.system('python project.py')
error = open('error.txt', 'w')
target = open('group_add.sh', 'w')
target.truncate()
error.truncate()
group_add=open('group_add.txt','r')
gid_group=open('gid_group.txt','r')
for group in group_add:
    group=group.split()
    #print(group)
    gid_group.seek(0)
    count=0
    for  gid_groups in gid_group:
         gid_groups=gid_groups.split()
         #print(gid_groups[1] +" " + group[0])
         if(group[0]==gid_groups[1]):
             target.write("groupadd -g "+gid_groups[0]+" "+gid_groups[1]+"\n")
             count=1
             #print("hi")
             break
    if(count==0):
       error.write("ERROR : Group "+ group[0]+ " does not exist in ldap")
