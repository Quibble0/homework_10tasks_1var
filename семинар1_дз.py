# VARIANT 1
#  №1 matrica

def spiral(*args):
    n,m = args[0],args[1]
    matr = [[0]*m for _ in range(n)]
    r, b = m-1, n-1
    l, t = 0,0
    count = 1

    while l <= r and t <= b:
        for i in range(l,r+1):
            matr[t][i] = count
            count += 1
        t += 1

        for i in range(t, b + 1):
            matr[i][r] = count
            count += 1
        r -= 1

        for i in range(r,l-1,-1):
            matr[b][i] = count
            count += 1
        b -= 1

        for i in range(b,t-1,-1):
            matr[i][l] = count
            count += 1
        l += 1

    return mat(matr)

def mat(matr):
    for x in matr:
        print(*x)

spiral(4,2)

 #2 stroka

def stroka():
    max_count_unik = 0
    max_str = ''

    s = input()

    while s != 'STOP':
        sp_unik = []

        for i in s.lower():
            if i not in sp_unik:
                sp_unik.append(i)

        if len(sp_unik) > max_count_unik:
            max_count_unik = len(sp_unik)
            max_str = s

        s = input()

    return [max_str, max_count_unik]


result = stroka()
print(result[0])
print(result[1])


#3 posledovatelnost

def posl(sp: list):
    if len(sp) == 0:
        return []

    res = []
    count = 1
    for i in range(len(sp) - 1):
        if sp[i] == sp[i + 1]:
            count += 1
        else:
            res.append((sp[i],count))
            count = 1

    res.append((sp[-1],count))
    return res

sp = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3]
print(posl(sp))


#№4 bliz tochka
n = int(input("Количество точек: "))

def rast(x,y,x0,y0):
    return (x-x0)**2 + (y-y0)**2

points = []
for i in range(n):
    x,y = map(int,input().split())
    points.append([x,y])
x0,y0 = map(int,input('Контрольная точка: ').split())

def bliz(points,x0,y0):
    minr = 10*10
    for i in range(len(points)):
        x,y = points[i][0], points[i][1]
        if rast(x,y,x0,y0) < minr:
            minr = rast(x,y,x0,y0)
            resx,resy = x,y
    return [(minr)**0.5,resx,resy]

res1,res2,res3 = bliz(points,x0,y0)
print(f'точка: ({res2},{res3}), расстояние: {res1}')


 #№5 srednee
def sred(sp, k):
    if k <= 0 or k > len(sp):
        return []

    res = []

    for i in range(len(sp) - k + 1):
        okno = sp[i:i + k]
        srednee = sum(okno) / k
        res.append(int(srednee))

    return res
sp = [2, 4, 6, 8, 10]
k = 3

print(sred(sp, k))

 #№6
import random
from faker import Faker

def create_file(file, n):
    fake = Faker("ru_RU")

    with open(file, "w", encoding="utf-8") as f:
        for i in range(n):
            name = fake.name()
            ball = random.randint(0, 100)
            f.write(f"{name};{ball}\n")


def statistika(file):
    summa = 0
    count = 0
    count60 = 0
    max_ball = None
    min_ball = None
    best_name = ""

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")

            if len(parts) != 2:
                continue

            name = parts[0].strip()

            try:
                ball = int(parts[1])
            except ValueError:
                continue

            if name == "" or ball < 0 or ball > 100:
                continue

            summa += ball
            count += 1

            if ball >= 60:
                count60 += 1

            if max_ball is None or ball > max_ball:
                max_ball = ball
                best_name = name

            if min_ball is None or ball < min_ball:
                min_ball = ball

    if count == 0:
        print("Нет корректных записей")
        return

    print("Средний балл:", summa / count)
    print("Максимальный балл:", max_ball)
    print("Минимальный балл:", min_ball)
    print("Набрали не менее 60:", count60)
    print("Лучший студент:", best_name)


create_file("students.txt", 1000)
statistika("students.txt")


 #№7 slova

