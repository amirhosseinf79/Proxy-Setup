import os
import sys
import time
import json

debug = 0

try: MODE = sys.argv[1]
except: MODE = "Global"

try: DNS = sys.argv[2]
except: DNS = "Default"

f=open("Config.json")
data = json.load(f)
f.close()

network = data["network"]

provider = data["DNS"][-1]["provider"]
prim_dns = data["DNS"][-1]["prim_dns"]
sec_dns = data["DNS"][-1]["sec_dns"]

for dns in data["DNS"]:
    if DNS == dns["call"]:
        provider = dns["provider"]
        prim_dns = dns["prim_dns"]
        sec_dns = dns["sec_dns"]
        break
    
valorant_path = data["VAL_PATH"]

f = open("stats.txt")
try: stat = int(f.readlines()[0])
except: stat = 0
f.close()

debugtitle = "(Debug Mode)" if debug else ""
print(f"\n\nMode: {MODE} {debugtitle}")
print("-"*33)
print(f"Network: {network}")
print(f"DNS Provider: {provider}")
print(f"Primary DNS: {prim_dns}")
print(f"Secondary DNS: {sec_dns}")
print("-"*33, end="\n")

def setDns(prim=0,sec=0):
    if MODE != "onlyProxy":
        if prim == 0 or sec == 0:
            print("Connecting DNS to Google")
            if debug == 0:
                os.system(f'netsh interface ip set dns name="{network}" static 8.8.8.8')
                os.system(f'netsh interface ip add dns name="{network}" 8.8.4.4 index=2')
        else:
            print(f"Connecting DNS to {prim} & {sec}...")
            if debug == 0:
                os.system(f'netsh interface ip set dns name="{network}" static {prim}')
                os.system(f'netsh interface ip add dns name="{network}" {sec} index=2')

def setProxy(toggle):
    if MODE!="onlyDNS":
        if toggle==0: print("Setting Proxy off...")
        else: print("Setting Proxy on...")
        if debug == 0:
            os.system(f"REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d {toggle} /f")

    return str(toggle)

def toggleProxy(stat):
    if MODE=="valorant":
        if debug == 0:
            os.system(f'start "" "{valorant_path}" --launch-product=valorant --launch-patchline=live')
        stat = 1

    f=open("stats.txt","w+")
    if stat==1:
        f.write(setProxy(0))
        setDns(prim_dns,sec_dns)
        if MODE == "onlyDNS": return "DNS Enabled"
        elif MODE == "onlyProxy": return "Proxy Disabled"
        else: return "DNS Enabled\nProxy Disabled"
    else:
        f.write(setProxy(1))
        setDns(0,0)
        if MODE == "onlyDNS": return "DNS Disabled"
        elif MODE == "onlyProxy": return "Proxy Enabled"
        else: return "DNS Disabled\nProxy Enabled"
    f.close()


print(toggleProxy(stat))
if debug == 0: time.sleep(2)
else: os.system("pause")