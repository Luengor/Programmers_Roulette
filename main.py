from sys import platform
import subprocess
import random
import time

if platform.startswith("linux"):
    shutdown = "shutdown now"
elif platform in ["win32", "cygwin"]:
    shutdown = "shutdown /p /f"

shut = random.randint(0, 6)

player = True
for drum in range(6):
    if player:
        input(f"drum {drum+1}, press enter to drum")
        time.sleep(1)
        if drum == shut:
            print("o7")
            time.sleep(0.5)
            subprocess.run(shutdown, shell=True)
            break
        else:
            print("no shut")
    else:
        time.sleep(2)
        print(f"drum {drum+1}, computer's turn")
        time.sleep(2)
        if drum == shut:
            print("You win!!")
            break
        else:
            print("no shut")
    
    player = not player
