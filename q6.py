class Math:
    def calculate(self,num1,num2):
        pass

class Adder(Math):
    def calculate(self,num1,num2):
        return num1+num2

class Multiplier(Math):
    def calculate(self,num1,num2):
        return num1*num2

class Divider(Math):
    def calculate(self,num1,num2):
        return num1/num2

class Subtracter(Math):
    def calculate(self,num1,num2):
        return num1-num2

def calculator(math,a,b):
    return math.calculate(a,b)

def main():
    add = Adder()
    result = calculator(add,5,5)
    print(result)

if __name__=="__main__":
    main()



