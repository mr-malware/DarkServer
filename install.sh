#!/bin/bash coded by : Mr. Malware Link: 
#https://www.github.com/SkyKnight-Team
cyan='\e[0;36m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'

Darklink=/var/lib/tor/hidden_service/hostname
banner()
{
echo -e $blue" ______   _______  _______  _        $red _______  _______  _______           _______  _______ 	"
echo -e $blue"(  __  \ (  ___  )(  ____ )| \    /\ $red(  ____ \(  ____ \(  ____ )|\     /|(  ____ \(  ____ )	"
echo -e $blue"| (  \  )| (   ) || (    )||  \  / / $red| (    \/| (    \/| (    )|| )   ( || (    \/| (    )|	"
echo -e $blue"| |   ) || (___) || (____)||  (_/ /  $red| (_____ | (__    | (____)|| |   | || (__    | (____)|	"
echo -e $blue"| |   | ||  ___  ||     __)|   _ (   $red(_____  )|  __)   |     __)( (   ) )|  __)   |     __)	"
echo -e $blue"| |   ) || (   ) || (\ (   |  ( \ \  $red      ) || (      | (\ (    \ \_/ / | (      | (\ (   	"
echo -e $blue"| (__/  )| )   ( || ) \ \__|  /  \ \ $red/\____) || (____/\| ) \ \__  \   /  | (____/\| ) \ \__	"
echo -e $blue"(______/ |/     \||/   \__/|_/    \/ $red\_______)(_______/|/   \__/   \_/   (_______/|/   \__/	"
echo -e $blue"                                                                                          	"
echo -e $red "	      SkyKnight-Team		 $cyan(V_2.0)		   $blue By: Mr. Malware		"
tput sgr0
}
banner
echo ""
echo ""
echo ""
#checking Python
which python > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] python.............................[ found ]"
which python > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] python -> not found! "
sleep 2
echo -e $yellow "[ ! ] Installing python "
sleep 2
echo -e $green ""
sudo apt-get install python -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which python > /dev/null 2>&1
fi
#Checking tor
which tor > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] tor................................[ found ]"
which tor > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] tor -> not found! "
sleep 2
echo -e $yellow "[ ! ] Installing tor "
sleep 2
echo -e $green ""
sudo apt-get install tor -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which tor > /dev/null 2>&1
fi
#
clear
banner
echo -e $yellow "Launching...................."
rm -f /etc/tor/torrc > /dev/null 2>&1
cp torrc /etc/tor/torrc >/dev/null 2>&1
#
clear

python3 DarkServer.py
