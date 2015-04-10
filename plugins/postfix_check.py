__author__ = 'sabin'

import default_values
from conf_loader.server_auditor_conf import conf
from conf_loader import postfix_conf


# different standards for the postfix
ok = " .......................................[OK]"
warning = " .......................................[WARNING]"
error = " .......................................[NOT INSTALLED]"

my_network = ""
smtpd_use_tls = ""

try:
    my_network = postfix_conf.load_conf(default_values.POSTFIX_MAIN_LOCATION).get('mynetworks ')
    smtpd_use_tls = postfix_conf.load_conf(default_values.POSTFIX_MAIN_LOCATION).get('smtpd_use_tls')
except:
    pass

if my_network == "":
    my_network = ""
    smtpd_use_tls = ""

def check_postfix():
    print "Checking Postfix settings from /etc/postfix/main.cf file"

    if default_values.POSTFIX_MY_NETWORK == my_network:
        print " The postfix allow network is ", my_network, ok
    elif my_network != "" :
        print " The postfix allow network is ", my_network, warning
    
    if default_values.POSTFIX_SMTPD_USE_TLS == smtpd_use_tls:
        print " The postfix smtpd uses TLS ", ok
    elif smtpd_use_tls != "" :
        print " The postfix smtpd does not uses TLS ", warning
    
    if my_network == "" and smtpd_use_tls == "":
        print "Postfix ", error 

def run_postfix_checker():
    check_postfix()

#calling function
#run_postfixChecker()