"""
Program: dellStartBackup.py
Author: Brian Miranda Perez
Date: 30/DEC/2022

"""
from datetime import datetime
import os
import subprocess
from os import path
import yaml
import time


"""
Program variables that setup the main environmental
variables for the IPMI commands an user access for
set the dell servers. This program can be use
with other dell servers but the raw commands has to be adjusted to
the particular server. This script is use to start dell server, run backup server in proxmox,
and stop server after all.
"""
# this line of for the yaml file integration.
with open("dellSetUp.yaml", "r") as stream:
    setup_data = yaml.load(stream, Loader=yaml.FullLoader)
    #setup_data is the data colection from the yaml file 
    #debug
    # print(setup_data)

# Variables set from the yaml values
SERVER_IP = setup_data.get('database').get('serverIP')
IPMI_USERNAME = setup_data.get('IPMI').get('username')
IPMI_PASSWORD = setup_data.get('IPMI').get('password')

NOW = datetime.now().time() #time of the day
HOURSTRi= str(NOW)[:2] # first 2 number of the hour
HOURSTRf= str(NOW)[1] # this is to fix the leading 0 at 02 am
#add .py after ipmitool for venv remove to run on regular containers
IPMI_LOGIN = ("ipmitool -I lanplus -H %s -U %s -P %s ") % (SERVER_IP,IPMI_USERNAME, IPMI_PASSWORD)

"""
bellow this text is the lines for testing change if need.

"""
# ipmitool commands variables
IPMI_GET_STATUS = "chassis status"
IPMI_POWER_ON = "power on"
IPMI_POWER_OFF = "power off"


get_status = IPMI_LOGIN + IPMI_GET_STATUS

split_status = os.popen(get_status).read()


# the hour is in ZULU time. make sure you do the convertion. 
if HOURSTRi == str(21):
    os.system(IPMI_LOGIN+IPMI_POWER_ON)

if HOURSTRf == str(2):
    os.system(IPMI_LOGIN+IPMI_POWER_OFF)

else:
    print(str(split_status))
    print (HOURSTRf)


