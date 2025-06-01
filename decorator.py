class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

class SugarDecorator:
    def __init__(self,coffee) -> None:
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 1 

def main():
   c = Coffee() 
   c_with_s = SugarDecorator(c)
   c_with_s_with_m = MilkDecorator(c_with_s)
   print(c_with_s_with_m.cost())

main()
