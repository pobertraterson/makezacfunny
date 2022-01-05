import os
import time
topics = ["joke", "response", "dont", "don't"]
def make():
    os.system('cls')
    time.sleep(1)
    y=0
    while y!=3:
        x=input("How do we make Zac funny?\nType stop to finish\n: ")
        if "joke" in x:
            jokearray=[]
            print("Give 3 jokes to make Zac funny")
            z=0
            while z != 3:
                joke=input(": ")
                jokearray.append(joke)
                z=z+1
            print("So you gave the jokes:")
            print(*jokearray, sep=", ")
            f=open("jokes.txt", "a")
            f.write(jokearray)
            f.close()
        if x=='stop' or x=='STOP':
            break
        if "response" in x:
            responses=[]
            print("Give 3 whitty responses to make Zac funny")
            z=0
            while z != 3:
                resp=input(": ")
                responses.append(resp)
                z=z+1
            print("So you gave the jokes:")
            print(*responses, sep=", ")
            f=open("resp.txt", "a")
            f.write(responses)
            f.close()
        if "dont" or "don't" in x:
            print("Way to be optimistic...")
            time.sleep(1)
        else:
            print("That is not a valid response")
        y=y+1
    print("Your attempts to make Zac funny are futile because Zac will never be funny")
    time.sleep(3)