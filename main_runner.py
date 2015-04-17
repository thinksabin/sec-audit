
import argparse
from plugins import jail_check
from plugins import ossec_ids_check
from plugins import aws_port_check
from plugins import module_check
from plugins import os_check
from plugins import postfix_check
from plugins import modsecurity_check



parser = argparse.ArgumentParser()
parser.add_argument("-o", "--operatingsystem", action="store_true",
                    help="Check Operating System version and bits")
parser.add_argument("-m", "--modules", action="store_true",
                    help="check Installed Modules version")
parser.add_argument("-j", "--fail2ban", action="store_true",
                    help="check Fail2ban configuration")
parser.add_argument("-mod", "--modsecurity", action="store_true",
                    help="check Apache ModSecurity configuration")
parser.add_argument("-pf", "--postfix", action="store_true",
                    help="check Postfix configuration")
parser.add_argument("-i", "--ossecids", action="store_true",
                    help="check OSSEC HIDS configuration")
parser.add_argument("-p", "--awsports", action="store_true",
                    help="check AWS ports")

args = parser.parse_args()

if args.operatingsystem:
    print " "
    os_check.run_os_checker()

if args.modules:
    print " "
    module_check.run_module_checker()
if args.fail2ban:
    print " "
    jail_check.run_jail_checker()
if args.modsecurity:
    print " "
    modsecurity_check.run_modsecurity_checker()
if args.postfix:
    print " "
    postfix_check.run_postfix_checker()
if args.awsports:
    print " "
    aws_port_check.run_port_checker()
if args.ossecids:
    print " "
    ossec_ids_check.run_ids_checker()
else:
    print " "
    print "**************End of Testing*************************"
