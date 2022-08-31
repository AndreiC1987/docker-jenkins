import random
import time

import schedule
import datetime
# from bs4 import BeautifulSoup


class Elf:
    def __init__(self, name, dodge, life=200, attack=100, defense=50):
        self.attack = attack
        self.defense = defense
        self.life = life
        self.dodge = dodge
        self.name = name

    def get_name(self):
        return self.name

    def charge(self, attack, *args):
        self.attack = attack
        attack = random.randint(10, 500)
        print("Dealing", attack, "to", args.__str__())

    def dodge_succes(self, dodge, defense, *args):
        self.dodge = dodge + defense
        dodge = random.randint(1, 10)
        print("dodging", dodge, "from", args.__str__())
        if dodge <= self.dodge:
            return True
        return False


class Dwarf:
    def __init__(self, name, block, charge_chance, life=400, attack=50, defense=200):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.block = block
        self.charge_chance = charge_chance
        self.name = name

    def get_name(self):
        return self.name

    def charge(self, charge_chance, attack, *args):
        self.charge_chance = charge_chance + attack
        attack = random.randint(20, 80)
        print("Dealing", charge_chance + attack, "to", args.__str__())

    def blocking(self, block, defense, *args):
        self.block = block + defense
        print("Blocking", block, "to", args.__str__())
        block = random.randint(1, 10)
        if block <= 10:
            return True
        return False


class Witch:
    def __init__(self, name, spell_damage, weaken, life=150, attack=150, defense=200):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.spell_damage = spell_damage
        self.weaken = weaken
        self.name = name

    def get_name(self):
        return self.name

    def damage(self, spell_damage, weaken, *args):
        self.spell_damage = spell_damage + weaken
        spell_damage = random.randint(1, 15)
        print("Dealing", spell_damage + weaken, "to", args.__str__())
        if spell_damage <= 5:
            return True
        return False


def start():
    with open('fisier.xml') as text:
        return text.readlines()[0]
    # with open("fisier.xml", 'r') as f:
    #     data = f.read()
    # bs = BeautifulSoup(data, 'xml')
    # bchild = bs.find_all('child')
    # return bchild


def final():
    with open('fisier.xml') as text:
        return text.readlines()[1]


def raid():
    print("----------------------------------------")
    Gigi.charge(100, Timmy.get_name())
    Timmy.charge(2, 100, Galadriel.get_name())
    Galadriel.damage(20, 5, Gigi.get_name())
    time.sleep(10)
    Timmy.charge(Gigi.get_name(), 120)
    Galadriel.damage(Timmy.get_name(), 80)
    Gigi.charge(Galadriel.get_name(), 210)
    time.sleep(10)
    Gigi.dodge_succes(Galadriel.damage(100, 50), 10)
    print("----------------------------------------")


if __name__ == "__main__":

    Gigi = Elf("Gigi", 150, 2)
    Timmy = Dwarf("Timmy", 100, 3)
    Galadriel = Witch("Galadriel", 50, 4)

    now = datetime.datetime.now()
    data1 = now.hour, ":", now.minute, ":", now.second
    data2 = str(data1[0])+data1[1]+str(data1[2])+data1[3]+str(data1[4])
    # Gigi.charge(100, Timmy.getName())
    schedule.every(10).seconds.do(raid())
    i = 1
    while i < 4:
        schedule.run_pending()
        schedule.run_pending()
        schedule.run_pending()
        break
    i += 1
