def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    This function is designed to validate test scores entered into the program
    :param test_name: Required - no validation on the test name itself
    :param test_score: Optional - defaults to 0, must be between 0 and 100
    :param invalid_message: Optional - has a default message that is returned if the score is invalid
    :return: a string following the format 'test_name: test_score'
    """
    if not str(test_score).isnumeric():
        return invalid_message
    if float(test_score) < 0:
        return invalid_message
    elif float(test_score) > 100:
        return invalid_message
    return test_name + ': ' + str(test_score)
