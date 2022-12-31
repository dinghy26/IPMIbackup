"""
Program: dellStartBackup.py
Author: Brian Miranda Perez
Date: 30/DEC/2022

"""
from datetime import datetime
from proxmoxmanager import ProxmoxManager
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

NOW = datetime.now()
IPMI_LOGIN = ("ipmitool -I lanplus -H %s -U %s -P %s ") % (SERVER_IP,IPMI_USERNAME, IPMI_PASSWORD)
#proxmox_manager = ProxmoxManager(host = "%s:8006", user= "root@pam", token_name = "Tname", token_value = "Secret_value") % (SERVER_IP)

"""
bellow this text is the lines for testing change if need.

"""
IPMI_GET_DATA = "sdr entity 7"
IPMI_GET_TEMP = "sdr type Temperature"

temp_collection_command = IPMI_LOGIN + IPMI_GET_TEMP
general_ipmi_data = IPMI_LOGIN + IPMI_GET_DATA

temp_data = os.popen(temp_collection_command).read().split()
all_data = os.popen(general_ipmi_data).read().split()

SERVER_TEMP = str(temp_data)
SERVER_DATA = str (all_data)

print (str(SERVER_TEMP))
print (SERVER_DATA)


