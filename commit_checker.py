import os
import subprocess
from datetime import datetime

# START_MONTH = input("Month to begin searching: ")
# START_DAY = input("Day to begin searching: ")
YEAR = '2023'
DEFAULT_TIME = '1:00:00'

# def handle_homework_date(homework_tuple):
    # is_friday =


def ask_type():
    valid_input = ['h', 'c']
    type = input("Homework or Classwork: ")
    while len(type) < 1 or type[0].lower() not in valid_input:
        type = input("Bad Input. Homework or Classwork: ")

    if type[0].lower() == 'h':
        valid_bool = ['y', 'n']
        weekend_bool = input("Is it a Friday? y/n: ")
        while len(type) < 1 or type[0].lower() not in valid_bool:
            type = input("Bad Input. Is it a Friday? y/n: ") 

        return ()

    return tuple(type[0].lower())

# def start_date():
    


# start_date_time = f'{YEAR}-{START_MONTH}-{START_DAY} '

def main():
    start_date()

if __name__ == "__main__":
    main()