def cnt_word(file):
    words = {}
    with open(file) as f:
        for line in f:
            line = line.lower()
            for symbol in ".,!?:;":
                line = line.replace(symbol, '')

        for el in line.split():
            if el in words:
                words[el] += 1
            else:
                words[el] = 1

    top_10 = sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top_10:
        print(f'{word}: {count}')

    return words


# №8

import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print("Время выполнения:", end - start)

        return result

    return wrapper


@measure_time
def numbers():
    s = 0
    for i in range(100000):
        s += i
    return s


@measure_time
def squares(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
    return res


@measure_time
def hello(name):
    print("Привет,", name)


print(numbers())
print(squares(5))
hello("Мир")


#9

class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        self.owner = owner
        self.__balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Неверная сумма")
            return

        self.__balance += amount
        self.history.append(f"Пополнение: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Неверная сумма")
            return

        if amount > self.__balance:
            print("Недостаточно денег")
            return

        self.__balance -= amount
        self.history.append(f"Снятие: {amount}")

    def get_balance(self):
        return self.__balance

    def get_history(self):
        return self.history.copy()


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            print("Неверная сумма")
            return

        if self.get_balance() - amount < 1000:
            print("На счете должно остаться 1000")
            return

        super().withdraw(amount)


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, limit=5000):
        super().__init__(owner, balance)
        self.limit = limit
        self.__debt = 0

    def withdraw(self, amount):
        if amount <= 0:
            print("Неверная сумма")
            return

        balance = self.get_balance()

        if amount <= balance:
            super().withdraw(amount)
            return

        need = amount - balance

        if self.__debt + need > self.limit:
            print("Превышен кредитный лимит")
            return

        if balance > 0:
            super().withdraw(balance)

        self.__debt += need
        self.history.append(f"Использован кредит: {need}")

    def deposit(self, amount):
        if amount <= 0:
            print("Неверная сумма")
            return

        payment = min(amount, self.__debt)
        self.__debt -= payment

        if payment > 0:
            self.history.append(f"Погашение долга: {payment}")

        if amount > payment:
            super().deposit(amount - payment)

    def get_debt(self):
        return self.__debt


accounts = [
    BankAccount("Иван", 3000),
    SavingsAccount("Петр", 3000),
    CreditAccount("Анна", 3000)
]

for account in accounts:
    print("\nВладелец:", account.owner)
    account.withdraw(3500)
    print("Баланс:", account.get_balance())
    print("История:", account.get_history())



#10

from functools import wraps

def log_command(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Выполняется команда")
        return func(*args, **kwargs)
    return wrapper


class Command:
    def execute(self, a, b):
        raise NotImplementedError


class Add(Command):
    @log_command
    def execute(self, a, b):
        return a + b


class Multiply(Command):
    @log_command
    def execute(self, a, b):
        return a * b


class Subtract(Command):
    @log_command
    def execute(self, a, b):
        return a - b


class Divide(Command):
    @log_command
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b


class CommandProcessor:
    def __init__(self):
        self.number = 0
        self.history = []

        self.commands = {
            "add": Add(),
            "multiply": Multiply(),
            "subtract": Subtract(),
            "divide": Divide()
        }

    def run(self, text):
        parts = text.split()

        if len(parts) == 0:
            print("Пустая команда")
            return

        command = parts[0].lower()

        if command == "history":
            if len(parts) != 1:
                print("Команда history не принимает аргументы")
                return

            for el in self.history:
                print(el)
            return

        if command not in self.commands:
            print("Неизвестная команда")
            return

        if len(parts) != 2:
            print("Нужно ввести команду и число")
            return

        try:
            value = float(parts[1])
        except ValueError:
            print("Неверное число")
            return

        try:
            result = self.commands[command].execute(self.number, value)
        except ValueError as e:
            print("Ошибка:", e)
            return

        self.number = result
        self.history.append(f"{command} {value} = {result}")
        print("Результат:", self.number)


processor = CommandProcessor()

while True:
    text = input("Введите команду: ").strip()

    if text.lower() == "exit":
        break

    processor.run(text)





