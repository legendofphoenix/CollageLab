#Question 2
class string():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str=input("Enter string : ")
    def print_string(self):
        print(self.str.upper())
        print(self.str.lower())
str=string()
str.get_string()
str.print_string()
