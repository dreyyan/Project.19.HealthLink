''' MODULES '''
from msys.characterDelayAnimation import characterDelayAnimation
from msys.lineDelayAnimation import lineDelayAnimation
from msys.displayFormat import displayFormat
from msys.clearScreen import clearScreen
from msys.errorMessage import errorMessage
from msys.pressEnterToContinue import pressEnterToContinue

''' IMPORTS '''
from datetime import datetime, date
import time, re

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

    ''' UTILITIES '''
    @staticmethod
    def display_header(menu_title: str):         
        lineDelayAnimation("      [ HealthLink ]", 0.1)
        lineDelayAnimation(menu_title.center(25), 0.1)
        displayFormat('*', 25)

    ''' CUSTOM EXCEPTIONS ''' 
    class InvalidNameError(Exception):
        pass
    
    class InvalidGenderError(Exception):
        pass

    class InvalidDateOfBirthError(Exception):
        pass
    
    class InvalidNationalityError(Exception):
        pass
    
    class InvalidAddressError(Exception):
        pass
    
    class InvalidContactNumberError(Exception):
        pass
    
    class InvalidEmailError(Exception):
        pass

    ''' VALIDATIONS '''
    def validate_name(name: str) -> None:
        if len(name) == 0: # ERROR: blank input
            raise Patient.InvalidNameError("Name must not be blank")
        
        if bool(re.search(r'\d', name)): # ERROR: number/s input
            raise Patient.InvalidNameError("Name must not contain numbers")

        if bool(re.search(r'[^A-Za-z0-9\s]', name)): # ERROR: special character/s input
            raise Patient.InvalidNameError("Name must not contain special characters")

        if not (2 < len(name) < 50):
            raise Patient.InvalidNameError("Name must be between 2 to 50 characters")
 
    def validate_gender(gender: str) -> None:
        pass

    def validate_date_of_birth(date_of_birth: date) -> None:
        pass

    def validate_nationality(nationality: str) -> None:
        pass

    def validate_address(address: str) -> None:
        pass

    def validate_contact_number(contact_number: str) -> None:
        pass

    def validate_email(email: str) -> None:
        pass
        
    ''' METHODS '''
    def display_information(self) -> None:
        lineDelayAnimation(f"{'':<4}[ PATIENT INFORMATION ]", 0.2)
        lineDelayAnimation(f"{'Name: ':>14}{self.name}", 0.2)
        lineDelayAnimation(f"{'Age: ':>14}{self.get_age()}", 0.2)
        lineDelayAnimation(f"{'Gender: ':>14}{self.gender}", 0.2)
        lineDelayAnimation(f"{'Date of Birth: ':>14}{self.birthdate}", 0.2)
        lineDelayAnimation(f"{'Nationality: ':>14}{self.nationality}", 0.2)
        lineDelayAnimation(f"{'Address: ':>14}{self.address}", 0.2)
        lineDelayAnimation(f"{'Contact No.: ':>14}{self.phone_number}", 0.2)
        lineDelayAnimation(f"{'Email: ':>14}{self.email}", 0.2)

    def admit_new_patient():
        Patient.display_header("Admit New Patient")

        # Name Validation
        while True:
            try:
                patient_name: str = input("[ Enter Name of Patient ] >> ").strip()
                Patient.validate_name()
                break

            except Patient.InvalidNameError:
                errorMessage("Invalid input, please enter a valid name")

        # Gender Validation    
        while True:
            try:
                patient_gender: str = input("[ Enter Gender ] >> ").strip()
                Patient.validate_gender()
                break
                    
            except Patient.InvalidGenderError:
                errorMessage("Invalid input, please enter a valid gender")

        # Date of Birth Validation
        while True:
            try:
                patient_date_of_birth: str = input("[ Enter Date of Birth ] >> ").strip()
                Patient.validate_date_of_birth()
                break
                    
            except Patient.InvalidDateOfBirthError:
                errorMessage("Invalid input, please enter a valid date of birth")

        # Nationality Validation
        while True:
            try:
                patient_nationality: str = input("[ Enter Nationality ] >> ").strip()
                Patient.validate_nationality()
                break
                    
            except Patient.InvalidNationalityError:
                errorMessage("Invalid input, please enter a valid nationality")

        # Address Validation
        while True:
            try:
                patient_name: str = input("[ Enter Address ] >> ").strip()
                Patient.validate_address()
                break
                    
            except Patient.InvalidAddressError:
                errorMessage("Invalid input, please enter a valid address")

        # Contact No. Validation
        while True:
            try:
                patient_name: str = input("[ Enter Contact No. ] >> ").strip()
                Patient.validate_contact_number()
                break
                    
            except Patient.InvalidContactNumberError:
                errorMessage("Invalid input, please enter a valid contact no.")

        # Email Validation
        while True:
            try:
                patient_name: str = input("[ Enter Email ] >> ").strip()
                Patient.validate_email()
                break
                    
            except Patient.InvalidEmailError:
                errorMessage("Invalid input, please enter a valid email")
            
    def patient_list():
        Patient.display_header("Patient List")

    def update_patient_record():
        Patient.display_header("Update Patient Record")

    def discharge_patient():
        Patient.display_header("Discharge Patient")

    @staticmethod
    def display_main_menu():
        while True:
            clearScreen()
            try:
                Patient.display_header("Main Menu")
                lineDelayAnimation("[1] Admit New Patient", 0.1)
                lineDelayAnimation("[2] Patient List", 0.1)
                lineDelayAnimation("[3] Update Patient Record", 0.1)
                lineDelayAnimation("[4] Discharge Patient", 0.1)
                lineDelayAnimation("[5] Exit", 0.1)
                displayFormat('*', 25)

                # prompt user to enter choice
                user_choice = input("~ ").strip().lower()

                # clear screen before navigating
                clearScreen()

                if user_choice in ["1", "admit"]:
                    Patient.admit_new_patient()
                elif user_choice in ["2", "list"]:
                    Patient.patient_list()
                elif user_choice in ["3", "update"]:
                    Patient.update_patient_record()
                elif user_choice in ["4", "discharge"]:
                    Patient.discharge_patient()
                elif user_choice in ["5", "exit"]:
                    clearScreen()
                    characterDelayAnimation("` exiting system... `", 0.1)
                    time.sleep(2)
                    break
                else:
                    errorMessage("Invalid input, please enter a valid choice")
            
            except ValueError as e:
                print(f"ERROR: {e}")

            pressEnterToContinue()

person: Patient = Patient("Adrian Dominic L. Tan", "2005-07-29", 'M', "Filipino", "Iloilo City, Iloilo", "09382277245", "adriandominic.tan@wvsu.edu.ph")
person.display_main_menu()