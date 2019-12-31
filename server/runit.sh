#!/bin/sh

echo "starting zootopia on port 80"
sudo python zootopia.py 80 >& /tmp/zootopia_log.txt &

