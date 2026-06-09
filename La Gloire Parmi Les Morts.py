from sys import stdout
import os
import time
def write(print):
    for i in print:
        stdout.write(i)
        stdout.flush()
        time.sleep(.086)
    next = input()
def auto(print):
    for i in print:
        stdout.write(i)
        stdout.flush()
        time.sleep(.086)
def dd(hp,act,death):
    if hp == 0 and act == 0:
        global deadach
        print('')
        print("You have died...")
        print("Would you like to try again?")
        res = input(":",).upper()
        if res == "NO":
            print("\033[1m GAME OVER \033[0m")
            act = 0
            quit()
        elif res == "YES":
            hp += 1000
            death +=1
        if death == 1 and deadach == "off":
            print("Achievement Unlocked:")
            print("\033[38;2;230;190;0mLazarus, come out!(John 11:43-44)\033[0m")
            achieve.append("Lazarus, come out!(John 11:43-44)(Revive for the first time)")
            deadach == "on"
    return hp, act
def firpoint(canend):
    if canend == 1:
        print('')
        print("Achievement Unlocked:")
        print("\033[38;2;230;190;0mOne Step Closer To The Truth\033[0m")
        achieve.append("One Step Closer To The Truth(Earn Your First Canon Ending point)")
    else:
        print("you've aquired another canon ending point.")
    return canend
#AHHHHHHHHH I must finish this stupid ass game cuz I...Just want to lowkey
notoriety = 0
hp = 1000
weap = ["Golden Dagger","Rapier",]
invent = ["\033[38;2;130;0;250mGrappling Hook\033[0m)","\033[38;2;135;62;35mMap of Switzerland\033[0m","\033[38;2;255;105;180mDried up viola flower\033[0m"]
allies = ["Horse",]
outfit = "regular"
achieve = []
smkbmb = 5
mon = 100
foodrat = 10
act = 1
kill_count = 0
canend = 0
death = 0
checkpoint = 0
deadach = "off"

#I really hope nobody reads these notes... They're just me lowkey rambling about my OC(cuz he's cool and my son and I just love this universe xp) and randomly droping lore...

