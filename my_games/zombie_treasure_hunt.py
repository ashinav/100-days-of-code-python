print("\n========== SCENE 1 — THE NIGHTMARE ==========\n")

print("Scene 1 — The Nightmare\nIt is midnight. A boy is running through a dark, abandoned street.\nThe streetlights are flickering. Strange noises are coming from everywhere.\nSuddenly, he hears footsteps behind him.")

print("Boy: \"Who is there? Why is someone following me?\"\nHe turns around and sees a group of zombies running towards him!")
print("Boy: \"AHHH! ZOMBIES! HELP ME!\"\nHe starts running faster, but the zombies are getting closer.One zombie jumps towards him!\nBoy: \"NOOOOO!\"")


print("\n========== SCENE 2: THE AWAKENING ==========\n")

print("Suddenly, the boy wakes up, breathing heavily.")

print('Boy: "AHHH!"')

print("He looks around and wipes the sweat from his forehead.")

print('Boy: "Oh my God! What a horrible nightmare!"')

print('Boy: "Thank God... it was just a dream."')

print("He closes his eyes for a moment and tries to relax.")

print("But suddenly, he notices something strange.")

print('Boy: "Wait a minute..."')

print('Boy: "Where am I?"')

print("He looks around. The room is dark. The windows are broken. There is blood on the floor.")

print('Boy: "This is not my bedroom!"')

print("He runs towards the door, but it is locked.")

print("Suddenly, a strange voice comes from an old radio.")


print("\n========== SCENE 3: THE MYSTERIOUS MESSAGE ==========\n")

print('Radio: "Hello... hello... Can anyone hear me?"')

print('Boy: "Hello! Who are you? Where am I?"')

print('Radio: "Listen carefully! The city has been infected. Zombies are everywhere!"')

print('Boy: "WHAT?! ZOMBIES?!"')

print('Radio: "If you want to survive, find the secret laboratory. There is something inside that can save you."')

print('Boy: "But how do I get there?"')

print('Radio: "First, find a flashlight and a keycard. You will need both to enter the laboratory."')

print("Suddenly, the radio signal disappears.")

print('Boy: "Hello?! HELLO?!"')

print("Someone starts banging on the door.")

print('Boy: "Oh no... Please don\'t tell me..."')

print("A terrifying growl comes from outside.")

print('Boy: "MY NIGHTMARE IS REAL?!"')



print("\n========== SCENE 4: THE FIRST ESCAPE ==========\n")

health = 100
flashlight = False
keycard = False
police_note_found = False
game_won = False

print("Zombies are banging on the door!")
print('Boy: "I need to get out of here!"')

while health > 0:

    print("\nHealth:", health)

    print("\nWhat will you do?")
    print("1. Escape through the broken window")
    print("2. Try to break open the locked door")
    print("3. Hide inside the cupboard")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("You jump through the broken window!")
        print("You successfully escape from the room!")
        break

    elif choice == "2":
        print("You try to break the door, but it won't open!")
        health -= 20
        print("You lose 20 health!")

    elif choice == "3":
        print("You hide inside the cupboard.")
        print("But a zombie discovers you!")
        health -= 30
        print("You lose 30 health!")

    else:
        print("Invalid choice! Try again.")

if health <= 0:
    print("\nGAME OVER! The zombies caught you!")

else:
    print("\nYou have reached a safe location!")
    print("Remaining health:", health)
    print("Your adventure begins now!")
    
    

# =====================================
# SCENE 6 - ABANDONED SUPERMARKET
# =====================================

food_available = True

