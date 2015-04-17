__author__ = 'sabin'

from conf_loader.server_auditor_conf import conf
from conf_loader import postfix_conf
from report import txt_report

# different standards for the postfix
ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

#conf = serverAuditor_confLoader.load_config('serverAuditor.conf')

#some standards for postfix
location_postfix_main = conf.get("postfix.path_postfix_main")
s_my_network = conf.get("postfix.mynetwork")
s_smtpd_use_tls = conf.get("postfix.smtpd_use_tls")
#end of different standards for the postfix

mynetwork = postfix_conf.load_conf(location_postfix_main).get('mynetworks ')
smtpd_use_tls = postfix_conf.load_conf(location_postfix_main).get('smtpd_use_tls')


def check_postfix():
    banner = " ***************Checking Postfix *************** "
    print banner
    print " "
    print "Checking Postfix settings from /etc/postfix/main.cf file"

    if s_my_network == mynetwork:
        print " The postfix allow network is ", s_my_network, ok
    else:
        print " The postfix allow network is ", mynetwork, warning
    if s_smtpd_use_tls == smtpd_use_tls:
        print " The postfix smtpd uses TLS ", ok
    else:
        print " The postfix smtpd does not uses TLS ", warning


def run_postfix_checker():
    txt_report.create_txt_file()
    check_postfix()

#calling function
#run_postfixChecker()