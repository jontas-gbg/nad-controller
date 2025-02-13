#
# Copyright (c) 2025 jontas@gmx.com
# This file is licensed under the MIT License. See LICENSE for details.
#

import socket
import codecs
import sys
import os

TCP_IP = '192.168.1.199' # Your device IP
TCP_PORT = 50001
LAST_STATE_FILE = os.path.expanduser("~/.cache/last_state")

def send(MESSAGE):
    MESSAGE = codecs.decode(MESSAGE, "hex_codec")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
    except socket.error as e:
        print(f"Error. Unable to connect: {e}")
        sys.exit(1)

def save_last_state(input_source=None, volume=None):
    """Save the last selected input source and volume to a file."""
    last_state = ["Unknown", "127"]
    if os.path.exists(LAST_STATE_FILE):
        with open(LAST_STATE_FILE, "r") as file:
            last_state = file.read().strip().split(',')

    if input_source is not None:
        last_state[0] = input_source
    if volume is not None:
        last_state[1] = str(volume)

    with open(LAST_STATE_FILE, "w") as file:
        file.write(','.join(last_state))

def save_last_volume(volume):
    """Save the last volume to the same file as input source."""
    save_last_state(volume=volume)

def load_last_state():
    """Load the last selected input source and volume from cached file."""
    if not os.path.exists(os.path.dirname(LAST_STATE_FILE)):
        os.makedirs(os.path.dirname(LAST_STATE_FILE))
    if not os.path.exists(LAST_STATE_FILE):
        with open(LAST_STATE_FILE, "w") as file:
            file.write("Unknown,127\n")
    with open(LAST_STATE_FILE, "r") as file:
        return file.read().strip()

def turnOff():
    send("0001020900") # Network standby, no powersaving

def turnOn():
    send("0001020901")

def coaxial1():
    send("0001020300")
    save_last_state(input_source="Coaxial 1")

def coaxial2():
    send("0001020301")
    save_last_state(input_source="Coaxial 2")

def optical1():
    send("0001020302")
    save_last_state(input_source="Optical 1")

def optical2():
    send("0001020303")
    save_last_state(input_source="Optical 2")

def computer():
    send("0001020304")
    save_last_state(input_source="Computer")

def airplay():
    send("0001020305")
    save_last_state(input_source="Airplay")

def dock():
    send("0001020306")
    save_last_state(input_source="Dock")

def bt():
    send("0001020307")
    save_last_state(input_source="Bluetooth")
