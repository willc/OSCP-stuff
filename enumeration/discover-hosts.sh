#!/bin/bash   
IP=$1
nmap -sn $IP
fping -a -g $IP 2> /dev/null
