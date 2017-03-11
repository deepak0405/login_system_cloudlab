#!/usr/bin/python
import ldap
target = open('gid_group.txt', 'w')
target.truncate()
## first you must open a connection to the server
try:
    l = ldap.open("bhairav.cse.iitd.ac.in")
    l.protocol_version = ldap.VERSION3	
except ldap.LDAPError, e:
	print e
	
'''username="cn=cs1150223, o=cse.iitd.ernet.in"
password="keepsmiling9"
#using my username and password need to think of something else
try:
     l.simple_bind(username, password)
except Exception, error:
     print error '''
# simple bind not required
searchScope = ldap.SCOPE_SUBTREE
#search scope determine in which subtree to search
#retrieveAttributes =["cn"]
retrieveAttributes=["gidNumber"]
retrieveAttributes1=["cn"]
# retrieveAttributes means what information we want
searchFilter ='(objectClass=posixGroup)'
# search is filter on the basis of search filter
baseDN="dc=cse,dc=iitd,dc=ernet,dc=in"

try:
	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        ldap_result_id1 = l.search(baseDN, searchScope, searchFilter, retrieveAttributes1)
	result_set = []
        result_set1 = []
	while 1:
		result_type, result_data = l.result(ldap_result_id, 0)
                result_type1, result_data1 = l.result(ldap_result_id1, 0)
		if (result_data == [] or result_data1==[]):
			break
		else:
			if result_type == ldap.RES_SEARCH_ENTRY:
				result_set.append(result_data)
                        if result_type1 == ldap.RES_SEARCH_ENTRY:
				result_set1.append(result_data1)
        for key,key_1 in zip(result_set,result_set1):
              for key1,key_11 in zip(key[0][1],key_1[0][1]):
                     target.write(key[0][1][key1][0]+"  "+key_1[0][1][key_11][0]+"\n")
except ldap.LDAPError, e:
	print e

