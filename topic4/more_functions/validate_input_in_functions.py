def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    This function is designed to validate test scores entered into the program
    :param test_name: Required - no validation on the test name itself
    :param test_score: Optional - defaults to 0, must be between 0 and 100
    :param invalid_message: Optional - has a default message that is returned if the score is invalid
    :return: a string following the format 'test_name: test_score'
    """
    return test_name + ': ' + str(test_score)
