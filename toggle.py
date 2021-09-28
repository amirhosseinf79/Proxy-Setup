import os
import sys
import time

network = "Home"

if sys.argv[1]=="valorant":
	provider = "Electro"
	prim_dns = "185.231.182.126"
	sec_dns = "37.152.182.112"
else:
	provider = "Shecan"
	prim_dns = "178.22.122.100"
	sec_dns = "185.51.200.2"
    
valorant_path = "E:\Riot Games\Riot Client\RiotClientServices.exe"

f = open("stats.txt")
stat = f.readlines()[0]
f.close()

print(f"DNS Provider: {provider}")
print(f"Primary DNS: {prim_dns}")
print(f"Secondary DNS: {sec_dns}")
print("-"*33)

def setDns(prim=0,sec=0):
    if prim == 0 or sec == 0:
        print("Connecting DNS to Google")
        os.system(f'netsh interface ip set dns name="{network}" static 8.8.8.8')
        os.system(f'netsh interface ip add dns name="{network}" 8.8.4.4 index=2')
    else:
        print(f"Connecting DNS to {prim} & {sec}...")
        os.system(f'netsh interface ip set dns name="{network}" static {prim}')
        os.system(f'netsh interface ip add dns name="{network}" {sec} index=2')

def setProxy(toggle):
    if toggle==0:
        print("Setting Proxy off...")
    else:
        print("Setting Proxy on...")
    
    os.system(f"REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d {toggle} /f")

def toggleProxy():
    if sys.argv[1]=="valorant":
        os.system(f'start "" "{valorant_path}" --launch-product=valorant --launch-patchline=live')
    
    f=open("stats.txt","w+")
    if int(stat)==1:
        setProxy(0)
        f.write("0")
        setDns(prim_dns,sec_dns)
        return "Proxy Disabled"

    elif int(stat)==0 and sys.argv[1]!="valorant":
        setProxy(1)
        setDns(0,0)
        f.write("1")
        return "Proxy Enabled"
    else:
        f.write(stat)
        setDns(prim_dns,sec_dns)
        return "Proxy Already Disabled"
    
    f.close()
    


print(toggleProxy())
time.sleep(2)
