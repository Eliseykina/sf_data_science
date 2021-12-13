"""The computer guesses the numbers by itself in less than 20 attempts"""

import numpy as np

number = np.random.randint(1, 101) # guessing the number


def middle_predict(number) -> int:
    """Guessing the hidden number using the fast search algorithm

    Args:
        number ([type]): the hidden number

    Returns:
        int: number of attempts
    """
    count = 0
    begin = 1
    end = 100

    while True:
        count +=1
        list_numbers = list(range(begin,end+1))
        mean_index = len(list_numbers)//2
        mean = list_numbers[mean_index]

        if number < mean:
            end = list_numbers[mean_index-1]

        elif number > mean:
            begin = list_numbers[mean_index+1]
            
        else:
            break 
         
    return count


print(f"The computer guessed the number in {middle_predict(number)} attempts")