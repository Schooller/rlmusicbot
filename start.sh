#!/bin/bash

while true
do
    echo "starting..."
    python3 bot.py
    echo "If you want to completely stop the server process now, press Ctrl+C before the time is up$"
    echo "Rebooting in:"
    for i in 12 11 10 9 8 7 6 5 4 3 2 1
    do
      	echo "$i..."
        sleep 1
    done
    echo "Rebooting now!"
done