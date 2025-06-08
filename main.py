''' MODULES '''
from msys.characterDelayAnimation import characterDelayAnimation
from msys.lineDelayAnimation import lineDelayAnimation
from msys.displayFormat import displayFormat
from msys.clearScreen import clearScreen

''' IMPORTS '''
from datetime import datetime, date

class Person:
    def __init__(self, name: str, birthdate: date):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

    ''' METHODS '''
    def get_age(self) -> int:
        date_today = datetime.now()
        age = date_today.year - self.birthdate.year

        # check if birthday occured this year
        if (date_today.month, date_today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

class Patient(Person):
    def __init__(self, name: str, birthdate: date, gender: str = None, nationality: str = None, address:str = None, phone_number: str = None, email: str = None):
        super().__init__(name, birthdate)
        self.gender = gender
        self.nationality = nationality
        self.address = address
        self.phone_number = phone_number
        self.email = email

    ''' METHODS '''
    def display_information(self) -> None:
        lineDelayAnimation(f"{'':<4}[ PATIENT INFORMATION ]", 0.2)
        lineDelayAnimation(f"{'Name: ':>14}{self.name}", 0.2)
        lineDelayAnimation(f"{'Age: ':>14}{self.get_age()}", 0.2)
        lineDelayAnimation(f"{'Gender: ':>14}{self.gender}", 0.2)
        lineDelayAnimation(f"{'Birthday: ':>14}{self.birthdate}", 0.2)
        lineDelayAnimation(f"{'Nationality: ':>14}{self.nationality}", 0.2)
        lineDelayAnimation(f"{'Address: ':>14}{self.address}", 0.2)
        lineDelayAnimation(f"{'Contact No.: ':>14}{self.phone_number}", 0.2)
        lineDelayAnimation(f"{'Email: ':>14}{self.email}", 0.2)
        

person: Patient = Patient("Adrian Dominic L. Tan", "2005-07-29", 'M', "Filipino", "Iloilo City, Iloilo", "09382277245", "adriandominic.tan@wvsu.edu.ph")
person.display_information()