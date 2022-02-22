from sys import platform
import subprocess
import random
import time

if platform.startswith("linux"):
    shutdown = "shutdown now"
elif platform in ["win32", "cygwin"]:
    shutdown = "shutdown /s"

shut = random.randint(0, 6)

player = True
for drum in range(6):
    if player:
        input(f"drum {drum+1}.")
        if drum == shut:
            print("o7")
            subprocess.run(shutdown, shell=True)
        else:
            print("no shut")
    else:
        print(f"drum {drum+1}.")
        time.sleep(3)
        if drum == shut:
            print("You win!!")
        else:
            print("no shut")
    
    player = not player
