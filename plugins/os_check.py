__author__ = 'sabin'

import subprocess

from conf_loader.server_auditor_conf import conf
from report import txt_report


ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

# different standards in variables

os_description = conf.get("os.os_description")
os_bit = conf.get("os.os_bit")

# end of the different os standards

## check OS description
def check_os_description():
    banner = " ***************Checking OS *************** "
    print banner
    try:
        p1 = subprocess.Popen("lsb_release -d", stdout=subprocess.PIPE, shell=True)
        (osOutput, err) = p1.communicate()
        l_osOutput = osOutput.strip().split(":")
        osdesc = l_osOutput[1].strip()
        #print "here", l_osOutput[1]

    except OSError as oserror:
        print "Error has occured in " +  + p1 + " " + oserror
        exit(200)

    else:

        if os_description == osdesc :                              # if os_description match
            print "The OS is " + osdesc + ok

        else:
            print "The OS found to be: " + osdesc + warning


    ## check OS bit
    try:
        p4 = subprocess.Popen("uname -i", stdout=subprocess.PIPE, shell=True)
        (osbitOutput, err) = p4.communicate()


    except OSError as osbiterror:
        print "Error has occured in " + p4 + " " + osbiterror
        exit(200)

    else:
        if os_bit== osbitOutput.strip() :                              # if os_description match
            print "The OS is " + os_bit + " bit" +ok
        else:
            print "The OS found to be of " + osbitOutput + warning
            r_osbitOutput = "The OS found to be of " + osbitOutput + warning


    print "******** End of Checking OS version and bit ********"




def run_os_checker():
    txt_report.create_txt_file()
    check_os_description()


#run_osChecker()