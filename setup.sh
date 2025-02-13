#!/usr/bin/env bash

# Copyright (c) 2025 jontas@gmx.com
# This file is licensed under the MIT License. See LICENSE for details.

chmod +x nad-controller
mkdir -p "$HOME/.local/bin"
cp $(pwd)/{nad-controller,selector.py} $HOME/.local/bin

cat <<EOF > $HOME/.local/share/applications/nad-controller.desktop
[Desktop Entry]
Name=NAD D7050 Controller
Exec=nad-controller
Terminal=false
Type=Application
Icon=pythonbackend
Comment=Control your NAD D7050 Streaming Amp from your desktop
Categories=AudioVideo;Audio;Video;Player;TV;
EOF

printf "\n\e[1mIt's done\e[0m\n"
