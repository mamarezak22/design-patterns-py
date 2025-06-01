from abc import ABC,abstractmethod


class Stock:
    def __init__(self,
                name,
                price) -> None:
        self.name = name
        self.old_price = 0 
        self.current_price = price
        self.observers = []

    def attach(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self,observer):
        try : 
            self.observers.remove(observer)
        except Exception:
            raise ValueError("that is not a observer")

    def notify(self): 
        for observer in self.observers:
            observer.observe(self)

    def change_price(self,price):
        if price != self.current_price:
            self.old_price = self.current_price
            self.current_price = price
            self.notify()
        

class Observer:
    def observe(self,stock):
        print(f"{stock.name} was {stock.old_price} but now is {stock.current_price}")


def main():
    s1 = Stock("LG",10000)
    o1 = Observer()
    s1.attach(o1)
    s1.change_price(9000)
main()  


