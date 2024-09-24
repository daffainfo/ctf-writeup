#!/bin/bash
cron
/usr/sbin/sshd -D &
sleep 3
su ctf -c "python app.py"