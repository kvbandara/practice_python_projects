

print("🌴 Welcome to 'The Curse of the Eye' 🌴")
print("You are a lone explorer, lost in the heart of an uncharted jungle.")
print("You come across a muddy, forked road under the thick jungle canopy.")
print("Would you like to turn left or right?")

answer =input("Type 'left' or 'right': ").lower()
if answer == "left":
    print("\nYou turn left and push through thorny bushes.")
    print("A crow suddenly screeches overhead, and a strange symbol appears glowing on a tree.")
    print("Do you follow the glowing symbols or turn back?")

    answer = input("Type 'follow' or 'back': ")
    if answer == "follow":
        print("\nYou follow the symbols deeper until you reach a large stone gate covered in moss.")
        print("It has three levers: 'Fire', 'Water', and 'Wind'. One opens the gate. Two trigger traps.")
        answer = input("Which lever will you pull? Type 'fire', 'water', or 'wind': ").lower()

        if answer =="wind":
            print("\n🌀 The gate rumbles and opens, revealing a spiral staircase into the earth.")
            print("You descend into a silent underground temple lit by blue crystals.")
            print("At the center lies a glowing orb — the Eye of Eternity.")
            print("Do you touch it or observe it carefully?")

            answer = input("Type 'touch' or 'observe': ").lower()

            if answer == "observe":
                print("\nYou notice an inscription around it: 'Only the patient shall possess the truth.'")
                print("You wait, and the orb opens, revealing a map and a golden key.")
                print("You take both and escape the temple just before it collapses.")
                print("🏆 Ending: The Wise Adventurer — You unlocked the secrets of the jungle!")
            elif answer == "touch":
                print("\nAs you grab the Eye, the room shakes and the ground cracks beneath you.")
                print("A shadowy figure whispers: 'Greed has a price.'")
                print("You fall into darkness forever.")
                print("💀 Ending: Cursed by the Eye")
            else:
                print("You hesitate. A trap is triggered and arrows shoot from the walls. Game Over.")
        else:
            print("\n🔥 The lever triggers a hidden flame trap. You’re engulfed in fire. Game Over.")
    elif answer == "back":
        print("\nYou try to head back, but the path is gone. Vines close around you.")
        print("You are never seen again.")
        print("💀 Ending: Lost in Time")
    else:
        print("You wait too long. The ground crumbles under you. Game Over.")

elif answer == "right":
    print("\nYou walk to the right and find a rickety old rope bridge over a foggy chasm.")
    print("Do you cross the bridge or look for another way?")

    answer = input("Type 'cross' or 'search': ").lower()

    if answer == "search":
        print("\nBehind a waterfall, you find a secret cave. Inside is a man with glowing eyes.")
        print("He offers to guide you to treasure in exchange for your voice.")
        print("Do you accept his offer or refuse?")

        answer = input("Type 'accept' or 'refuse': ").lower()

        if answer == "accept":
            print("\nYou lose your voice instantly. The man smiles and vanishes.")
            print("A path lights up and leads you to a golden statue with the Eye embedded in it.")
            print("But now, without your voice, you cannot speak the spell to claim it.")
            print("💀 Ending: The Silent Treasure Hunter")
        elif answer == "refuse":
            print("\nThe man hisses and dissolves into dust. A glowing path appears anyway.")
            print("You follow it and find the Eye. You return with riches and your soul intact.")
            print("🏆 Ending: Brave and Clever — True treasure seeker.")
        else:
            print("You freeze. The cave seals shut behind you. Game Over.")
    elif answer == "cross":
        print("\nHalfway across, the bridge snaps! You fall into the mist below.")
        print("But instead of death, you land in a hidden temple pool.")
        print("A whisper says: 'One who falls may rise... if worthy.'")
        print("Do you dive deeper or swim to shore?")

        answer = input("Type 'dive' or 'shore': ").lower()

        if answer == "dive":
            print("\nYou dive and find the Eye of Eternity held by a golden serpent.")
            print("You grab it. The serpent fades. You've proven your bravery.")
            print("🏆 Ending: The Chosen One — Destiny fulfilled.")
        elif answer == "shore":
            print("\nYou swim to shore and escape the jungle, but the Eye is lost forever.")
            print("🏆 Ending: Survivor — Alive, but empty-handed.")
        else:
            print("You hesitate too long. The pool turns black. Game Over.")
    else:
        print("You get lost in the mist and vanish without a trace. Game Over.")
else:
    print("You stand still, unable to decide. The jungle watches... and then consumes you. Game Over.")


























