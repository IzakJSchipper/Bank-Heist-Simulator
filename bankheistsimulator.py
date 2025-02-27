import random
import sys
import time
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def wait():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()    

def nextpg():
    input("press enter to contenue...")


def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Random delay
    print()

security_level = random.randint(1, 10)



a = 0
b = 0
c = 0

def hacker_skill():
    global crew, security_level
    
    act = int(input(f"0 for Smart Guy, 1 for Strong Guy, 2 for Fast Guy: "))

    if crew[act]["hacklvl"] > security_level:
        print(f"since the security was {security_level}0 percent secure, {crew[act]["Name"]}'s hacker level of {crew[act]["hacklvl"]}0 percent was able to easily break through!")   
    else:
        print("You got caught... implement more logic here later.")

def moneycheck1():
    global a, b, c

    while True:
        a = int(input("Enter his percent of the cut in a numeric value of 1-100: "))
    
        if a + b + c <= 100:
            print(f"His cut will be {a} percent.")
            nextpg()
            break
        else:
            print("the split makes no sense, you can't steal more than 100 percent!")
        
def moneycheck2():
    global a, b, c

    while True:
        b = int(input("Enter his percent of the cut in a numeric value of 1-100: "))
    
        if a + b + c <= 100:
            print(f"His cut will be {b} percent.")
            nextpg()
            break
        else:
            print("the split makes no sense, you can't steal more than 100 percent!")

def moneycheck3():
    global a, b, c

    while True:
        c = int(input("Enter his percent of the cut in a numeric value of 1-100: "))
    
        if a + b + c < 100:
            print(f"They realize, the total percent is only {a + b + c}")
            print("less than 100...")
            print("maybe give the fast guy some more money?")
        elif a + b + c == 100:
            print(f"His cut will be {c} percent.")
            nextpg()
            break
        else:
            print(f"{a + b + c} percent? you can't steal more than 100 percent!")
                


cash = 1

crew = [
    {
        "Name" : "Smart-Guy",
        "hacklvl" : 9,
        "stronglvl" : 2,
        "speed" : 2,
        "split" : a % cash,
    },
    {
        "Name" : "StrongGuy",
        "hacklvl" : 1,
        "stronglvl" : 8,
        "speed" : 5,
        "split" : b % cash,
    },
    {
        "Name" : "FastGuy",
        "hacklvl" : 4,
        "stronglvl" : 5,
        "speedlvl" : 9,
        "split" : c % cash,
    },
]

hackdiff = random.randint(1, 10)
punchdiff = random.randint(1, 10)
runawaydiff = random.randint(1, 10)

clear_screen()

type_text("Welcome to", delay=0.05)
wait()
type_text("", delay=0.07)
type_text("\033[41mThe Bank Heist.\033[0m", delay=0.07)

type_text("", delay=0.07)
type_text("", delay=0.07)
type_text("", delay=0.07)


type_text("You are watching a gang of 3", delay=0.07)
type_text("FRIENDS", delay=0.06)
type_text(" ", delay=2)
type_text("\033[44mDefinatly NOT bank robbers.\033[0m", delay=0.07)
type_text("", delay=0.07)
type_text("But they just so happend to decide one day, to rob a bank.", delay=0.05)
type_text("And as a first order of buisness,", delay=0.05)
type_text("they discuss how they should split the money.", delay=0.05)
type_text("As the god of this universe", delay=0.05)
type_text("you must decide how they do so.", delay=0.05)
nextpg()
clear_screen()
type_text("\033[44mFirst up, Smart Guy.\033[0m", delay=0.05)
type_text("He's good with the technical stuff.", delay=0.05)
type_text("But he's definatly never been on the track team.", delay=0.05)
type_text("And the heaviest thing he lifts is a bag of doritos.", delay=0.05)
type_text("But if you need something technical, he's your guy", delay=0.05)
type_text("so, what's his cut?", delay=0.05)
moneycheck1()
clear_screen()
type_text("\033[44mNext, Strong Guy.\033[0m", delay=0.05)
type_text("He's very strong.", delay=0.05)
type_text("Kinda fast.", delay=0.05)
type_text("But not known for solving puzzles...", delay=0.05)
type_text("so cliche...", delay=0.05)
type_text("anyways, what's his cut?", delay=0.05)
moneycheck2()
clear_screen()
type_text("\033[44mLastly, Fast Guy.\033[0m", delay=0.05)
type_text("Kinda an all arounder,", delay=0.05)
type_text("But he's the fastest around.", delay=0.05)
type_text("REALLY fast.", delay=0.05)
type_text("anyways, what's his cut?", delay=0.05)
moneycheck3()
clear_screen()

type_text("\033[44mChapter one, driving to the bank.\033[0m", delay=0.07)
type_text("the thre drive to the bank. It's outside of hours.", delay=0.03)
type_text("You must break into the bank, by hacking the security system.", delay=0.05)
type_text("Chose someone to do it", delay=0.05)
hacker_skill()