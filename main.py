import subprocess
import thread
import time
import os
from keystrokes import *
from winsound import *

def launch_fight():
    # launch_game
    os.chdir("E:\Games\sdlmame")
    subprocess.Popen("E:\Games\sdlmame\sdlmame64.exe")
    time.sleep(6)
    input_string_vc("hyper")
    time.sleep(0.5)
    enter_vc()

    # skip scenes and labels
    time.sleep(3)
    MessageBeep()
    for i in xrange(15):
        enter_vc()
        time.sleep(1)

    MessageBeep()
    # insert coins
    input_string_vc("55555555111")

    # select fighter

def main():
    launch_fight()

if  __name__ == "__main__":
    main()

