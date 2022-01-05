import os
import time
import how
import why
#make zac funny
x=3
while x==3:    
    print(" __  __       _          ______            ______                       ")
    print("|  \/  |     | |        |___  /           |  ____|                      ")
    print("| \  / | __ _| | _____     / / __ _  ___  | |__ _   _ _ __  _ __  _   _ ")
    print("| |\/| |/ _` | |/ / _ \   / / / _` |/ __| |  __| | | | '_ \| '_ \| | | |")
    print("| |  | | (_| |   <  __/  / /_| (_| | (__  | |  | |_| | | | | | | | |_| |")
    print("|_|  |_|\__,_|_|\_\___| /_____\__,_|\___| |_|   \__,_|_| |_|_| |_|\__, |")
    print("                                                                    __/|")
    print("                                                                    ___/")
    print("\nMake a selection:")
    print("(A) Make Zac Funny")
    print("(B) Why am I making this?")
    print("(C) Quit")
    selection=input(": ")
    sel=selection.lower()
    if sel=="a":
        how.make()
    if sel=="b":
        why.why()
    if sel=="c":
        exit()