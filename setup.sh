#!/usr/bin/env bash

#
# (c) 2025 jontas@gmx.com
# This code is licensed under MIT license (see LICENSE for details)
#


if [[ ! -x "$PWD/nad-controller" ]]; then
  chmod +x "$PWD/nad-controller"
fi

mkdir -p "$HOME/.local/bin"
cp "$PWD"/{nad-controller,selector.py} "$HOME/.local/bin"

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
