import os
import os.path
import subprocess
import time

while True:
	if os.path.isfile("_data/public_html/restart_me_please"):
		p = subprocess.Popen(["docker", "compose", "down"])
		p.wait()
		os.remove("_data/public_html/restart_me_please")
		p = subprocess.Popen(["docker", "compose", "up", "-d"])
		p.wait()
	time.sleep(2)
