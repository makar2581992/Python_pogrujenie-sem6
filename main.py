from sys import argv
from leap_year import date_validator


if __name__ == '__main__':
    data = '12.01.2020'
    print(date_validator(data))
