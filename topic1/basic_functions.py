"""
Program: basic_functions.py
Author: Daniel Meeker
Date: 06/14/2020

This program will define and call a function designed to
gather and print user input.
"""


def hourly_employee_input():
    """This function will gather and print
    employee name, hours worked, and hourly pay rate"""
    try:
        employee_first_name = input("Please enter your first name: ")
        if not employee_first_name.isalpha():
            print("First Name Error: Enter first name only without any numbers or symbols.")
            raise ValueError
        employee_last_name = input("Please enter your last name: ")
        if not employee_last_name.isalpha():
            print("Last Name Error: Enter first name only without any numbers or symbols.")
            raise ValueError
        employee_hours = int(input("Please enter in your hours worked: "))
        if employee_hours < 0:
            print("Hours can't be negative!")
            raise ValueError
        elif employee_hours > 80:
            print("We don't allow overtime, please report to HR for discipline!")
            raise ValueError
        employee_pay_rate = float(input("Please enter in your hourly wage: "))
        if employee_pay_rate < 0:
            print("Pay can't be negative!")
            raise ValueError
        elif employee_pay_rate < 7.25:
            print("Pay can't be less than minimum wage!")
            raise ValueError
        elif employee_pay_rate > 1000:
            print("Ain't no way you make that much.")
            raise ValueError
    except ValueError as err:
        print("Error in input detected")
    else:
        print("Employee name: {}, {} \nHours Worked: {}\nHourly Wage: ${:.2f}".format(employee_last_name,
                                                                                      employee_first_name,
                                                                                      employee_hours,
                                                                                      employee_pay_rate))


if __name__ == '__main__':
    hourly_employee_input()
