#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
import requests, re, platform, random
from os import system
from sys import platform as pl
from bs4 import BeautifulSoup as par

purple = '\033[95m'
blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
u = '\033[4m'

if pl == 'win32':
    system('color')

url = 'https://com.all-url.info/{}/{}/'
user_agent = 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
ubuntu_color = random.choice([yellow, cyan, end])
print(f'''{red}
            .-/+oossssoo+/-.  
        `:+ssssssssssssssssss+:`     
      -+ssssssssssssssssssyyssss+-       
    .ossssssssssssssssss{ubuntu_color}dMMMNy{red}sssso.       
   /sssssssssss{ubuntu_color}hdmmNNmmyNMMMMh{red}ssssss/    
  +sssssssss{ubuntu_color}hm{red}yd{ubuntu_color}MMMMMMMNddddy{red}ssssssss+
 /ssssssss{ubuntu_color}hNMMM{red}yh{ubuntu_color}hyyyyhmNMMMNh{red}ssssssss/   
.ssssssssd{ubuntu_color}MMMNh{red}ssssssssss{ubuntu_color}hNMMMd{red}ssssssss.  
+ssss{ubuntu_color}hhhyNMMNy{red}ssssssssssss{ubuntu_color}yNMMMy{red}sssssss+  {green}  Mr.Crifty - Forze-XPLOIT{red}
oss{ubuntu_color}yNMMMNyMMh{red}ssssssssssssss{ubuntu_color}hmmmh{red}ssssssso  {green}  Priv8 Mass Grabber V.2 New Api{red}
oss{ubuntu_color}yNMMMNyMMh{red}sssssssssssssshmmmh{red}ssssssso  {green}  Server: {platform.platform()} {red}
+ssss{ubuntu_color}hhhyNMMNy{red}ssssssssssssy{ubuntu_color}NMMM{red}ysssssss+  {green}  Date: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')} {red}
.ssssssss{ubuntu_color}dMMMNh{red}ssssssssss{ubuntu_color}hNMMMd{red}ssssssss.    
 /ssssssss{ubuntu_color}hNMMM{red}yh{ubuntu_color}hyyyyh{ubuntu_color}dNMMMNh{red}ssssssss/
  +sssssssss{ubuntu_color}dm{red}yd{ubuntu_color}MMMMMMMMddddy{red}ssssssss+
   /sssssssssss{ubuntu_color}hdmNNNNmyNMMMMh{red}ssssss/
    .ossssssssssssssssss{ubuntu_color}dMMMNy{red}sssso.
      -+sssssssssssssssss{ubuntu_color}yyy{red}ssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-. {end}\n''')

domain = int(input('Pilih angka (1-10000): '))
page = int(input('Page: '))
to = int(input('To Page: '))
tahun = input("Tahun: ")
bulan = input("Bulan: ")
tgls = input("Sampai tanggal: ")
save_filename = 'crifty.txt'


print('\n\n')
print('results are saved in '+save_filename)

num = 0
for i in range(page, to+1):
    try:
        req = requests.get(url.format(domain, i), headers={'User-Agent': user_agent}, timeout=50)
        domains = re.findall('<a href=https://com.all-url.info/com/([^>]*)/>', req.text)
        for yz in domains:
                num += 1
                print("\r[!] Found "+str(num)+" Domain ", end="")
                with open(save_filename, 'a') as sv:
                     sv.write(yz.strip().replace("\n","") + "\n")
    except:
        print('\r[-] Error di angka {}'.format(i))

for x in range(1, int(tgls)+1):
    if x < 10:
    	qq = "0"+str(x)
    else:
        qq = x
    query = bulan+"-"+str(qq)+"-"+tahun
    try:
       req = requests.get("https://www.desktopcatcher.com/wp-content/plugins/domaingrab/download.php?date="+query).text
       if "." in req:
            finds = req.strip().split("\n")
            icikiwir = 0
            for fn in finds:
                    icikiwir += 1
                    print("\r[+] Found {} Domain [{}]".format(str(icikiwir), query), end="")
                    with open(save_filename, 'a') as sv:
                         sv.write(fn.strip().replace("\n","") + "\n")
       else:
            print('\r[-] Error, domain not found [{}]'.format(query))
    except:
        print('\r[-] Error, domain not found [{}]'.format(query))


nek = 0
take = par(requests.get("https://whoisdatacenter.com/free-database", headers={"user-agent":"chrome"}).text, "html.parser")
for td in take.find_all("td", {"class":"first domain_name"}):
    nek += 1
    gets = td.find("a").text
    print("\r[•] Collect "+str(nek)+" Domain.. ", end="")
    with open(save_filename, "a") as sev:
         sev.write(gets+"\n")

print("\n[✓] Done proses\n")
