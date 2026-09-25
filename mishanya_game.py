
count = 0

class Hero:
    Hp = 20
    Name = None
    power = 10

    def __init__(self, Name, Hp, Power):
        self.Name = Name
        self.Hp = Hp
        self.Power = Power

    def __str__(self):
        return f"Hero: {self.Name} (Hp: {self.Hp}, Power: {self.Power})"

    pass

class Weapon:
    Patrons = 10
    state = None

    def __init__(self, Patrons, state, count):
        self.Patrons = Patrons
        self.state = state
        self.count = 0

    def check_state(self):
        if self.count == 10:
            print("your Pistol State is Change!")
            self.state = "Dirty"

    def fire(self):
        if self.Patrons <= 0:
            print("No ammo!")
            return


        tip = input("Nashmi F chto bi strelat: ")
        if tip.lower() == "f":
            self.Patrons -= 1
            self.count += 1
            print(f"ti vistrilel u teba {self.Patrons}")
            self.check_state()

    def __str__(self):
        return f"🔫 Оружие [Патроны: {self.Patrons} | Состояние: {self.state}]"

    pass


Pistol = Weapon(Patrons=10, state="norm", count=1)

tip = input("")

if tip.lower() == "ok":
    while True:
        print(Pistol)
        Pistol.fire()
        if Pistol.Patrons <= 0:
            Pistol.fire()
            print("No ammo!")
            break

misha1 = Hero("Hero", 20, 10)
print(misha1)

misha = Hero("misha", 5, 5)
print(misha)







