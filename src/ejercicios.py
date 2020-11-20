from builtins import True
def factorial(number):
    if number == 0:
        number = 1
    elif number < 0:
        number = -1
    else:
        output = 1
        for cont in range(1, number + 1):
            output *= cont
        number = output
    return number

def leapYear(num):
    bicies = 1
    if num % 4 == 0:
        if num % 100 == 0:
            bicies = -1
        elif num % 400 == 0:
            bicies = 1
    else:
        bicies = -1
    return bicies

def daysInMonth(month, year):
    if (month < 1 or month > 12) or year < 0:
        output = -1
    else:
        if month == 2:
            bisiesto = leapYear(year)
            if bisiesto == 1:
                output = 29
            else:
                output = 28
        else:
            dia = {
                1: 31,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
                }
            output = dia.get(month)
    return output
def dayOfWeek(day, month, year):
    a = int((14 - month) / 12)
    y = year - a 
    m = month + 12 * a - 2 
    d = int((day + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12)) % 7)
    return d
def myPower(n, p):
    if p < 0:
        output = -1
    elif p == 0:
        output = 1
    else:
        output = 1
        for cont in range(p):
            output = output * n
    return output
def numberOfNumbers(n):
    if n < 0:
        output = -1
    else:
        output = 1
        while n > 9:
            n = n / 10
            output = output + 1
    return output
def isPrime(n):
    if n <= 0:
        output = -1
    else:
        output = 1
        for i in range(2, n):
            if n % i == 0:
                output = 0
    return output
def secondOrder(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        result = b*b-4*a*c
        if result > 0:
            output = 2
        elif result == 0:
            output = 1
        else:
            output = 0
    except:
        output = -1
    
    return output
def numberDivisorPrime(n):
    numdivi = 0
    for c in range(1, n + 1):
        if n % c == 0:
            if isPrime(c) == 1:
                numdivi += 1
    return numdivi
def friend(n, m):
    def isFriend(n, m):
        result = 0
        for c in range(1, n):
            if n % c == 0:
                result += c
            if result == m:
                friend = True
            else:
                friend = False
    if isFriend(n,m) == isFriend(m,n):
        friend = True
    else:
        friend = False
    return friend
