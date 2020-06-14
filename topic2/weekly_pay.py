"""
Program: weekly_pay.py
Author: Daniel Meeker
Date: 06/14/2020

This program will use the input gathered from hourly_employee_input()
and pass the hours and hourly wage to another function to calculate
the weekly wage.
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
        employee_hours = int(input("Please enter in your hours worked this week: "))
        if employee_hours < 0:
            print("Hours can't be negative!")
            raise ValueError
        elif employee_hours > 40:
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
        return "Error in input detected"
    else:
        return ("Employee name: {}, {}\nWeekly Pay: ${:.2f}".format(employee_last_name,
                                                                    employee_first_name,
                                                                    weekly_pay(employee_hours,
                                                                               employee_pay_rate)))


def weekly_pay(hours, wage):
    """This function performs the calculation hours * wage to get weekly pay
    :param hours: This is the number of hours worked in the week
    :param wage: This is the amount of money per hour
    """
    return hours * wage


if __name__ == '__main__':
    print(hourly_employee_input())
