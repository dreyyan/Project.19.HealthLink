''' MODULES '''
from msys.characterDelayAnimation import characterDelayAnimation
from msys.lineDelayAnimation import lineDelayAnimation
from msys.displayFormat import displayFormat
from msys.clearScreen import clearScreen
from msys.errorMessage import errorMessage
from msys.pressEnterToContinue import pressEnterToContinue

''' IMPORTS '''
from datetime import datetime, date
import time

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

    def admit_new_patient():
        print("admitting new patient...")

    def patient_list():
        print("displaying patient list...")

    def update_patient_record():
        print("updating patient record...")

    def discharge_patient():
        print("discharging patient...")

    @staticmethod
    def display_main_menu():
        while True:
            clearScreen()
            try:
                lineDelayAnimation("     [ HealthLink ]", 0.1)
                displayFormat('*', 25)
                lineDelayAnimation("[1] Admit New Patient", 0.1)
                lineDelayAnimation("[2] Patient List", 0.1)
                lineDelayAnimation("[3] Update Patient Record", 0.1)
                lineDelayAnimation("[4] Discharge Patient", 0.1)
                lineDelayAnimation("[5] Exit", 0.1)
                displayFormat('*', 25)

                # prompt user to enter choice
                user_choice = input("~ ").strip().lower()

                if user_choice in ["1", "admit"]:
                    Patient.admit_new_patient()
                elif user_choice in ["2", "list"]:
                    Patient.patient_list()
                elif user_choice in ["3", "update"]:
                    Patient.update_patient_record()
                elif user_choice in ["4", "discharge"]:
                    Patient.discharge_patient()
                elif user_choice in ["5", "exit"]:
                    print("# exiting system...")
                    time.sleep(2)
                    break
                else:
                    errorMessage("Invalid input, please enter a valid choice")
            
            except ValueError as e:
                print(f"ERROR: {e}")

            pressEnterToContinue()

person: Patient = Patient("Adrian Dominic L. Tan", "2005-07-29", 'M', "Filipino", "Iloilo City, Iloilo", "09382277245", "adriandominic.tan@wvsu.edu.ph")
person.display_main_menu()