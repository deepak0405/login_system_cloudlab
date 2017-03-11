useradd -u 2339 -G btech15 cs1150223
usermod -g btech15 cs1150223
groupdel cs1150223
mkdir /mnt/plos/home/cs1150223
chown -R cs1150223:btech15 /mnt/plos/home/cs1150223
useradd -u 1161 -G faculty sbansal
usermod -g faculty sbansal
groupdel sbansal
usermod -a -G svn44,updaters,faculty,svn46 sbansal
mkdir /mnt/plos/home/sbansal
chown -R sbansal:faculty /mnt/plos/home/sbansal
