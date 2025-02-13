# NAD D7050 Controller
A Python-based control software for the **NAD D7050 Streaming Amp**. It allows users to control the volume, switch inputs, and turn the unit on/off via a simple graphical interface.

## Background
I lost my remote control and the Android app is a joke. So I did some research on how to control the device via TCP/IP. As far as I know, there is no official API from NAD Electronics. I found the hex codes used to send commands to the device by simply googling. 

Since the amp can sometimes be a bit difficult and stubborn, no guarantees are given that the code will work on your particular system. As always, you use the code at your own risk. It's tested on Arch Linux.

For example, it is possible to send a request to the device and get status about the selected source, volume level, etc., but my device tends to crash then. I have solved this by writing known device status to a text file instead. Not optimal, but it's the best I could come up with at the moment.

## Needed
You _may_ also need to install the associated widget toolkit packages (e.g. **tk** must also be installed to use `Tkinter`).

### Dependencies
**You probably already have `tk` installed. If not, install it using your package manager.**
```sh
sudo pacman -S tk # Arch
sudo apt-get install python3-tk # Debian/Ubuntu
sudo dnf install python3-tkinter # Fedora
```

## Installation
```sh
git clone https://github.com/jontas-gbg/nad-d7050-controller.git
cd nad-d7050-controller
chmod +x nad-controller
```
Open `selector.py` with a text editor and change the variable TCP_IP to the IP address of your NAD.
```py
TCP_IP = '192.168.1.199' # eg. 192.168.0.0/16, 10.0. 0.0/8
```
#### Run it from terminal with
```sh
./nad-controller
```
#### Or use the install script
```sh
chmod +x setup.sh && ./setup.sh
```
It'll copy `nad-controller` to `~/.local/bin` and `nad-controller.desktop` to `~/.local/share/applications` letting you start the application from your start menu.
Make sure `~/.local/bin` are in your `$PATH`.

---
Copyright (c) 2025 jontas@gmx.com
This file is licensed under the MIT License. See LICENSE for details.
