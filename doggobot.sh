#!/bin/bash

while true; do
    if [ `date +%H` == "08" ]; then
        python3 /home/$USER/dogs/doggobot.py;
        dogs=/home/$USER/dogs/*.jpg;
        neomutt -a $dogs -s "Fresh Doggo Delivery" -- user@domain.com < /home/$USER/dogs/email.txt && rm $dogs;
        sleep 6000;
    fi
    sleep 1200;
done
