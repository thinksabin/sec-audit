__author__ = 'sabin'

import default_values
from conf_loader import modsecurity_conf
from conf_loader.server_auditor_conf import conf

# different standards in variables

ok = " .......................................[OK]"
warning = " .......................................[WARNING]"
error = " .......................................[NOT INSTALLED]"

## checking modsecurity settings. This method should be called only if modsecurity is installed in the system.
def check_modsecurity():
    status_engine = ""
    ruleEngine = ""
    response_body_access = ""
    audit_log = ""

    try:
        status_engine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecStatusEngine")
        ruleEngine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecRuleEngine")
        response_body_access = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecResponseBodyAccess")
        audit_log = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecAuditLog")
    except:
        status_engine = ""
        ruleEngine = ""
        response_body_access = ""
        audit_log = ""

#print "the value of status  = " + status_engine + " " + ruleEngine + " " + response_body_access + " " + audit_log
    print "checking Apache Modsecurity Firewall Settings "
    print "Reading /etc/modsecurity/modsecurity.conf "
    try:
        if status_engine == default_values.MODSECURITY_SEC_STATUS_ENGINE:
            print " The modsecurity engine status is " + str(status_engine) + ok
        elif status_engine != "" :
            print " The modsecurity engine status is " + str(status_engine) + warning

        if ruleEngine == default_values.MODSECURITY_SEC_RULE_ENGINE:
            print " The modsecurity rule engine status is " + str(ruleEngine) + ok
        elif ruleEngine != "" :
            print " The modsecurity rule engine status is " + str(ruleEngine) + warning

        if response_body_access == default_values.MOSECURITY_Sec_RESPONSE_BODY_ACCESS:
            print " The modsecurity response_body_access is " + response_body_access + ok
        elif response_body_access != "" :
            print " The modsecurity response_body_access is " + response_body_access + " This setting might consume more server memory" + warning
        
        if status_engine != "":                                                                          
            print " The location of the modsecurity audit log is " + audit_log
        
        if status_engine == "" or ruleEngine == "" or response_body_access == "" or audit_log == "" :
            print "Modsecurity ", error
        print " "
        print " End of Testing Modsecurity settings. Please do the Needful"
    except IOError as checkModsecurityError:
        print (" Error has occur in " + "checkModsecurity()" + " " + checkModsecurityError.strerror)


def run_modsecurity_checker():
    check_modsecurity()
