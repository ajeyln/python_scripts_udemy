import random
class Enemy:
    def __init__(self, name="Enemy", hit_point=0, lives=0):
        self.name = name
        self.hit_point = hit_point
        self.lives = lives
        self.alive = True
    
    def take_damage(self, damage):
        remaining_points = self.hit_point - damage
        if remaining_points >= 0:
            self.hit_point = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_point))
        else:
            self.lives -= 1
            if self.alive > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Point : {0.hit_point}" .format(self)

# Troll took inheritance from class Enemy
class Troll(Enemy):

    def __init__(Self,name):
        # super(Troll,self).__init__(name=name, lives=1, hit_point=23)
        super().__init__(name=name, lives=1, hit_point=23)
    
    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


# Troll took inheritance from class Enemy
class Vampyre(Enemy):
    def __init__(self,name):
        super().__init__(name=name, lives=3, hit_point=12)
    
    def dodges(self):
        if random.randint(1, 3) == 3:
            print("****** {0.name} dodges *****".format(self))
            return True
        else:
            return False
# Vampyreking took inherited from class Vampyre
class VampyreKing(Vampyre):
    def __init__(self,name):
        super().__init__(name)
        self.hit_point = 140
    
    def take_damage(self, damage):
        super().take_damage(damage // 4)



if __name__ == "__main__":
    random_monster = Enemy("Basic Enemy", 12 , 1)
    print(random_monster)

    random_monster.take_damage(5)
    print(random_monster)  

    random_monster.take_damage(9)
    print(random_monster)    

    random_monster.take_damage(15)
    print(random_monster)

# inheritace
    ugly_troll = Troll("Pug")
    print("Ugly troll - {}".format(ugly_troll))

    another_troll = Troll("ug")
    print("Another troll - {}".format(another_troll))

    brother = Troll("urg")
    print(brother)

    ugly_troll.grunt()
    another_troll.grunt()
    brother.grunt()

print("*" * 75)
vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)
print("*" * 75)

# Sub-class
dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)