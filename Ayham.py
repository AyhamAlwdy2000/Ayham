#!/usr/bin/env python

# imports that won't cause errors
import sys
import os
import signal
import subprocess
from threading import Thread
from time import sleep
import datetime
import logging
logging.getLogger("scapy.runtime").setLevel(logging.E>

# terminal colors
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\33[1;93m"
NORMAL = "\033[0;0m"
BOLD = "\033[;1m"

def auto_installer():
    '''
    Just installing required modules
    if they do not already exist
    '''
    print("{R}ERROR: Modules missing.{N}".format(R=RE>
    inst = raw_input("Do you want to automatically in>

    if inst in ('y', 'yes'):
        print("[{Y}*{N}] Installing requirements, ple>
        subprocess.call("sudo pip install netifaces",>
        subprocess.call("sudo apt-get install python->
        subprocess.call("sudo apt-get install python->
        subprocess.call("sudo apt-get install python->
        subprocess.call("sudo apt-get install nmap -y>
        sys.exit("\n[{G}+{N}] Requirements installed.>

    sys.exit(0)

'''
Usually modules that need to be installed
'''
try:
    import netifaces
    from scapy.all import *
