
"""
Program: dellStartBackup.py
Author: Brian Miranda Perez
Date: 30/DEC/2022

"""
from datetime import datetime
import os
import subprocess
from os import path
import time
"""
Program variables that setup the main environmental
variables for the IPMI commands an user access for
set the dell servers. This program can be use
with other dell servers but the raw commands has to be adjusted to
the particular server. This script is use to start dell server, run backup server in proxmox,
and stop server after all. THIS SCRIPT IS USE ON A DOCKER CONTAINER RUNNING IN UNRAID  
"""
# Variables set from docker compose enviroment
SERVER_IP = os.environ.get('MY_IP')
IPMI_USERNAME = os.environ.get("MY_USER")
IPMI_PASSWORD = os.environ.get("MY_PASS")
TIME_START = os.environ.get("START")
TIME_STOP = os.environ.get("STOP")

# crone flie inide container
CRON_FILE_PATH = "/etc/cron.d/crontab"

NOW = datetime.now().time() #time of the day

HOURSTRi= str(NOW)[1] # this is to fix the leading 0 at 02
HOURSTRf= str(NOW)[:2]  # first 2 number of the hour

setup = ("Variable are as follow:\n SERVER IP : %s \n\n USERNAME : %s \n PASSWORD : %s \n START TIME : %s \n STOP TIME : %s \n") % (str(SERVER_IP), str(IPMI_USERNAME), str(IPMI_PASSWORD), str(TIME_START), str(TIME_STOP))
print (setup)
print   ("Container time is : "+ str(NOW))

#add .py after ipmitool for venv remove to run on regular containers
IPMI_LOGIN = ("ipmitool -I lanplus -H %s -U %s -P %s ") % (SERVER_IP,IPMI_USERNAME, IPMI_PASSWORD)

"""
bellow this text is the lines for testing change if need.

"""

# Function for writing into the file
def Write_To_File(fileMessage, filename, method):
    f = open(filename, method)
    f.write(fileMessage)
    f.close()
    print(("Successfully wrote to the file %s") % (filename))

# ipmitool commands variables
IPMI_GET_STATUS = "chassis status"
IPMI_POWER_ON = "power on"
IPMI_POWER_OFF = "chassis power soft"

#Status  command
get_status = IPMI_LOGIN + IPMI_GET_STATUS
split_status = os.popen(get_status).read()

# the hour is in TZ= America/New_York on the CT
if HOURSTRi == str(TIME_START):
    os.system(IPMI_LOGIN+IPMI_POWER_ON)

if HOURSTRf == str(TIME_STOP):
    os.system(IPMI_LOGIN+IPMI_POWER_OFF)

else :
    # all debug print erase if you don't need it
    print(" ")
    print(str(split_status))