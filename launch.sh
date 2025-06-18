#!/bin/bash

EXEC="./rp.py"
CONFIG="./config.json"

if ! [ -f $EXEC ]; then
	echo "script not found"
	exit 1
fi

python3 "$EXEC" $CONFIG & > /dev/null 2>&1 &
job_id=$(jobs | head -n 1| sed -n 's/^\[\([0-9]\+\)\].*/\1/p')
disown %$job_id

sleep 1
echo "script is active, you can close this terminal"
echo "use \`bash stop.sh' to stop the script"