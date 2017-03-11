import os
import command

os.system("mount filer01:/vol/plos1 /mnt/plos")
os.system("ln -s /mnt/plos/home /")
