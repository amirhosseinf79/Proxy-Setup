import os
import sys
import time

network = "Ethernet"
try: mode = sys.argv[1]
except: mode = "Default"

try: DNS = sys.argv[2]
except: DNS = "Default"

if DNS=="Electro":
	provider = "Electro"
	prim_dns = "185.231.182.126"
	sec_dns = "37.152.182.112"
elif DNS=="begzar":
	provider = "Begzar"
	prim_dns = "185.55.226.26"
	sec_dns = "185.55.225.25"
else:
	provider = "Shecan"
	prim_dns = "178.22.122.100"
	sec_dns = "185.51.200.2"
    
valorant_path = "E:\Riot Games\Riot Client\RiotClientServices.exe"

f = open("stats.txt")
try: stat = int(f.readlines()[0])
except: stat = 0
f.close()

print(f"\n\nMode: {mode}")
print("-"*33)
print(f"DNS Provider: {provider}")
print(f"Primary DNS: {prim_dns}")
print(f"Secondary DNS: {sec_dns}")
print("-"*33, end="\n")

def setDns(prim=0,sec=0):
    if mode != "onlyProxy":
        if prim == 0 or sec == 0:
            print("Connecting DNS to Google")
            os.system(f'netsh interface ip set dns name="{network}" static 8.8.8.8')
            os.system(f'netsh interface ip add dns name="{network}" 8.8.4.4 index=2')
        else:
            print(f"Connecting DNS to {prim} & {sec}...")
            os.system(f'netsh interface ip set dns name="{network}" static {prim}')
            os.system(f'netsh interface ip add dns name="{network}" {sec} index=2')

def setProxy(toggle):
    if mode!="onlyDNS":
        if toggle==0: print("Setting Proxy off...")
        else: print("Setting Proxy on...")
        os.system(f"REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d {toggle} /f")

    return str(toggle)

def toggleProxy(stat):
    if mode=="valorant":
        os.system(f'start "" "{valorant_path}" --launch-product=valorant --launch-patchline=live')
        stat = 1

    f=open("stats.txt","w+")
    if stat==1:
        f.write(setProxy(0))
        setDns(prim_dns,sec_dns)
        if mode == "onlyDNS": return "DNS Enabled"
        elif mode == "onlyProxy": return "Proxy Disabled"
        else: return "DNS Enabled\nProxy Disabled"
    else:
        f.write(setProxy(1))
        setDns(0,0)
        if mode == "onlyDNS": return "DNS Disabled"
        elif mode == "onlyProxy": return "Proxy Enabled"
        else: return "DNS Disabled\nProxy Enabled"
    f.close()


print(toggleProxy(stat))
time.sleep(2)