from datetime import datetime
from typing import NamedTuple

class UserInput(NamedTuple):
    name:str
    age:int

class AgeCalculator:
    def __init__(self, name: str, age: int) -> None:
        self.name = name[:20]  
        self.age = age

    def calculate_year_turn_for_100(self) -> int:
        """Calculate the year in which the user will turn 100 years old."""
        current_year = datetime.now().year
        years_until_100 = 100 - self.age
        return current_year + years_until_100

    def display_message(self) -> None:
        """Display a message with the user's name and the year they will turn 100."""
        year_100 = self.calculate_year_turn_for_100()
        print(f"{self.name}, you  turn 100 years old in the year {year_100}.")

def get_user_input() -> UserInput:
    """Prompt the user for their name and age, with validation."""
    while True:
        name = input("Enter your name (up to 20 characters): ").strip()
   
        if len(name) == 0 or len(name) > 20 or any(char.isdigit() for char in name):
            print("Invalid input: Name must be a non-empty string without digits and a maximum of 20 characters.")
            continue
        break  

    while True:
        age_input = input("Enter your age (0-120): ").strip()
        try:
            age = int(age_input)
            if age < 0 or age > 120:
                raise ValueError("Age must be between 0 and 120.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid age.")
    return UserInput(name=name,age=age)

def main() -> None:
    """Main function to execute the program."""
    user_details = get_user_input()
    
   
    age_calculator = AgeCalculator(name=user_details.name,age=user_details.age)
    
    age_calculator.display_message()


if __name__ == "__main__":
    main()
