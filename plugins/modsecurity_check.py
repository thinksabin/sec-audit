__author__ = 'sabin'

from conf_loader import modsecurity_conf
from conf_loader.server_auditor_conf import conf
from report import txt_report

# different standards in variables

ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

#conf = serverAuditor_confLoader.load_config('serverAuditor.conf')

modsecurity_sec_status_engine = conf.get("modsecurity.SecStatusEngine")
modsecurity_sec_rule_engine_on = conf.get("modsecurity.SecRuleEngine")
modsecurity_sec_response_body_access = conf.get("modsecurity.SecResponseBodyAccess")

#modsecurity_conf_location    = "sample_modsecurity.conf"
modsecurity_conf_location = conf.get("modsecurity.conf_location")



## checking modsecurity settings. This method should be called only if modsecurity is installed in the system.
def check_modsecurity():

    status_engine = modsecurity_conf.load_conf(modsecurity_conf_location).get("SecStatusEngine")
    ruleEngine = modsecurity_conf.load_conf(modsecurity_conf_location).get("SecRuleEngine")
    response_body_access = modsecurity_conf.load_conf(modsecurity_conf_location).get("SecResponseBodyAccess")
    audit_log = modsecurity_conf.load_conf(modsecurity_conf_location).get("SecAuditLog")

#print "the value of status  = " + status_engine + " " + ruleEngine + " " + response_body_access + " " + audit_log
    print " *************** Checking Apache Modsecurity Firewall Settings ***************"
    print "Reading /etc/modsecurity/modsecurity.conf "
    try:
        if status_engine == modsecurity_sec_status_engine:
            print " The modsecurity engine status is " + str(status_engine) + ok
        else:
            print " The modsecurity engine status is " + str(status_engine) + warning

        if ruleEngine == modsecurity_sec_rule_engine_on:
            print " The modsecurity rule engine status is " + str(ruleEngine) + ok
        else:
            print " The modsecurity rule engine status is " + str(ruleEngine) + warning

        if response_body_access == modsecurity_sec_response_body_access:
            print " The modsecurity response_body_access is " + response_body_access + ok
        else:
            print " The modsecurity response_body_access is " + response_body_access + " This setting might consume more server" \
                                                                                  " memory" + warning
        print " The location of the modsecurity audit log is " + audit_log
        print " "
        print " End of Testing Modsecurity settings. Please do the Needful"
    except IOError as checkModsecurityError:
        print (" Error has occur in " + "checkModsecurity()" + " " + checkModsecurityError.strerror)


def run_modsecurity_checker():
    txt_report.create_txt_file()
    check_modsecurity()
