def std(n):
    while n != 2:
        if n % 2 != 0:
            return "No"
        n = n / 2
    return "Yes"
 
 
def prime(number):
    m = []
    for i in range(1, number + 1):
        if number % i == 0:
            m.append(i)
    if len(m) == 2:
        return "Простое число"
    return "Составное число"
 
 
def palindrome(s):
    s = s.replace(" ", "")
    if s.lower() == s[::-1].lower():
        return "Палиндром"
    return "Не палиндром"
 
 
def check_pin(pinCode):
    a = [int(i) for i in pinCode.split("-")]
    if prime(a[0]) == "Простое число":
        if palindrome(str(a[1])) == "Палиндром":
            if std(a[2]) == "Yes":
                return "Корректен"
            else:
                return "Некорректен"
        else:
            return "Некорректен"
    else:
        return "Некорректен"
