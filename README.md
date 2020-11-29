# doggobot
Bot which sends emails with dog pics

Installation:<br>
```git clone https://github.com/sylvan-c/doggobot```

Usage:<br>
```cd doggobot
chmod +x doggobot.sh
./doggobot.sh target@email.com```

You'll need to set up neomutt with your email address for this to work. I used mutt-wizard (https://github.com/LukeSmithxyz/mutt-wizard) and it worked fine for a gmail account. 

You also need to change the recipient email address in the neomutt command in doggobot.sh

I have a screen session on my VPS running doggobot.sh but will probably turn it into a systemd service when I can be bothered to figure out how. I tried running the execution of the script with cron but it wouldn't let me since cron has no MTA installed so msmtp failed to send the email every time.
