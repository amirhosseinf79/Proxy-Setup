import os
import time

network = "Home"
prim_dns = "178.22.122.100"
sec_dns = "185.51.200.2"

f = open("stats.txt")
stat = f.readlines()[0]
f.close()

def setDns(prim=0,sec=0):
    if prim == 0 or sec == 0:
        print("Connecting DNS to Google")
        os.system(f'netsh interface ip set dns name="{network}" static 8.8.8.8')
        os.system(f'netsh interface ip add dns name="{network}" 8.8.4.4 index=2')
    else:
        print(f"Connecting DNS to {prim_dns} & {sec_dns}...")
        os.system(f'netsh interface ip set dns name="{network}" static {prim}')
        os.system(f'netsh interface ip add dns name="{network}" {sec} index=2')

def setProxy(toggle):
    if toggle==0:
        print("Setting Proxy off...")
    else:
        print("Setting Proxy on...")
    
    os.system(f"REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d {toggle} /f")

def toggleProxy():
    f=open("stats.txt","w+")
    if int(stat)==1:
        setDns(prim_dns,sec_dns)
        setProxy(0)
        f.write("0")
        return "Proxy Disabled"

    else:
        setDns()
        setProxy(1)
        f.write("1")
        return "Proxy Enabled"
    f.close()


print(toggleProxy())
time.sleep(1)