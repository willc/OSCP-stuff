#!/bin/bash
#
# A simple Bash script to grab all the images from a website and save them into a directory.
#
# Written by Will Chatham. @willc
#
# Use at your own risk.
#
#
cat << "EOF"
 ____  __  __    __     ___  ____    ___  __  __   ___  _  _  ____  ____ 
(_  _)(  \/  )  /__\   / __)( ___)  / __)(  )(  ) / __)( )/ )( ___)(  _ \
 _)(_  )    (  /(__)\ ( (_-. )__)   \__ \ )(__)( ( (__  )  (  )__)  )   /
(____)(_/\/\_)(__)(__) \___/(____)  (___/(______) \___)(_)\_)(____)(_)\_)
-------------------------------------------------------------------------
EOF

echo Enter a URL or IP address to get started \(do NOT include http:// or https://\):
read url
echo Output will be saved in ./$url

sleep 1
URL=$url
DIR=$url

echo Here we go...

# Create dir to save everything into. -p tells this script to not fail if the dir already exists.

    mkdir -p $url

# Download all images from the domain
wget --no-check-certificate -nd -r -P $DIR -A jpeg,jpg,bmp,gif,png http://$URL