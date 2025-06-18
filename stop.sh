#!/bin/bash

EXEC="/home/mjuncker/github/perso/RP42/rp.py"
PID=$(pgrep -f $EXEC)

if [[ $PID == "" ]]; then
	echo "no rp42 process found, check path if the process is still running"
	exit 1
fi

kill -15 $PID
echo "rp42 was killed"
