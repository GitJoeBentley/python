# CIS22b - Assignment 8

from random import randint
from datetime import date
from datetime import timedelta

date_today = date.today()

names = ("Fadak","Adis","Kia","Adam","Ran","Jason","Brian","Hin Hang",
    "Swati","Alaxendar","Robert","Samar","Thi Thu Vy","Salomon","Marian","Nicolas",
    "Brian Ha","Wanjia","Dolly","Trien Bang","Suraj","Bereket","Ben",
    "Victor","Xinru","Zheng","Ken","Jason Kai","Ryan","Seyedamirhossei","Arrzu",
    "Nimra","Brian Ndiaye","Le Ngoc","Pham Bao Bao","Xuan Yen Tram","Kuangzhong","Joseph",
    "Het","Isha","Ahmad","Mehui","Tarandeep","Minrou","Lauren","Trang","Victoria",
    "An","Vinh","William","Benjamin","Hsin-Chieh","Jiasheng","Siyun")

def get_birthday() -> date:
    """ Returns a random birthdate in the last 100 years """
    number_of_day_in_100_years = 36525      # 365.25 * 100
    one_hundred_years_ago = date(date_today.year-100, date_today.month, date_today.day)
    random_birthday = one_hundred_years_ago + timedelta(days=randint(1, number_of_day_in_100_years))
    return random_birthday
    

class Human:
    def __init__(self, name: str):
        self._name = name
        self._birthday = get_birthday()
        self._is_alive = True
        
    def __repr__(self) -> str:
        ret = self._name + " was born on " + self._birthday.strftime("%m/%d/%Y") + " is " + str(self.age())
        return ret
    
    def age(self) -> int:
        return int((date_today - self._birthday).days/365.25)

class Population:
    def __init__(self):
        self._people = []
        self._original_population_size = len(names)
        self._people = [Human(name) for name in names]
        
    def print(self):
        print('================================================')
        print("Today is",date_today.strftime("%m/%d/%Y"))
        for human in self._people:
            if human._is_alive:
                print(human)
        print('================================================')
        
    def examine_population(self):
        for i in range(len(self._people)):
            if self._people[i]._is_alive and roll_the_dice(self._people[i].age()) > 0.67:
                self._people[i]._is_alive = False
                print(date_today.strftime("%m/%d/%Y ") + self._people[i]._name +
                      " died at the age of " + str(self._people[i].age()))
                
    def get_number_living(self) -> int:
        num = 0
        for person in self._people:
            if person._is_alive:
                num += 1
        return num
                

def let_time_pass():
    global date_today
    date_today = date_today + timedelta(days=randint(1,365))
    
def roll_the_dice(age: int) -> float:
    return age * (randint(0,100) / 10000.0)
    
    
if __name__ == '__main__':
    world = Population()
    world.print()
    while world.get_number_living() > world._original_population_size / 2:
        let_time_pass();
        world.examine_population();
    world.print()
