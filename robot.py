from colorama import init
from colorama import Fore, Back, Style

init()

class Robot:

    population = 0

    def __init__(self,name):
        self.name = name
        print('(Иницифлизация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def sayHi(self):
        print('Hello! My houseband named me {0}.'.format(self.name))

    def howMany():
        print('У нас {0:d} работающих роботов.'.format(Robot.population))

droid1 = Robot('R2-D2')
print(Back.LIGHTWHITE_EX)
print(Fore.LIGHTCYAN_EX)

droid1.sayHi()
print(Back.LIGHTYELLOW_EX)
Robot.howMany()
print(Back.LIGHTMAGENTA_EX)
print(Fore.GREEN)
droid2 = Robot('C-3PO')
print(Back.CYAN)
print(Fore.LIGHTWHITE_EX)
droid2.sayHi()
print(Back.LIGHTRED_EX)
Robot.howMany()
print(Back.LIGHTWHITE_EX)
print(Fore.LIGHTBLUE_EX)
print('Here robot may does job.\n')
print('Работой роботов будут вычисления - возведение в квадрат и в куб\n')
print('Введите,пожалуста,2 числа(целых или с плавающей точкой)')
a = float(input())
b = float(input())
c = a**2
print(c)
d = b**3
print(d)
print('Robot complete the job and deleted\n')
del droid1
del droid2

Robot.howMany()


