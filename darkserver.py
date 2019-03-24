#!/usr/bin/python3
#Coded By : Mr. Malware
#https://www.github.com/mr-malware

try:
  import os
  import sys
  darklink="/var/lib/tor/hidden_service/hostname"
  file=open(darklink,"r")
except:
      print("")
      print("")
      print("            \033[1;31mDarkServer v_2.0 ")
      print("")
      print(" \033[1;31mError! Please Run install.sh")
      print("")
      print("")
      sys.exit()

def banner():
	print("\033[1;34m ______   _______  _______  _        " + "\033[1;31m _______  _______  _______           _______  _______ 	")
	print("\033[1;34m(  __  \ (  ___  )(  ____ )| \    /\ " + "\033[1;31m(  ____ \(  ____ \(  ____ )|\     /|(  ____ \(  ____ )	")
	print("\033[1;34m| (  \  )| (   ) || (    )||  \  / / " + "\033[1;31m| (    \/| (    \/| (    )|| )   ( || (    \/| (    )|	")
	print("\033[1;34m| |   ) || (___) || (____)||  (_/ /  " + "\033[1;31m| (_____ | (__    | (____)|| |   | || (__    | (____)|	")
	print("\033[1;34m| |   | ||  ___  ||     __)|   _ (   " + "\033[1;31m(_____  )|  __)   |     __)( (   ) )|  __)   |     __)	")
	print("\033[1;34m| |   ) || (   ) || (\ (   |  ( \ \  " + "\033[1;31m      ) || (      | (\ (    \ \_/ / | (      | (\ (   	")
	print("\033[1;34m| (__/  )| )   ( || ) \ \__|  /  \ \ " + "\033[1;31m/\____) || (____/\| ) \ \__  \   /  | (____/\| ) \ \__	")
	print("\033[1;34m(______/ |/     \||/   \__/|_/    \/ " + "\033[1;31m\_______)(_______/|/   \__/   \_/   (_______/|/   \__/	")
	print("\033[1;34m                                                                                          			")
	print("        \033[1;31mSkyKnight-Team         " + "    \033[1;36m(V_2.0)"+"          \033[1;32mBy: Mr. Malware		")

def config():
	os.system("rm -f /etc/tor/torrc > /dev/null 2>&1")
	os.system("cp torrc /etc/tor/torrc >/dev/null 2>&1")
	os.system("clear")

config()

def opt():
	list=["\033[1;32m[1] Simple Server","\033[1;31m[2] DarkServer","\033[0;31m[3] Exit"]
	print(list[0])
	print(list[1])
	print(list[2])
	inpt=input("\033[1;36m===>\033[0m")
	path=input("\033[1;32mEnter Host Path: ")	
	print("")

	if inpt == '1':
		
		print("CTRL + C for exit")
		print("")
		print("\033[1;34mServer Started.......")
		print("Link: http://127.0.0.1:80")
		print("\033[1;32mHost Path: "+path)
		os.system('cd ' +path+"&&"+ 'python3 -m http.server --bind 127.0.0.1 80  > /dev/null 2>&1')

	elif inpt== '2':
		print("\033[1;35mCTRL + C for exit")
		print("")
		print("\033[1;34mServer Started.......")
		print("\033[1;34mLocal Link: http://127.0.0.1:80")
		print("\033[1;33mDark Link: http://"+file.read())
		print("\033[1;32mHost Path: "+path)
		os.system('cd ' +path+"&&"+ 'python3 -m http.server --bind 127.0.0.1 80  > /dev/null 2>&1 | xterm -e tor')
	
	elif inpt == '3':
		
		print("\033[1;36mGood Bye")		
		sys.exit()

	else:
	     print("")
	     print("\033[1;31mInvalid Input")
	     print("")
	     banner()
	     print("")
	     opt()

print("\033[0m")
banner()
print("")
opt()



