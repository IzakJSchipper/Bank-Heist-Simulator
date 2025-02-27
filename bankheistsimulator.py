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
door_strength = random.randint(1, 10)
police_speed = random.randint(1, 10)


a = 0
b = 0
c = 0

def hacker_skill():
    global crew, security_level
    
    type_text("\033[41m0 for Smart Guy, 1 for Strong Guy, 2 for Fast Guy\033[0m", delay=0.07)
    act = int(input(f"Chose wisely: "))

    if crew[act]["hacklvl"] > security_level:
        type_text(f"\033[42mSince the security was {security_level}0 percent secure, {crew[act]["Name"]}'s hacker level of {crew[act]["hacklvl"]}0 percent was able to easily break through!\033[0m", delay=0.03)   
    else:
        print("You got caught... implement more logic here later.")

def breaking_skill():
    global crew, door_strength
    
    type_text("\033[41m0 for Smart Guy, 1 for Strong Guy, 2 for Fast Guy\033[0m", delay=0.07)
    act = int(input(f"Chose wisely: "))

    if crew[act]["stronglvl"] > door_strength:
        type_text(f"\033[42mSince the door was {door_strength}0 percent reinforced, {crew[act]["Name"]}'s strength level of {crew[act]["stronglvl"]}0 percent was able to easily break through!\033[0m", delay=0.03)   
    else:
        print("You got caught... implement more logic here later.")        

def outrun_skill():
    global crew, police_speed
    
    type_text("\033[41m0 for Smart Guy, 1 for Strong Guy, 2 for Fast Guy\033[0m", delay=0.07)
    act = int(input(f"Chose wisely: "))

    if crew[act]["speed"] > police_speed:
        type_text(f"\033[42mSince the police were {police_speed}0 percent ready, {crew[act]["Name"]}'s speed level of {crew[act]["speed"]}0 percent allowed for him to run away and lead the crew to safety!\033[0m", delay=0.03)   
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
        "split" : (a / 100) * cash,
    },
    {
        "Name" : "StrongGuy",
        "hacklvl" : 1,
        "stronglvl" : 8,
        "speed" : 5,
        "split" : (b / 100) * cash,
    },
    {
        "Name" : "FastGuy",
        "hacklvl" : 4,
        "stronglvl" : 5,
        "speed" : 9,
        "split" : (c / 100) * cash,
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
nextpg()
clear_screen()
type_text("\033[44mChapter two, Breaking down the door.\033[0m", delay=0.07)
type_text("The three walk into the bank...", delay=0.03)
type_text("But... there is a physically locked door. Literally no way to sneekily break in or hack through something...", delay=0.05)
type_text("Chose someone to do it", delay=0.05)
breaking_skill()
nextpg()
clear_screen()
type_text("\033[44mChapter three, Running away!\033[0m", delay=0.07)
type_text("Boom! Jackpot!", delay=0.03)
cash = random.randint(100, 1000000000000)
type_text(f"\033[42mthey found {cash} USD!\033[0m", delay=0.03)
wait()
type_text("But... the sirens go off...", delay=0.05)
type_text("They notice that the police are already at the building.", delay=0.03)
type_text("Now they need to escape, someone has to find an escape plan.", delay=0.03)
outrun_skill()
nextpg()
clear_screen()

crew[0]["split"] = round((a / 100) * cash)
crew[1]["split"] = round((b / 100) * cash)
crew[2]["split"] = round((c / 100) * cash)


type_text("\033[42mChapter four, Reap the rewards!\033[0m", delay=0.07)
type_text("Congrats to the team!", delay=0.03)
type_text("Thanks to the teamwork, nobody had been caught!", delay=0.03)
type_text(f"Smart Guy made \033[42m{crew[0]["split"]}\033[0m, Strong Guy Made \033[42m{crew[1]["split"]}\033[0m, and Fast Guy made \033[42m{crew[2]["split"]}\033[0m.", delay=0.03)