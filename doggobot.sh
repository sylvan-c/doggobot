#!/bin/bash

while true; do
    if [ `date +%H` == "08" ]; then
        python3 /home/$USER/dogs/doggobot.py;
        dogs=/home/$USER/doggobot/*.jpg;
        neomutt -a $dogs -s "Fresh Doggo Delivery" -- user@domain.com < /home/$USER/doggobot/email.txt && rm $dogs;
        sleep 6000;
    fi
    sleep 1200;
done
