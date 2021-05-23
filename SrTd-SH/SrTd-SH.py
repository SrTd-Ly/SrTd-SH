#/usr/bin/python
#SrTd_Ly

import requests
import sys
from termcolor import colored

print("""                                                             
            ───────────────────────────────────────
            ───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
            ───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
            ──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
            ──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
            ▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
            ▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
            ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
            ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
            ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
            ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
            ─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
            ─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
            ──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
            ──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
            ────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────
                 \*/ Coded By Omar M Erbeh \*/
                      [!] Social media [!]
                    facebook.com/Omar.alajeley.20    
            ░█▀▀▀█ █▀▀█ ▀▀█▀▀ █▀▀▄ ── ░█▀▀▀█  █──█ 
            ─▀▀▀▄▄ █▄▄▀ ─░█── █──█ ▀▀ ─▀▀▀▄▄  █▀▀█ 
            ░█▄▄▄█ ▀─▀▀ ─░█── ▀▀▀─ ── ░█▄▄▄█  ▀──▀ """)
            
host = sys.argv[1]

if host == '-h' or '--help':
    print("""
        ==================================================
        =   Use The Tool "http://" or "https://          =
        =   EX: python3 SrTd-SH.py https://site.com      =
        ==================================================
         """)
wordlist = [word.strip() for word in open('wordlist.txt').readlines()]

try:

    for word in wordlist:
        url = host+"/"+word


        with requests.session() as session:
            req = session.get(url)

        if req.status_code == 200 :
            print(colored('[+] Found [200] : ', 'blue'), colored(url, 'green'))

        elif req.status_code == 301 :

             print(colored('[~] Found redirect [301] : ', 'white'), colored(url, 'cyan‏'))

        elif req.status_code == 403 :
    
             print(colored('[-] Blocked [403] : ', 'magenta'), colored(url, 'blue'))


        else:
            
             print(colored('[-] Not Found ' +str(req.status_code) + ':' , 'red'), colored(url, 'yellow'))

 
            
except ValueError:
    sys.exit()
    
