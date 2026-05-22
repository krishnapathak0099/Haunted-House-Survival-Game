import pyttsx3
import time
import sys
def speek(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text1 = ('''
It is late night.
You are going to your home..
Ohhhh shitt....
Your car breaks down on an empty road during heavy rain...
There is no signal...
No help....
Ahead of you, you see an old mansion.
The door is slightly open.
You have no choice… you entered the home
the door opens and you went inside
''')
print(text1)
speek(text1)

text2 = ('''The door shuts behind you on its own.
You hear footsteps upstairs… but no one is there.
You see two paths:
A) Go upstairs
B) Explore the ground floor''')

print(text2)
speek(text2)
#----------------------------------------------------------------------------------------
c = input("Enter your choice: ").lower()
if(c == "a"):
    text3 = ('''
    You slowly walk up the stairs.
    The wood creaks loudly.
    At the top, there are three doors
    
    A1) Red Door (locked but shaking)
    A2) Blue Door (cold wind coming out)
    A3) Old Mirror Room (mirror covered with cloth)
    Choose wiselyy''')

    print(text3)
    speek(text3)
    c = input("Enter your choice: ").lower()
    if(c=="a1" ):
        text4 = ('''
    You force it open.
    Inside, you see a child sitting in the corner crying.
    When you approach:
    The child turns into a shadow and attacks you.''')

        print(text4)
        speek(text4)
        print("GAME OVERR\nYOU ARE POSSESSED")

    elif(c=="a2" ):
        text5 = ('''
A freezing wind pushes you inside.
The room is empty… but you hear whispers calling your name.
Suddenly, the door disappears.
        ''')
        print(text5)
        speek(text5)
        print("GAME OVER\nYOU ARE TRAPPED FOR EVER")

    elif(c=="a3"):
        text5 = ('''
You remove the cloth.
Your reflection does NOT copy you.
It smiles… even when you don’t.
The mirror starts glowing''')
        print(text5)
        speek(text5)
        print("YOU ESCAPED THE HOUSE.\nBUT THE REFLECTION IS STILL INSIDE")
    sys.exit()

#-------------------------------------------------------------------------------------------------

if(c=="b"):
    textb = ('''
You enter a dusty living room.
A radio turns on by itself.
It says:
"Do not go upstairs…"
You see:
B1) Kitchen (lights flickering)
B2) Basement door (locked but shaking) ''')
    print(textb)
    speek(textb)
    c = input("Enter your choice: ").lower()
    if(c=="b1"):
        textb1 = ('''
You find food on the table… still warm.
Suddenly, the fridge opens by itself.
Something is inside… but you don’t see it clearly.''')
        print(textb1)
        speek(textb1)
        print("YOU SURVIVED\nBUT NEVER LEAVE THE HOUSE")

    elif(c=="b2" ):
        textb2 = ('''
The door opens slowly by itself.
A strong smell of death comes out.
You hear multiple voices calling you to come down.''')
        print(textb2)
        speek(textb2)
        print("YOU DISCOVERED THE TRUTH\nBUT NOONE GONNA SEE YOU AGAIN")

#------------------------------------------------------------------------------------------
