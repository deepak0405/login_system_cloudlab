import warnings
import os
from collections import defaultdict
import shutil

userfile = "/root/cloudlab/sudoaccess/users"
user = open(userfile,'r')

# header information of sudoers file
header = "Defaults  env_reset "+"\n"+'Defaults  secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"'+"\n"+"root  ALL=(ALL:ALL) ALL\n%admin ALL=(ALL) ALL\n%sudo ALL=(ALL:ALL) ALL\n\nabhishek ALL=(ALL) NOPASSWD:ALL\n"

pc = defaultdict(list)
filecheck=dict()
sudoers=""
userdata = dict()

################## storing user and machine info
def sudoaccess():
	for line in user:
		users = line.split(" ")
# getting array length
		arraylen = len(users)
		uid = users[0].rstrip()
		userdata[uid] = dict()
# if user need sudo access on more than one machine following block will run
		if (arraylen > 2):
			i = 0
			while(i < int(arraylen) - int("1")):
				index = int(i) + int("1")
				pcname = users[index].rstrip()
				userdata[uid][pcname] = dict()
				userdata[uid][pcname]['uid'] = uid
				userdata[uid][pcname]['pc'] = pcname
				userdata[uid][pcname]['sudo'] = ("%s ALL=(ALL) NOPASSWD:ALL"%(uid))
				i = index
# if user need sudo access only on single machine following block will run
		elif(arraylen == 2):
			pcname = users[1].rstrip()
			userdata[uid][pcname] = dict()
			userdata[uid][pcname]['uid'] = uid
			userdata[uid][pcname]['pc'] = pcname
			userdata[uid][pcname]['sudo'] = ("%s ALL=(ALL) NOPASSWD:ALL"%(uid))
######################################


# Creating sudoers file####################
	for uid in userdata:
		for uidpc in userdata[uid]:
			machinename = userdata[uid][uidpc]['sudo']
			pc[uidpc].append((str(machinename)))

	for machine in pc:
		machine = machine.rstrip()
		directory = "/root/cloudlab/sudoaccess/machine/"+machine+"/etc"
		sudofile = "/root/cloudlab/sudoaccess/machine/"+machine+"/etc/sudoers"

		if not os.path.exists(directory):
			os.makedirs(directory)
			sudoers = open(sudofile,"w")
			rootuser = '\n'.join(pc[machine])
			sudoers.write(header + rootuser)
			sudoers.close()
		elif os.path.exists(directory):
			sudoers = open(sudofile,"w")
			rootuser = '\n'.join(pc[machine])
			sudoers.write(header + rootuser)
			sudoers.close()


#### function to delete directory if it doesn't exist in "user" file
def checkdir():
	lsdir = os.listdir("/root/cloudlab/sudoaccess/machine")
	for directory in lsdir:
		if directory in pc:
			continue
		elif not directory in pc:
			shutil.rmtree('/root/cloudlab/sudoaccess/machine/'+directory)

#### calling functions
sudoaccess()
checkdir()

## closing file	
user.close()
