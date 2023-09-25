class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

# создание обьекта
my_cl = Calculator()

while True:

    print("1: Сложить")
    print("2: Вычесть")
    print("3: Перемножить")
    print("4: Разделить")
    print("5: Завершить и выйти")
    
    ch = int(input("Выберите операцию: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(ch == 5):
            break
        
        #If not then ask fo the input and call appropiate methods        
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cl.divide(a, b))
    
    else:
        print("Некорректный ввод")
