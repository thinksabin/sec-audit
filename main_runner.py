
from plugins import jail_check
from plugins import ossec_ids_check
from plugins import aws_port_check
from plugins import packages_check
from plugins import os_check
from plugins import postfix_check
from plugins import modsecurity_check


print " "
print " *************** Checking OS *************** "
try:
	os_check.run_os_checker()
except:
	pass

print " "
print " *************** Checking modules *************** "
try:
	packages_check.run_packages_checker()
except:
	pass

print " "
print " *************** Checking ports *************** "
try:
	aws_port_check.run_port_checker()
except:
	pass

print " "
print " *************** Checking Fail2ban *************** "
try:
	jail_check.run_jail_checker()
except:
	pass

print " "
print " *************** Checking postfix ***************"
try:
	postfix_check.run_postfix_checker()
except:
	pass

print " "
print " *************** Checking IDS (OSSEC) ***************"
try:
	ossec_ids_check.run_ids_checker()
except:
	pass

print " "
print " *************** Checking WAF (Modsecurity) ***************"
try:
	modsecurity_check.run_modsecurity_checker()
except :
	pass 
	
print " "
print "**************End of Testing*************************"
