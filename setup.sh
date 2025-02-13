#!/usr/bin/env bash

# Set permissions and copy the files where its belongs
# If the app icon doesnt shows up under Multimedia in
# your start menu, bring up a terminal and run:
#  - KDE Plasma: kbuildsycoca6 --noincremental
#  - XFCE4 run      : xfdesktop --reload && xfce4-panel -r
#
# Copyright (c) 2025 jontas@gmx.com
# This file is licensed under the MIT License. See LICENSE for details.


# Set execute permission on nad-controller
chmod +x nad-controller

# Ensure ~/.local/bin exists
mkdir -p "$HOME/.local/bin"

cp nad-controller selector.py  $HOME/.local/bin
cp nad-controller.desktop $HOME/.local/share/applications

printf "\n\e[1mIt's done\e[0m\n"
