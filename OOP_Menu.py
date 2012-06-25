class MenuItem:
    def __init__(self):
        self.name=""
        self.price=0
    def Show (self):
        print("%s       %i" %(self.name,self.price))
              
Spag= MenuItem()
Spag.name="Spaghetti"
Spag.price=95

print(Spag.name)
print(Spag.price)


Coke=MenuItem()
Coke.name="Coke Float"
Coke.price=25

print(Spag.name)
print(Spag.price)
print(Coke.name)
print(Coke.price)

Spag.Show()
Coke.Show()
