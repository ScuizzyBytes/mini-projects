import json
import time
import sys

pip = ["Get away from me!", "Dont touch me!", "Who are you?"]

Inventory = []

count = 0

player = {
    "name": "Misha",
    "Hp": 20,
    "speed": 10
}

firewood_damager = ("Axe")

Wood = {"FireWood": 10}

print("Hello Little feller!")
question = input("Are you remember what happend?: ")

if question.lower() == "no":
    print("Your Plane Just Falled...")
    time.sleep(1)
    print("And I saw you in bush you was very wounded...")
    time.sleep(1)
    print("I helped you to survive\n", )

else:
    print("alr", )

time.sleep(2)

question = input("Wanna come with me?:")
if question == "yes":
    print("We Need to go faster")
    time.sleep(1)
    print("We are in the Forest")
    time.sleep(0.5)
    print("Take Care of yourself!!!")
else:
    print("*You were hit - 10Hp*")
    time.sleep(1)
    print("*You were picked up*\n")
    time.sleep(2)
    print("*You Woke up in a Camp*\n")
    question1 = input("Hey, are you awake already?: ")
    if question1 in pip:
        print("Now you will be ours")
        time.sleep(1)
        print("Grab the axe and go chop us some firewood!!!")


        def Grab_axe():
            Inventory.append("Axe")


        Grab_axe()

    if "Axe" in Inventory:
        while True:
            Tipp = input("Nachmi F chto bi rubit: ")

            if Tipp.upper() == "F":
                Wood["FireWood"] += 1
                count += 1
                print(f"Срублено дров: {count}/5")

            if count >= 5:
                Tipp2 = input("to return the woods R: ")
                if Tipp2.upper() == "R":
                    print("Good now go fuck your self XD\n")
                    Tipp3 = print("Tipp: You Have Axe in your inventory")

                    answer3 = input("Ti che ahuel")

                    if answer3 == "Ti che ahuel?":
                        print("What?!?!?!!?")
                        answer4 = input("You: Ya govoru Ti che ahuel?")
                        print("COME HERE YOU SON OF A BITCH!!!")
                        time.sleep(1)
                        print("A fight breaks out!")
                        time.sleep(1)
                        print("Your Index: ", player)
                        answer4 = input("")
                        if answer4.lower() == "e":
                            print("Punch!!!")
                            time.sleep(1)
                            print("You: AHAHAHAHA ebat ti lox ya teba virubil odnim udarom")
                        elif answer4.lower() == "R":
                            print("Ti promachnulsa!")
                            player["Hp"] -= 5
                        else:
                            print("Game Over...")

                    break
print("*Ten Minute of walking had passed*")
time.sleep(1)
print("Well, here we are at the camp")
time.sleep(2)
print("You will be staying in that tent")

save_data = {
    "player": player,
    "Inventory": Inventory, }

with open("../data/Balance.JSON", "w", encoding="utf-8") as f:
    json.dump(save_data, f, ensure_ascii=False, indent=4)

print("\nGame Saved")