def supermarket():

    global health, flashlight, food_available

    print("\n========== SCENE 6: THE SUPERMARKET ==========\n")

    print("The boy enters an abandoned supermarket.")
    print('Boy: "Maybe I can find something useful here."')
    print("Suddenly, he hears a strange noise.")
    print('Boy: "Hello? Is someone there?"')

    while health > 0:

        print("\n========== SUPERMARKET MENU ==========")
        print("1. Search the Storage Room")
        print("2. Search for Food")
        print("3. Return to Safe House")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":

            if not flashlight:

                print("\nYou enter the storage room.")
                print("Suddenly, a zombie appears!")
                print('Boy: "AHHH! A ZOMBIE!"')

                print("\nWhat will you do?")
                print("1. Fight the Zombie")
                print("2. Run Away")

                action = input("Enter your choice: ")

                if action == "1":

                    health -= 20
                    print("\nYou fight the zombie!")
                    print("You lose 20 health.")

                    if health > 0:
                        print("You defeated the zombie!")
                        print("You found a flashlight!")
                        flashlight = True

                    else:
                        print("The zombie defeated you!")

                elif action == "2":

                    health -= 10
                    print("\nYou escape from the zombie!")
                    print("You lose 10 health.")

                    break

                else:
                    print("Invalid choice!")

            else:
                print("\nYou already collected the flashlight.")

        elif choice == "2":

            if food_available:

                print("\nYou found some food!")

                health = min(100, health + 15)
                food_available = False

                print("Health restored!")
                print("Current Health:", health)

            else:
                print("\nThere is no food left!")

        elif choice == "3":

            print("\nYou are returning to the Safe House.")
            break

        else:
            print("\nInvalid choice! Try again.")
            
    if health <= 0:
        print("\nGAME OVER! You did not survive!")
        

# ==========================================
# SCENE 7 - THE HAUNTED POLICE STATION
# ==========================================

def police_station():

    global health, keycard, police_note_found

    print("\n========== SCENE 7: POLICE STATION ==========\n")

    print("The boy enters an abandoned police station.")
    print('Boy: "Maybe I can find the keycard here."')
    print("The lights are flickering.")
    print("Suddenly, he hears a strange noise.")
    print('Boy: "What was that?!"')

    while health > 0:

        print("\n========== POLICE STATION MENU ==========")
        print("1. Search Reception Desk")
        print("2. Enter Evidence Room")
        print("3. Return to Safe House")
        print("4. Check Player Status")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":

            if not police_note_found:

                print("\nYou search the reception desk.")
                print("You find a mysterious note!")

                print("\n========== SECRET NOTE ==========")
                print("Evidence Locker PIN: 2468")
                print("Laboratory Access Code: 4321")
                print("=================================")

                police_note_found = True

                print("You remember both codes!")

            else:
                print("\nYou already found the secret note.")
                print("Locker PIN: 2468")
                print("Laboratory Code: 4321")

        elif choice == "2":

            if keycard:
                print("\nYou already collected the keycard!")

            elif not police_note_found:
                print("\nThe evidence room has a locked locker.")
                print("You don't know the PIN!")
                print("Search the reception desk first.")

            else:

                print("\nYou enter the dark evidence room.")
                print("Suddenly, a zombie appears!")
                print('Boy: "OH NO! ANOTHER ZOMBIE!"')

                print("\nWhat will you do?")
                print("1. Hide and wait for the zombie to leave")
                print("2. Rush past the zombie")

                action = input("Enter your choice (1/2): ")

                if action == "1":

                    print("\nYou quietly hide behind a cabinet.")
                    print("The zombie slowly moves away.")
                    print("You safely reach the evidence locker!")

                elif action == "2":

                    health -= 15

                    print("\nYou rush past the zombie!")
                    print("You lose 15 health.")
                    print("Remaining Health:", health)

                else:
                    print("\nInvalid action!")
                    continue

                if health <= 0:
                    print("\nThe zombie caught you!")
                    break

                print("\nYou find a locked evidence locker.")

                entered_pin = input("Enter the 4-digit locker PIN: ")

                if entered_pin == "2468":

                    print("\nCorrect PIN!")
                    print("The locker opens!")
                    print("You found the laboratory keycard!")

                    keycard = True

                else:

                    print("\nWrong PIN!")
                    print("An alarm suddenly starts ringing!")
                    print("You escape the zombie but lose 10 health.")

                    health -= 10
                    print("Remaining Health:", health)

        elif choice == "3":

            print("\nYou are returning to the Safe House.")
            break

        elif choice == "4":

            print("\n========== PLAYER STATUS ==========")
            print("Health:", health)
            print("Flashlight:", "Collected" if flashlight else "Missing")
            print("Keycard:", "Collected" if keycard else "Missing")
            print("Secret Note:", "Found" if police_note_found else "Missing")

        else:
            print("\nInvalid choice! Please enter 1 to 4.")
            

# ==========================================
# SCENE 8 - THE SECRET LABORATORY
# ==========================================

