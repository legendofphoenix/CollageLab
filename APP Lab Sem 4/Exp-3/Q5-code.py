#Question 5
from abc import ABC, abstractmethod

class Startup(ABC):
    def Ideas (self):
        print("3 months later.....\n")
class Infra(Startup):
    def Ideas(self):
        super(). Ideas()
        print("1. INFRASTRUCTURE ON WORK AREA")
        print("->Communication networks")
        print("->Electric system")
        print("->cost\n")

class Fund (Startup): 
    def Ideas (Self):
        super(). Ideas()
        print ("2.CAPITAL AND FUNDING")
        print("->Equity") 
        print ("->Debt")
        print("->Profit\n")

class Resource (Startup):
    def Ideas (Self):
        super(). Ideas()
        print ("3.HUMAN RESOURCE")
        print("->Recruitment\n")
x=Infra()
x.Ideas()
y= Fund()
y.Ideas()
z=Resource()
z.Ideas()