txt = "La Gloire Parmi Les Morts"
space = "."
print( txt.center(100))
print("")
while act == 1:
    print(space.center(100))
    print(space.center(100))
    print(space.center(100))
    auto("       Act 1 - Et Quand On A Les Bras Ballants, La Maison Finit Par Avoir Des Gouttières")
    print("")
    print(space.center(100))
    print(space.center(100))
    print(space.center(100))
    auto("                                         \033[1mDecember 15, 1793\033[0m")
    print("")
    write("The storm is not dying down; it continues to intensify with every gallop of the horse below. The winds, wild and vile, shake the surrounding trees. The snow descending from the sky feels like small daggers piercing through the skin. Yet, none of it will quench the fire of your determination.")
    auto("It’s been months since you left France for this strange country. All of your journey has led you here: a foreign country far away from home, a place where the sun doesn't rise, the land of thieves and mercenaries, the land where those \033[3mcowards\033[0m ran away to.")
    auto("The loud galloping of the horse below stops as soon as you pull on the reins. It neighs and steps on its hind legs. The gates of the kingdom welcome your view, standing tall like an obelisk.")
    auto("You dismount the horse and slowly make your way towards the gates. Two guards standing side by side, both of them equipped with sabres.")
    print('')
    auto("")
    auto("What will you do?")
    auto("A: Kill the guards (requires a weapon)")
    auto("B: sneak past (requires:\033[38;2;130;0;250mGrappling Hook\033[0m)")
    auto("To check your stats, type 'C'")
    Q0 = input(":",).upper()
    while Q0 != "A" or Q0 !="B":
        dd(hp,act,death)
        if Q0 == "A":
            print("Are you sure?")
            qw = input(":",).upper()
            if qw == "YES":
                print(space.center(100))
                print(space.center(100))
                print(space.center(100))
                write("You manage to kill both guards but were wounded in the process")
                hp-=25
                notoriety+=20
                auto("Your current health is:",hp)
                print("")
                canend += 1
                break
            else:
                print("A: Kill the guards (requires a weapon)")
                print("B: sneek past (requires: \033[38;2;130;0;250mGrappling Hook\033[0m)")
                print("To check inventory, type 'C'")
                Q0 = input(":",).upper()
        elif Q0 == "B":
            print(space.center(100))
            print(space.center(100))
            print(space.center(100))
            auto("You silently retrieve, and while you are out of the guards vision, you run to the nearest wall of the border. You throw the hook, and it grips the edge of the border. You begin to climb slowly, making sure to check your surroundings with every step you take. You hear and see two guards approaching just as you are about to reach the ledge.")
            write("What should you do?")
            print("")
            auto("A: Ledge Kill(requires a weapon)")
            auto("B: Call horse (requires: \033[38;2;100;100;100mHorse\033[0m ally)")
            auto("C: Throw smoke bomb (requires: \033[38;2;0;40;255msmoke bomb\033[0m)")
            Q1 = input(":",).upper()
            if Q1 == "A":
                print(space.center(100))
                print(space.center(100))
                print(space.center(100))
                write("You successfully take out one of the guards by pulling him off the ledge and letting him fall to his death. You finish climbing but are surprised to see that there were more guards than you expected.")
                print("")
                auto("What should you do?")
                auto("A: Throw smoke bomb (requires: \033[38;2;0;40;255msmoke bomb\033[0m)")
                auto("B: Make a run for it")
                auto("C: Fight back (requires a weapon)")
                btwo = input(":",).upper()
                if btwo == "A":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write("You reach into your satchel and throw the smoke bomb at the guards. The bomb doesn't go off and they begin to approach you.")
                    auto('You slowly back away, raising your hands in surrender. Just as the guards are only a few inches away from you the smoke bomb goes off.')
                    auto("You quickly begin to descend into the country while the guards start coughing.")
                    print('')
                    auto('Your notoriety has increased')
                    notoriety+=35
                    auto("Your current notoriety is:",notoriety)
                    smkbmb-=1
                    print('')
                    auto("You now have:",smkbmb,"smoke bombs left")
                    break
                elif btwo == "B":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    auto('You decide to make a run for it...')
                    auto("It does not end in your favor")
                    auto('You hear the sound of muskets going off followed by multiple sharp pains through your body. You fall to the ground and the world starts to go dark')
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    print("\033[1mENDING 0: Le Destin du fou\033[0m")
                    hp = 0
                    act = 0
                elif btwo == "C":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    auto("You decide to stab your way out of confrontation.")
                    auto("You successfully end kill all five guards but are wounded in the process")
                    hp -=55
                    print('')
                    auto("Your current health is:",hp)
                    print("")
                    auto('After taking a small break, you resume your descend and successfully make it over the border.')
                    break
            elif Q1 =="B" and "Horse" in allies:
                auto("Are you sure?")
                horsedeath = input(":",).upper()
                if horsedeath =="YES":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    auto('You whistle for your horse, startling the guards above. You see them running past you, and they begin shouting at the animal. While they are distracted, you finally finish climbing up the border and, without a second thought, begin descending into the country. As you finally make it down, you hear multiple muskets going off, followed by a loud neigh.')
                    print('')
                    auto("You have lost an ally:")
                    auto("\033[38;2;100;100;100mHorse\033[0m has been removed")
                    print('')
                    allies.remove("Horse")
                    allies.append("None")
                    print("Your current ally list is:")
                    print(allies)
                    break
                elif horsedeath == "NO":
                    print("action canceled")
            elif Q1 == "C":
                auto("You reach for your satchel while keeping yourself steady with one hand. Quickly you pull out a smoke bomb and throw it over the ledge. You hear commotion coming from above followed by coughs once the bomb goes off.")
                auto("You finish climbing the ledge and quickly begin to descend on the country. You make it there once the smoke has disappeared.")
                smkbmb-=1
                print("")
                print('')
                auto("You now have:",smkbmb,"smoke bomb(s) left.")
                break
        elif Q0 == "C":
            for wep in weap:
                print("Your current weapons are:",wep)
            for items in invent:
                print("Your inventory has:",items)
            for allies in allies:
                print('Available allies:',allies)
            print("Your health is:",hp, "hp")
            print("Smoke Bombs:",smkbmb)
            print("You have:",mon,"francs to your name")
            print('')
            print("A: Kill the guards (requires a weapon)")
            print("B: Sneek In (requires:\033[38;2;130;0;250mGrappling Hook\033[0m)")
            print("To check your stats, type 'C'")
            Q0 = input(":",).upper()
    print("")
    if Q0 == "A":
        write("As you mount your horse and make it through the gates, you hear shouts coming from up the border. You turn to look back and see five guards shouting at you, the muskets pointing at you and the horse. You tell your horse 'allez!' and it speeds off.")
        write("Your notoriety has gone up:")
        print("Your current notoriety is:",notoriety)
        firpoint(canend)
    elif Q0 == "B" and "Horse" in allies:
        write("As you begin walking, you see that the guards at the entrance are closely observing your horse. Whistling for it is not an option. Hence, you walk away, hoping for the horse's well being...")
        print('')
        write("You have lost an ally:")
        write("\033[38;2;100;100;100mHorse\033[0m has been removed")
        print('')
        allies.remove("Horse")
        allies.append("None")
        print("Your current ally list is:")
        print(allies)
        print('')
        print("Achievement Unlocked:")
        print("\033[38;2;230;190;0mThe Journey Begins(Again)\033[0m")
        print('')
        achieve.append("The Journey Begins(Again)(Make it over the border in Act 1)")
    elif Q1 == "B" and "Horse" != allies:
        print("You run without looking back and only stop once you are out of breath. You collapse infront of a tree and rest against it. You run your hands through the bark wishing it was the pelt of your horse.")
        print("You sigh and extract the map with your free hand.")
        print('')
        print("Achievement Unlocked:")
        print("\033[38;2;230;190;0mAin't That a Warm Welcome?\033[0m")
        print('')
        achieve.append("Ain't That a Warm Welcome?(Sacrifice your horse in Act 1)")
    print('')
    print('')
    print("Now that you've made it into Switzerland, you must find the Kingdom ruled by \033[0;31mAldéric Tremblay\033[0m.")
    
    

# ending yay and achievements lol!!:
print("")
print(space.center(100))
print(space.center(100))
print(space.center(100))
print("Thanks for playing!")
print('')
print("Across your journey, you earned the following achievements:")
for OH in achieve:
    print(OH)