def secret_laboratory():

    global health, game_won

    print("\n========== SCENE 8: THE SECRET LABORATORY ==========\n")

    print("The boy reaches a mysterious building.")
    print('Boy: "This must be the secret laboratory!"')

    print("A large metal door blocks the entrance.")

    print('Computer: "ACCESS DENIED! SECURITY CLEARANCE REQUIRED!"')

    if not (flashlight and keycard):

        print("\nYou cannot enter the laboratory!")

        if not flashlight:
            print("Flashlight is missing!")

        if not keycard:
            print("Keycard is missing!")

        return

    print("\nThe boy places his keycard on the scanner.")

    print('Computer: "KEYCARD ACCEPTED!"')

    print("The laboratory door slowly opens.")

    print('Boy: "Wow! I actually made it!"')

    print("The laboratory is completely dark.")

    print("The boy switches on his flashlight.")

    print("Suddenly, he discovers another locked security door.")

    print('Computer: "ENTER THE FOUR-DIGIT SECURITY CODE."')

    print('Boy: "Wait! The note from the police station!"')

    while health > 0 and not game_won:

        print("\n========== LABORATORY MENU ==========")
        print("1. Enter Security Code")
        print("2. Return to Safe House")

        choice = input("\nEnter your choice (1/2): ")

        if choice == "1":

            entered_code = input("\nEnter the 4-digit code: ")

            if entered_code == "4321":

                print("\nACCESS GRANTED!")
                print("The security door slowly opens!")

                print("\nInside the room, you discover a glowing chest.")

                print('Boy: "Is this the treasure?"')

                print("You open the chest.")

                print("Inside, you discover the hidden treasure and a cure!")

                print("\nSuddenly, the radio turns on.")

                print('Radio: "Congratulations! You found the cure!"')

                print('Boy: "I survived! I actually survived!"')

                print("\n====================================")
                print("        CONGRATULATIONS!")
                print("           YOU WIN!")
                print("====================================")

                print("Treasure: Collected")
                print("Cure: Collected")
                print("Remaining Health:", health)

                game_won = True
                break

            else:

                print("\nINCORRECT SECURITY CODE!")
                print("WARNING! SECURITY ALARM ACTIVATED!")

                print("Zombies are approaching the laboratory!")

                health -= 15

                print("You lose 15 health!")
                print("Remaining Health:", max(0, health))

                if health <= 0:
                    print("\nThe zombies have caught you!")
                    print("GAME OVER!")
                    break

        elif choice == "2":

            print("\nYou return to the Safe House.")
            break

        else:

            print("\nInvalid choice! Please enter 1 or 2.")

        

# ======================================
# SCENE 5 - THE SAFE HOUSE
# ======================================

next_scene = None

if health > 0:

    print("\n========== SCENE 5: THE SAFE HOUSE ==========\n")

    print("The boy escapes through the broken window.")
    print("He lands on an empty street.")

    print('Boy: "Finally! I escaped!"')

    print("He looks around. The city is completely abandoned.")

    print('Boy: "Where is everyone?"')

    print("He finds a small house and enters it.")

    print("Inside the house, he discovers a map.")

    print('Boy: "A map! This might help me!"')

    while health > 0:

        print("\n========== CITY MAP ==========")
        print("1. Explore Supermarket")
        print("2. Explore Police Station")
        print("3. Enter Secret Laboratory")
        print("4. Check Player Status")
        print("5. Quit Game")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            supermarket()
            continue

        elif choice == "2":
            police_station()
            continue


        elif choice == "3":
            if flashlight and keycard:
                print("\nYou are heading to the Secret Laboratory!")
                secret_laboratory()
                if game_won:
                    break
                continue

            else:
                print("\nThe laboratory is locked!")
                if not flashlight:
                    print("You need to find a flashlight!")
                
                if not keycard:
                    print("You need to find a keycard!")

        elif choice == "4":

            print("\n========== PLAYER STATUS ==========")
            print("Health:", health)

            if flashlight:
                print("Flashlight: Collected")
            else:
                print("Flashlight: Not Collected")

            if keycard:
                print("Keycard: Collected")
            else:
                print("Keycard: Not Collected")

        elif choice == "5":
            print("\nYou decided to quit the game.")
            next_scene = "quit"
            break

        else:
            print("\nInvalid choice! Please enter 1 to 5.")

    if next_scene == "supermarket":
        print("\nNext: Scene 6 - The Supermarket")

    elif next_scene == "police_station":
        print("\nNext: Scene 7 - The Police Station")

    elif next_scene == "laboratory":
        print("\nNext: Scene 8 - The Secret Laboratory")

