from report import txt_report

__author__ = 'sabin'

import ConfigParser, os


def load_config(config_file):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read (config_file)

        config_info = {}


        config_info['os.os_description'] = conf.get('os', 'os_description')
        config_info['os.os_bit'] = conf.get('os', 'os_bit')


        config_info['ossec-ids.ossec_init_conf'] = conf.get('ossec-ids', 'ossec_init_conf')
        config_info['ossec-ids.ossec_version'] = conf.get('ossec-ids', 'ossec_version')
        config_info['ossec-ids.ossec_type_agent'] = conf.get('ossec-ids', 'ossec_type_agent')
        config_info['ossec-ids.ossec_type_server'] = conf.get('ossec-ids', 'ossec_type_server')
        config_info['ossec-ids.ossec_error'] = conf.get('ossec-ids', 'ossec_error')
        config_info['ossec-ids.ossec_mail_alert_id'] = conf.get('ossec-ids', 'ossec_mail_alert_id')
        config_info['ossec-ids.ossec_central_server_ip'] = conf.get('ossec-ids', 'ossec_central_server_ip')


        config_info['modsecurity.SecStatusEngine'] = conf.get('modsecurity', 'SecStatusEngine')
        config_info['modsecurity.SecRuleEngine'] = conf.get('modsecurity', 'SecRuleEngine')
        config_info['modsecurity.SecResponseBodyAccess'] = conf.get('modsecurity', 'SecResponseBodyAccess')
        config_info['modsecurity.conf_location'] = conf.get('modsecurity', 'conf_location')


        config_info['postfix.path_postfix_main'] = conf.get('postfix', 'path_postfix_main')
        config_info['postfix.mynetwork'] = conf.get('postfix', 'mynetwork')
        config_info['postfix.smtpd_use_tls'] = conf.get('postfix', 'smtpd_use_tls')


        config_info['network.local_ip_resource'] = conf.get('network', 'local_ip_resource')
        config_info['network.public_ip_resource'] = conf.get('network', 'public_ip_resource')
        config_info['network.private_ip_resource'] = conf.get('network', 'private_ip_resource')
        config_info['network.valid_tcp_port_list_lo'] = conf.get('network', 'valid_tcp_port_list_lo')
        config_info['network.valid_tcp_port_list_eth0'] = conf.get('network', 'valid_tcp_port_list_eth0')
        config_info['network.valid_tcp_port_list_pub'] = conf.get('network', 'valid_tcp_port_list_pub')

        config_info['fail2ban.path_jail_conf'] = conf.get('fail2ban', 'path_jail_conf')
        config_info['fail2ban.path_jail_local'] = conf.get('fail2ban', 'path_jail_local')
        config_info['fail2ban.ssh_ignoreip_list'] = conf.get('fail2ban', 'ssh_ignoreip_list')
        config_info['fail2ban.ssh_enabled'] = conf.get('fail2ban', 'ssh_enabled')

        config_info['fail2ban.ssh_port'] = conf.get('fail2ban', 'ssh_port')
        config_info['fail2ban.ssh_filter'] = conf.get('fail2ban', 'ssh_filter')
        config_info['fail2ban.ssh_logpath'] = conf.get('fail2ban', 'ssh_logpath')
        config_info['fail2ban.ssh_maxretry'] = conf.get('fail2ban', 'ssh_maxretry')
        config_info['fail2ban.ssh_bantime'] = conf.get('fail2ban', 'ssh_bantime')
        config_info['fail2ban.ssh_findtime'] = conf.get('fail2ban', 'ssh_findtime')

        return config_info

    except IOError as server_auditor_confLoader:
        print (" Error has occur in " + "load_config()" + " " + server_auditor_confLoader.strerror)


if os.path.exists("templates/serverAuditor.conf"):

    file_exist = "server_auditor.conf file exist. yee!!!"
    print file_exist
    print "Generating Report in .txt Format"
    conf = load_config('templates/serverAuditor.conf')
    txt_report.create_txt_file()


else:
    print " ERROR: Main Standard configuration File ('server_auditor.conf') " + "is Missing."

# print "mail id = ", conf.get('ossec-ids.ossec_mail_alert_id')
# print "ignore ip = ", conf.get('ossec-ids.ossec_type_agent')
# print "postfix.mynetwork = ", conf.get('postfix.mynetwork')
# print "network.valid_tcp_port_list_eth0 = ", conf.get('network.valid_tcp_port_list_eth0')