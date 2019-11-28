
class Animal:
  def is_mammal(self):
    return None
  
  def set_age(self, age):
    self.age = age
  
  def tell_age(self):
    print('Age is ', self.age)

  

class Duck(Animal):
  def quack(self):
    print('quack', self.age)

  def is_mammal(self):
    return False

class Fish(Animal):
  def is_mammal(self):
    return False
  
  def swim(self):
    print('swimming...')


class Zebra(Animal):
  def is_wild(self, wild):
    self.wild = wild
  
  def is_mammal(self):
    return True



my_duck = Duck()
my_duck.set_age(99)
my_duck.quack()
unknow_var = my_duck

my_duck2 = Duck()
my_duck2.set_age(77)
my_duck2.quack()

my_fish = Fish()
my_fish.swim()
my_fish.set_age(1)
my_fish.tell_age()

my_zebra = Zebra()
my_zebra.is_wild(True)
print('Is wild?', my_zebra.wild)

animals = [my_duck, my_duck2, my_fish, my_zebra]

mammals = [it for it in animals if it.is_mammal()]
no_mammals = [it for it in animals if not it.is_mammal()]

print(type(my_duck))

if type(unknow_var) is Duck:
  print("it's a Duck")

print([type(animal).__name__ for animal in mammals])
print([type(animal).__name__ for animal in no_mammals])


