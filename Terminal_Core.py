import time
import keyboard as keyb

isBuyed = False

class Player:
    def __init__(self, maxhp, damage, hp, name, money):
        self.maxhp = maxhp
        self.damage = damage
        self.hp = hp
        self.name = name
        self.Money = money

    def attack_boss(self, target_boss):
        while True:
            event = keyb.read_event(suppress=True)
            if event.event_type == keyb.KEY_DOWN and event.name.lower() == 'f':
                target_boss.hp -= self.damage
                print(f"💥 Ты нанес урон боссу! Осталось HP: {max(0, target_boss.hp)}")
                break

class Enties:
    def __init__(self, hp, maxhp, speed, damage, name):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.maxhp = maxhp
        self.name = name

    def attack(self, player):
        time.sleep(0.5)
        player.hp -= self.damage
        print(f"⚔️ Босс нанес урон! Твое HP: {max(0, player.hp)}")

    def spawn_boss(self):
        print("Boss Just Spawned!")

MainPlayer = Player(100, 10, 100, "Misha", 100)
boss = Enties(200, 200, 20, 20, "Boss")

print("Hi What you want to do?")
time.sleep(1)
question = input("Spawn Boss ?: ").strip().lower()

if question == "no":
    question1 = input("Buy new Sword?: ").strip().lower()
    if question1 == "yes":
        if isBuyed:
            print("You bought this sword already!")
        elif MainPlayer.Money >= 20:
            MainPlayer.damage += 10
            MainPlayer.Money -= 20
            isBuyed = True
            print("you bought this sword!")
        else:
            print("Not enough money!")

elif question == "yes":
    boss.spawn_boss()

    while MainPlayer.hp > 0 and boss.hp > 0:
        MainPlayer.attack_boss(boss)

        if boss.hp <= 0:
            print("\n🎉 ПОБЕДА! Босс повержен!")
            break

        boss.attack(MainPlayer)

        if MainPlayer.hp <= 0:
            print("\n💀 You just Died...")
            break