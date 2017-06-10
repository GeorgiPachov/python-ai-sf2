import subprocess
import thread
import time
import os
from directxinput import *
from keystrokes import *

def launch_fight():
    # launch_game
    os.chdir("E:\Games\sdlmame")
    subprocess.Popen("E:\Games\sdlmame\sdlmame64.exe")
    time.sleep(6)
    input_string_vc("hyper")
    time.sleep(0.5)
    enter_vc()

    # skip scenes and labels
    time.sleep(10)
    for i in xrange(100):
        # key_sc(28) # Enter = 28, 0x1C
        enter_vc()
        time.sleep(1)

    # insert coins
    time.sleep(5)
    input_string_sc("55555555111")

    # select fighter

def main():
    launch_fight()

if  __name__ == "__main__":
    main()

