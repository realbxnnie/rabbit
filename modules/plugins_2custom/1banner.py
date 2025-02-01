import time

from colorama import Fore
from glob import glob

print(f"\n{Fore.BLUE}Loading modules...{Fore.WHITE}\n")

sysmodules = glob("modules/plugins_1system/*")
sysmodules.remove("modules/plugins_1system/settings")
sysmodules.remove("modules/plugins_1system/__pycache__")

for i in sysmodules:
    print(f"{Fore.GREEN}Loaded module: {i.replace("modules/plugins_1system/", "")}{Fore.WHITE}")
    time.sleep(0.05)
print("\n")