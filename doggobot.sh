#!/bin/bash

if [ ! -d /home/$USER/doggobot/pics ]; then
    mkdir /home/$USER/doggobot/pics;
fi

while true; do
    if [ `date +%H` == "08" ]; then
        python3 /home/$USER/doggobot/doggobot.py $USER;
        dogs=/home/$USER/doggobot/pics/*;
        neomutt -a $dogs -s "Fresh Doggo Delivery" -- $1 < /home/$USER/doggobot/email.txt && rm $dogs;
        sleep 80000;
    fi
    sleep 1200;
done
