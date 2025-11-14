import os
import subprocess
from colorama import Fore

def recursiveMake(dirs):
	for subdir in os.walk(dirs, topdown=False, onerror=None):
		if ("linux" in subdir[0]):
			continue
		if ("Makefile" not in os.listdir(subdir[0])):
			continue
		print(Fore.WHITE + subdir[0])
		result = subprocess.run(("cd " + subdir[0] +" && make re 2>/dev/null"), shell=True, executable="/bin/bash", capture_output=True, text=True)
		if (result.returncode != 0):
			print(Fore.RED + "ERROR" + result.stderr)
		else :
			print(Fore.GREEN + "OK !")
			
print("Compile status")
for dirs in os.listdir("."):
	if (not os.path.isdir(dirs)):
		continue
	print(Fore.WHITE + dirs)
	recursiveMake(dirs)
