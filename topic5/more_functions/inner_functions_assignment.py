"""
Program: inner_functions_assignment
Author: Daniel Meeker
Date: 6/17/2020

This program defines a function with two inner functions
to calculate the area and the perimeter of the list passed in
"""


def measurements(list_of_measurements):
    """
    Outer function for the calculations
    :param list_of_measurements: a list of either one or two measurements
    :return: a string with both area and perimeter
    """
    def area(a_list):
        """
        inner function to calculate area
        :param a_list: list of measurements for calculation
        :return: a float number representing area
        """
        if len(a_list) == 2:
            return float(a_list[0]*a_list[1])
        else:
            return float(a_list[0]*a_list[0])

    def perimeter(a_list):
        """
        inner function to calculate perimeter
        :param a_list: list of measurements for calculation
        :return: a float number representing perimeter
        """
        if len(a_list) == 2:
            return float(a_list[0]*2 + a_list[1]*2)
        else:
            return float(a_list)*4
    area_of_object = area(list_of_measurements)
    perimeter_of_object = perimeter(list_of_measurements)
    return "Perimeter = {} Area = {}".format(perimeter_of_object, area_of_object)
