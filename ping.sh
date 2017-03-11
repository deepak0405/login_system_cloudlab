pingstatus(){
# $1 is hostname
	count=$( ping -c 2  $1 | grep ttl | wc -l )
	return $count;
}

host=$1;
# Calling function
pingstatus $host

# echo returning value
echo $? 
