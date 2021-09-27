import os
import time

network = "Home"
prim_dns = "178.22.122.100"
sec_dns = "185.51.200.2"

f = open("stats.txt")
stat = f.readlines()[0]
f.close()

def toggleProxy():
	f=open("stats.txt","w+")
	if int(stat)==1:
		os.system(f'netsh interface ip set dns name="{network}" static {prim_dns}')
		os.system(f'netsh interface ip add dns name="{network}" {sec_dns} index=2')
		os.system("REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 0 /f")
		f.write("0")
		return "Proxy Disabled"

	else:
		os.system(f'netsh interface ip set dns name="{network}" static 8.8.8.8')
		os.system(f'netsh interface ip add dns name="{network}" 8.8.4.4 index=2')
		os.system("REG ADD \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 1 /f")
		f.write("1")
		return "Proxy Enabled"
	f.close()


print(toggleProxy())
time.sleep(1)