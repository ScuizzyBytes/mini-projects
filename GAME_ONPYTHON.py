import time

coins = 0
M1 = 1
m1_price = 1
has_effect = False

count = 1

print(f"Skoko u teba monet: ", coins)
action = input("Нажми Enter чтобы начать игру: ")

while True:

    action = input(f"\rMonet: {coins} | M1 = {M1} | CHMI BISTREE: ")


    if action == "":
        coins += M1
        print(f"+{M1} monet!")
        count += 1

    elif action == "buy":
        if has_effect:
            print(f"\nti uche prokachen povtorno nelsa")
        elif count >= 10:
            coins -= m1_price
            M1 += 2
            m1_price *= 2
            has_effect = True
            print("M1 prokachen")
        else:
            print("Ti rblan tebe ne hvataet")

    elif action == "BuyX2":
         if coins >= 200:
            has_effect = False
            coins -= m1_price
            M1 += 10
            print("M1 prokachen X2")

    else:
        print("Ti rblan tebe ne hvataet")


