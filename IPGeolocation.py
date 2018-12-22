'''
Subscribe To https://www.YouTube.com/CallMeCOM
Ensure you leave credits if you wish you use this script. Credits are nice and any dev likes that!
Enjoy.
'''
import requests, json, sys, time
import subprocess as sp
from colorama import Fore, init
init()

def main():
    clear()
    print(Fore.WHITE+'*'*37)
    print('+         '+Fore.CYAN+'Geolocation Script'+Fore.WHITE+'        +')
    print('*'*37)
    dankIP = raw_input(Fore.CYAN+'Please Enter IP Address: '+Fore.WHITE)
    try:
        r = requests.get('https://ipapi.co/'+dankIP+'/json')
        data = r.json()
        print('[+]'+'-'*32+'[+]'+Fore.CYAN)
        for i in data:
            print(str(i)+': '+str(data[i]))
        print(Fore.WHITE+'[+]'+'-'*32+'[+]')
    except Exception as e:
        print(str(e))
        pass

    restartBool = True
    while restartBool:
        restart = raw_input(Fore.CYAN+'Geolocate Another IP? (Y/N): '+Fore.WHITE)
        if restart.upper() == 'Y':
            main()
            restartBool = False
        elif restart.upper() == 'N':
            sys.exit('Closing The Dank Hax')
            restartBool = False
        elif restart != '':
            print(Fore.RED+'Please Type Only Y or N')

def clear():
    sp.call('clear', shell=True)

if __name__ == '__main__':
    main()
