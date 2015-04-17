__author__ = 'sabin'


# This module consist of some default values that will be used in script as constant for that version of script

# OS info
OS_DESCRIPTION = "Ubuntu 14.04.1 LTS"
OS_BIT= "x86_64"

# Ossec HIDS
OSSEC_INIT_CONF = "/etc/ossec-init.conf"
OSSEC_VERSION = "v2.8"

### standard modsecurity settings
SEC_STATUS_ENGINE = "On"
SEC_RULE_ENGINE = "On"
Sec_RESPONSE_BODY_ACCESS = "Off"
MODSECURITY_CONF_lOCATION = "/etc/modsecurity/modsecurity.conf"

# different standards for the postfix
PATH_POSTFIX_MAIN = "/etc/postfix/main.cf"
MY_NETWORK = "127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128"
SMTPD_USE_TLS = "yes"

# AWS IP
AWS_LOCAL_IP = "127.0.0.1"
AWS_PUBLIC_IP = "http://169.254.169.254/latest/meta-data/public-ipv4/"
AWS_PRIVATE_IP = "http://169.254.169.254/latest/meta-data/local-ipv4"

# Fail2ban info
PATH_JAIL_CONF  = "/etc/fail2ban/jail.conf"
PATH_JAIL_LOCAL = "/etc/fail2ban/jail.local"
