"""
Program: string_functions.py
Author: Daniel Meeker
Date: 6/15/2020

This program defines and tests a function to multiply strings.
"""


def multiply_string(message, n):
    """
    This function takes in a string and an int and
    multiplies the string by the int.

    :param message: string to be multiplied
    :param n: number of times string is multiplied
    :return: completed string multiplication
    """
    return message*n


if __name__ == '__main__':
    print(multiply_string('Python', 6))
