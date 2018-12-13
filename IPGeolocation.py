import urllib2, time, sys
import subprocess as sp
from colorama import Fore, init
init()

'''
Subscribe To https://www.YouTube.com/CallMeCOM
Ensure you leave credits if you wish you use this script. Credits are nice and any dev likes that!
Enjoy.
'''

def main():
	clear()
	print(Fore.WHITE+'*'*37)
	print('+         '+Fore.CYAN+'Geolocation Script'+Fore.WHITE+'        +')
	print('*'*37)
	ipshit = raw_input(Fore.RED+'Please Enter IP Address: '+Fore.GREEN)
	yolo = urllib2.urlopen('https://ipapi.co/'+ipshit+'/json')
	content = yolo.read()
	value = content.replace('"', '').replace('{', '').replace('}', '').replace('_', '').replace(',', '')
	print(Fore.WHITE+value)
	
	restartBool = True
	while restartBool:
		restart = raw_input(Fore.RED+'Geolocate Another IP? (Y/N): '+Fore.GREEN)
		if restart == 'y' or restart == 'Y':
			main()
			restartBool = False
		elif restart == 'N' or restart == 'n':
			sys.exit('Closing The Dank Hax')
			restartBool = False
		elif restart != '':
			print(Fore.RED+'Please Type Only Y or N')

def clear():
	sp.call('clear', shell=True)


if __name__ == '__main__':
	main()
