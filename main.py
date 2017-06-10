import subprocess
import thread
import time
import os
from directxinput import *
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
    time.sleep(5)
    MessageBeep()
    for i in xrange(25):
        # enter_vc()
        # key(DICT_SC["RETURN"])
        key_sc(28)
        time.sleep(1)

    MessageBeep()
    # insert coins
    # input_string_sc("55555555111")
    # input_string_vc("55555555111")
    for i in xrange(10):
        key_sc(6)
        time.sleep(1)
    for i in xrange(5):
        key_sc(2)

    # select fighter

def main():
    launch_fight()

if  __name__ == "__main__":
    main()

