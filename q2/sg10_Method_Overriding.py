class Animal:
  def __init__(self,name):
    self.name = name

  def feed(self):
    return f"{self.name} eats"
  
  def make_sound(self):
    return f"{self.name} makes sound"
  
class Lion(Animal):
  def __init__(self, name):
    self.name = name
    
  def feed(self):
    return f"{self.name} eats fresh meat"
  
  def make_sound(self):
    return f"{self.name} roars loudly!"

class Elephant(Animal):
  def __init__(self, name):
    self.name = name
    
  def feed(self):
    return f"{self.name} eats grass and fruits"
  
  def make_sound(self):
    return f"{self.name} trumpets!"
 
class Monkey(Animal):
  def __init__(self, name):
    self.name = name
    
  def feed(self):
    return f"{self.name} eats bananas"
  
  def make_sound(self):
    return f"{self.name} chatters"


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")

print(elephant.make_sound())
print(elephant.feed())
print("-----")

print(monkey.make_sound())
print(monkey.feed())
print("-----")
