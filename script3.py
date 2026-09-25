import random as rnd
import time
import pygame

pygame.init()

player = {
    'dollars': 20,
    'hp': 100,
    'speed': 10
}

efects = {
    'rare': 'sinii',
    'legendary': 'solotoi',
    'EBEICHII!!!!': 'rainbow'
}


meshi = {
    'Topor': 60,
    'mesh': 30,
    'LUK': 10
}

items = list(meshi.keys())
weights = list(meshi.values())

random_rare = list(efects.keys())
random_color = list(efects.values())

vopros1 = input(f'privet kak teba sovut: ')

if vopros1 == 'misha':
    print("OOOOO nihuyaaaa misha ya teba Snau idi sa mnoi")

    time.sleep(2)

    vopros2 = input("smotri u teba est vibor chto ti hochech (prokrut) ili (sa 20 baksow kupit tapor?): ")
    if vopros2 == '(prokrut)' or vopros2 == 'prokrut':

        print("prokrut stoit 100 baksow a u teba 20 tolko")
    elif vopros2 == 'topor' or vopros2 == 'kupit topor sa 20 dollars':
        if player['dollars'] >= 20:
            print(f"nice teper u teba Topor")
            player['dollars'] -= 20
        else:
           print("u teba net deneg")


    else:
       prokrut = rnd.choices(items, weights=weights, k=1)[0]
       if prokrut == ['LUK']:
            print(f'Ebat tebe vipal | {prokrut} a redkost | {rnd.choice(random_rare)}' )
       else:
         print(f"tebe vipal {prokrut} ebat ti lox")

choise = ['les', 'gorod', 'k drugu']

print('kuda Ti poidesh?: ' + str(choise))
answer2 = input()

if answer2 == choise[1]:
    print("okei bud ostorochen sdes ludi oni pomug visvat poliziiu!")

while True:
    screen = pygame.display.set_mode((800, 600))












