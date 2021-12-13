"""The computer guesses the numbers by itself in less than 20 attempts"""

import numpy as np


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


def score_game(middle_predict) -> int:
    """For how many attempts on average for 1000 approaches does our algorithm guess

    Args:
        middle_predict ([type]): the function of guess

    Returns:
        int: average number of attempts
    """

    count_ls = [] # list to save the number of attempts
    np.random.seed(1) # we fix the sid for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers

    for number in random_array:
        count_ls.append(middle_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts

    print(f'Your algorithm guesses the number on: {score} average per attempts')
    return(score)


if __name__ == "__main__":
    # RUN
    score_game(middle_predict) 