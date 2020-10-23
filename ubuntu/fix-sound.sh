#!/usr/bin/env bash

# https://help.ubuntu.com/community/SoundTroubleshootingProcedure

set +x

echo "Killing audio daemons/processes"
killall pulseaudio
pulseaudio -k
rm -r ~/.config/pulse/*
rm -r ~/.pulse*

echo "Waiting a few seconds then restarting daemon..."
sleep 10
pulseaudio --start

echo "Launching audio controller..."
pavucontrol
