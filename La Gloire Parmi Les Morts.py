from sys import stdout
import os
import time 
def write(print):
     for i in print:
        stdout.write(i)
        stdout.flush()
        time.sleep(.080)
     next = input()
def dd(hp,deaths):
    deaths +=1
    if hp == 0:
        global deadach
        print('')
        print("You have died...")
        print("Would you like to try again?")
        res = input(":",).upper()
        if res == "NO":
            print("\033[1m GAME OVER \033[0m")
            quit()
        elif res == "YES":
            hp += 1000
        if deaths == 1 and deadach == "off":
            print("Achievement Unlocked:")
            print("\033[38;2;230;190;0mLazarus, come out!(John 11:43-44)\033[0m")
            achieve.append("Lazarus, come out!(John 11:43-44)(Revive for the first time)")
            deadach == "on"
        elif deadach == "on" and deaths != 1:
            print("You have died again")
    return hp,deaths


def firpoint(canendpoints):
    if canendpoints == 1:
        print('')
        print("Achievement Unlocked:")
        print("\033[38;2;230;190;0mOne Step Closer To The Truth\033[0m")
        achieve.append("\033[38;2;230;190;0mOne Step Closer To The Truth\033[0m (Earn Your First Canon Ending point)")
    else:
        print("you've acquired another canon ending point.")
    return canendpoints
deadach = "off"
notoriety = 0
hp = 1000
weap = ["Golden Dagger","Rapier",]
invent = ["\033[38;5;212mGrappling Hook\033[0m)","\033[38;2;135;62;35mMap of Switzerland\033[0m","\033[38;2;130;0;250mDried up viola flower\033[0m","\033[38;2;135;7;250mList of 14 names\033[0m"]
allies = ["Horse",]
outfit = "regular"
achieve = []
smkbmb = 5
mon = 100
foodrat = []
act = 1
kill_count = 0
canon_kills = 0
canendpoints = 0
deaths = 0




#I really hope nobody reads these notes... They're just me lowkey rambling about my OC(cuz he's cool and my son and I just love this universe xp) and randomly dropping lore...


