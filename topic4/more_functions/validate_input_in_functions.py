"""
Program: validate_input_in_functions
Author: Daniel Meeker
Date: 6/17/2020

This program defines and tests a function to validate input that is
used as a parameter of the function.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    This function is designed to validate test scores entered into the program

    :param test_name: Required - no validation on the test name itself
    :param test_score: Optional - defaults to 0, must be between 0 and 100
    :param invalid_message: Optional - has a default message that is returned if the score is invalid
    :return: a string following the format 'test_name: test_score'
    """
    if not str(test_score).isnumeric():
        raise ValueError(invalid_message)
    elif float(test_score) < 0:
        raise ValueError(invalid_message)
    elif float(test_score) > 100:
        raise ValueError(invalid_message)
    else:
        return test_name + ': ' + str(test_score)


if __name__ == '__main__':
    try:
        """
        These are all redundant checks in the code below. I was trying my best to fulfill the directions
        which ask that the function prompt for input until it is valid, however I could not
        come up with a way to do that and still have the function throw exceptions as is required
        by the Rubric. In my view having one function fulfill both of these requirements seemed
        unreasonable so I set up a loop in the main code so that when executed this way the user
        is prompted for input until it is a valid input but if the function were to be called 
        by passing in invalid values it would throw exceptions 
        """
        valid = False
        score = input('Please enter a score for a test: ')
        while not valid:
            if not str(score).isnumeric():
                score = input('Please enter a positive numeric value for the test: ')
            elif not 0 < int(float(score)) < 100:
                score = input('Please enter a valid score for the test: ')
            else:
                valid = True
        print(score_input('Python', score))
    except ValueError as ex:
        print(ex)
