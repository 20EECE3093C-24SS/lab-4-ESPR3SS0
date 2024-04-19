# TODO-1: add convert_to_letter_grade(score) function
def convert_to_letter_grade(score: int)->str:
    '''Function to convert score to letter grade

    Args:
        score (int): The score between 0 and 100

    Returns: 
        str: The letter grade

    Raises:
        ValueError: If score is less than 0 or greater than 100
    '''

    if score < 0 or score > 100:
        raise ValueError
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'
