"""
Print the current date and time, and my name and surname.
"""
from datetime import datetime


def print_datetime_name(name: str):
    """
    Print the current date, time, and the passed name.
    :param name: name to print after date and time.
    :return: None
    """
    now = datetime.now()
    current_datetime = now.strftime('%d/%m/%Y %H:%M:%S')

    print(f'Current date and time: {current_datetime}.\n'
          f'My name is {name}.')


if __name__ == '__main__':
    print_datetime_name('Sofiia Myntiuk')
