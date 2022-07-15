class calculator:
    def __init__(self,a=0,b=20) -> None:
        self.a = a
        self.b = b

    def addition(self) -> int:
        return self.a+self.b

    def subtraction(self) -> float:
        return self.a-self.b

    def multiplication(self) -> float:
        return self.a*self.b    

cal = calculator(a=3,b=4)
print(cal.addition())             
        