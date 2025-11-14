import os
import subprocess
from colorama import Fore

print("remote status")
for d in os.listdir("."):
	if (not os.path.isdir(d)):
		continue
	print(Fore.WHITE + d)
	os.system("git submodule update --remote --recursive 2>/dev/null")
	result = subprocess.run(("cd "+d+" && LANG=en_GB git status | grep 'nothing to commit' | wc -l"), shell=True, executable="/bin/bash", capture_output=True, text=True)
	if (result.returncode != 0):
		print(Fore.RED + "ERROR")
	if (int(result.stdout) == 1):
		print(Fore.GREEN + "OK !")
	else:
		problem = subprocess.run("cd "+d+" && LANG=en_GB git status", shell=True, executable="/bin/bash", capture_output=True, text=True)
		print(Fore.RED + problem.stdout)