txt = "La Gloire Parmi Les Morts"
space = "."
print( txt.center(100))
print("")
while act == 1:
    Q0 = None
    dd(hp,deaths)
    print(space.center(100))
    print(space.center(100))
    print(space.center(100))
    write("       Act 1 - Et Quand On A Les Bras Ballants, La Maison Finit Par Avoir Des Gouttières")
    print("")
    print(space.center(100))
    print(space.center(100))
    print(space.center(100))
    write("                                         \033[1mDecember 15, 1793\033[0m")
    print("")
    write("The storm is not dying down; it continues to intensify with every gallop of the horse below. The winds, wild and vile, shake the surrounding trees. The snow descending from the sky feels like small daggers piercing through the skin. Yet, none of it will quench the fire of your determination.")
    write("It's been months since you left France for this strange country. All of your journey has led you here: a foreign country far away from home, a place where the sun doesn't rise, the land of thieves and mercenaries, the land where those \033[3mcowards\033[0m ran away to.")
    write("The loud galloping of your horse stops as soon as you pull on the reins. It neighs, stepping on its hind legs before becoming still.")
    print("")
    write("The gates of the kingdom welcome your view, standing tall like a mysterious obelisk.")
    print("")
    write("You dismount your horse and slowly make your way towards the gates.") 
    write("Two guards standing side by side, both of them equipped with sabres.")
    print("")
    print("")
    #yay first choice... Yuppie!
    print("What should you do you do?")
    write("A: Kill the guards (requires a weapon)")
    write("B: Sneak past (requires:\033[38;5;212mGrappling Hook\033[0m)")
    write("To check your stats, type 'C'")
    Q0 = input(":",).upper()
    while Q0 != "A" or Q0 !="B":
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
                write("Your current health is:")
                print(hp)
                print("")
                canendpoints += 1
                break
            else:
                print("A: Kill the guards (requires a weapon)")
                print("B: Sneak past (requires:\033[38;5;212mGrappling Hook\033[0m)")
                print("To check inventory, type 'C'")
                Q0 = input(":",).upper()
        elif Q0 == "B":
            Q1 = None
            print(space.center(100))
            print(space.center(100))
            print(space.center(100))
            write("You silently retrieve, and while you are out of the guard's vision, you run to the nearest wall of the border.") 
            write("You wind up the rope of the hook before throwing it over the border.") 
            write("You begin to climb slowly, making sure to check your surroundings with every step. The coast seems clear... for now")
            print("")
            print("")
            write("A few minutes pass; you are close to reaching the top of the border when suddendly-")
            write("You hear commotion approaching and see the silhouette of two guards nearing your location.")
            write("What should you do?")
            print("")
            write("A: Ledge Kill(requires a weapon)")
            write("B: Call horse (requires: \033[38;2;100;100;100mHorse\033[0m ally)")
            write("C: Throw smoke bomb (requires: \033[38;2;0;40;255msmoke bomb\033[0m)")
            Q1 = input(":",).upper()
            if Q1 == "A":
                print(space.center(100))
                print(space.center(100))
                print(space.center(100))
                write("One of your hands reaches for the top of the border, and with you propel yourself forward.")
                write("A guard sees you but you manage to grip the back of his cape and pulling towards the edge.")
                write("You successfully take him out by pulling him off and letting him fall to his deaths.") 
                write("You finish climbing but are surprised to see more guards than you expected.")
                write("They don't seem very content with what happened to their fellow guardsman.")
                print("")
                write("What should you do?")
                print("A: Throw smoke bomb (requires: \033[38;2;0;40;255msmoke bomb\033[0m)")
                print("B: Make a run for it")
                print("C: Fight back (requires a weapon)")
                btwo = input(":",).upper()
                if btwo == "A":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write("You reach into your satchel and throw the \033[38;2;0;40;255msmoke bomb\033[0m at the guards.") 
                    write("Unfortunately, it doesn't go off and the guards begin to approach you slowly.")
                    write("You back away, raising your hands in surrender. You back way until your back touches a pillar.")
                    write("You see a vision flash before your eyes:")
                    write("It isn't positive...")
                    write("")
                    write("")
                    write("")
                    write("But, just as the guards are only a few inches away from you the smoke bomb finally goes off.")
                    write("You quickly run away and begin to descend into the country while the guards start coughing.")
                    print('')
                    write('Your notoriety has increased')
                    notoriety+=35
                    print("Your current notoriety is:",notoriety)
                    smkbmb-=1
                    print('')
                    print("You now have:",smkbmb,"smoke bombs left")
                    break
                elif btwo == "B":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write('You decide to make a run for it!')
                    write("")
                    write("It doesn't end in your favor...")
                    write("You see a vision flash before your eyes:")
                    write("It isn't positive...")
                    write("")
                    write("")
                    write("")
                    write('You hear the blast of muskets going off')
                    write("Suddendly, your entire body feels as if it were in flames.")
                    write("You fall to your knees and onto the ground below; coughing up blood.")
                    write("The world in front of you becomes a blur before being consumed by darkness...")
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write("\033[1mENDING 0: Le Destin du fou\033[0m")
                    hp = 0
                    Q1 = None
                    # deaths +=1
                elif btwo == "C":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write("You decide to stab your way out of confrontation.")
                    write("Some of the guards were easy to take out; others fought back fiercely. Nevertheless, none survived the assault.")
                    write("The five guards are gone, but you were wounded in the process...")
                    hp-=55
                    print('')
                    print("Your current health is:",hp)
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write('After taking a small break, you resume your descend and successfully make it over the border.')
                    break
            elif Q1 == "B" and "Horse" in allies:
                print("Are you sure?")
                horsedeaths = input(":",).upper()
                if horsedeaths =="YES":
                    print(space.center(100))
                    print(space.center(100))
                    print(space.center(100))
                    write('You whistle for your horse, startling the guards above. You see them running past you, and they begin shouting at the animal. While they are distracted, you finally finish climbing up the border and, without a second thought, begin descending into the country. As you finally make it down, you hear multiple muskets going off, followed by a loud neigh.')
                    print('')
                    write("You have lost an ally:")
                    write("\033[38;2;100;100;100mHorse\033[0m has been removed")
                    print('')
                    allies.remove("Horse")
                    allies.append("None")
                    print("Your current ally list is:")
                    print(allies)
                    break
                elif horsedeaths == "NO":
                    print("action canceled")
                    Q1 = None
            elif Q1 == "C":
                write("You reach for your satchel while keeping yourself steady with one hand.")
                write("The commotion draws near, and you hear someone yell 'Hey!' before hearing someone running.")
                write("You struggle to pull out a smoke bomb from your satchel and cause one of them to fall")
                smkbmb-=1
                write("The footsteps draw closer")
                write("And closer")
                write("...")
                write("...")
                write("...!")
                write("You finally manage to extract a smoke bomb,") 
                write("You quickly throw it over the ledge.") 
                write("The running stops...")
                write("And a loud \x1B[1;3mhiss\x1B[0m replaces it.")
                write("You finish climbing the ledge and quickly begin to descend on the country. You make it there once the smoke has disappeared.")
                smkbmb-=1
                print('')
                print("You now have:",smkbmb,"smoke bomb(s) left.")
                break
        elif Q0 == "C":
            for wep in weap:
                print("Your weapons are:",wep)
            for items in invent:
                print("Your inventory has:",items)
            for allies in allies:
                print('Available allies:',allies)
            print("Your health is:",hp, "hp")
            print("Smoke Bombs:",smkbmb)
            print("You have:",mon,"francs to your name")
            print('')
            print("A: Kill the guards (requires a weapon)")
            print("B: Sneak Past (requires:\033[38;5;212mGrappling Hook\033[0m)")
            print("To check your stats, type 'C'")
            Q0 = input(":",).upper()
    print("")
    if Q0 == "A":
        #LOL! Not Lazare aura farming during this moment...
        write("You return to your horse, mounting it once more and riding to the gates.")
        write("As pass into the country, you hear shouts coming from up the border.") 
        write("You turn to look back and see five guards shouting at you, the muskets pointing at you.") 
        write("You tell your horse \033[1;3m'allez!'\033[0m and it speeds off.")
        write("The a loud bang echoes through the country, yet none of the shots reach you...")
        print(space.center(100))
        print(space.center(100))
        print(space.center(100))
        write("Your notoriety has gone up:")
        print("Your current notoriety is:",notoriety)
        firpoint(canendpoints)
        write("Achievement Unlocked:")
        print("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m")
        print('')
        achieve.append("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m(Make it over the border in Act 1)")
    elif Q0 == "B" and "Horse" in allies:
        write("As you begin walking away, you see that the guards at the entrance are observing your horse.")
        write("The poor thing...")
        write("Whistling for it is not an option, killing the guards now would be reckless... ")
        write("You simply walk away, hoping for the animals's well being.")
        print(space.center(100))
        print(space.center(100))
        print(space.center(100))
        write("You have lost an ally:")
        write("\033[38;2;100;100;100mHorse\033[0m has been removed")
        print('')
        allies.remove("Horse")
        allies.append("None")
        write("Your current ally list:")
        print(allies)
        print('')
        write("Achievement Unlocked:")
        print("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m")
        print('')
        achieve.append("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m(Make it over the border in Act 1)")
    elif Q1 == "B" and "Horse" != allies:
        #why would anyone do this to the poor horse! (I made this an option; why am I complaining???)
        write("You run...")
        write("And run...")
        write("And run...")
        write("Until you are out of breath and collapse near a tree.")
        write("You rest against it, running your hands through the bark wishing it was the pelt of your horse.")
        write("The poor thing...")
        write("What did it ever do to deserve such fate?")
        write("You decide take a few minutes to catch your breath...")
        print("")
        print("")
        write("...")
        write("You sigh and extract the map from your satchel, along with the list of names...")
        print('')
        write("Achievement Unlocked:")
        print("\033[38;2;230;190;0mAin't That a Warm Welcome?\033[0m")
        print('')
        achieve.append("\033[38;2;230;190;0mAin't That a Warm Welcome?\033[0m(Sacrifice your horse in Act 1)")
        write("Achievement Unlocked:")
        print("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m")
        print('')
        achieve.append("\033[38;2;230;190;0mThe Crusade Begins(Again)\033[0m(Make it over the border in Act 1)")
    print("")
    print("")


# ending yay and achievements lol!!:
print("")
print(space.center(100))
print(space.center(100))
print(space.center(100))
print("\033[1mThanks for playing!\033[0m")
print('')
print("Across your journey, you earned the following achievements:")
for OH in achieve:
    print(OH)
