from abc import ABC, abstractmethod

class FibonacciStartegy(ABC):
    @abstractmethod
    def caculate(self,n : int) -> int:
        pass

class RecursiveFibonacci(FibonacciStartegy):
    def caculate(self, n: int) -> int:
        if n <= 1:
            return n
        return self.caculate(n-1) + self.caculate(n-2) 

class SimpleFibonacci(FibonacciStartegy):
    def caculate(self, n: int) -> int:
        if n <= 1 :
            return n
        a = 0 
        b = 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class FibonacciCaculator:
    def __init__(self,strategy : FibonacciStartegy) -> None:
        self.strategy = strategy
    def caculate(self,n:int):
        return self.strategy.caculate(n)

def main():
    s = SimpleFibonacci()
    cac = FibonacciCaculator(s)
    print(cac.caculate(2))

main()
