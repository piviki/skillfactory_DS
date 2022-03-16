# Computer Guess A Number Game
# What shall we get from this task:
# 1. Our computer thinks of an integer number from 1 to 100, and we need to guess this number. 
# By the task  "guess"  we mean action to  "write a program (codes) that guesses a number".
# 2. The algorithm takes into account information about 
# whether the random number is greater or less than what we need.
# 3. It is necessary to ensure that the program number guesses are achieved with less than 20 attempts

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число (Randomly guess a number)

    Args:
        number (int, optional): Загаданное число (Hidden number). Defaults to 1.

    Returns:
        int: Число попыток (Number of attempts)
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 100) # 1.Our computer thinks of an integer number from 1 to 100
        if number == predict_number:
            break # exit from the loop if guessed correctly
    return(count)
print(f'Количество попыток (Number of attempts): {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм 
    (Attempts mean amount over 1000 approaches that guesses a number at our algorithm)

    Args:
        random_predict ([type]): функция угадывания (Guess function)

    Returns:
        int: среднее количество попыток (Mean number of attempts)
    """

    count_ls = [] # список для сохранения количества попыток (creating a list to save the number of attempts)
    np.random.seed(1) # фиксируем сид для воспроизводимости (fixing seed() for different values availability)
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел (made a list of numbers)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток (find the attempts mean number)

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    #print(f'Your algorithm guesses the number in: {score} times on mean attempts')
    return(score)

def optimal_predict(number: int = 1) -> int:
    """Компьютер угадает число меньше чем за 20 попыток
    
    (The computer guesses a number in less than 20 attempts)
    """

    import numpy as np

    min = 1
    max = 101

    number = np.random.randint(min, max)

    count = 0

    while True:
        count+=1
        mid = (min+max) // 2
    
        if mid > number:
            max = mid
    
        elif mid < number:
            min = mid

        else:
            print(f'Компьютер угадал число за {count} попыток. Это число {number}')
            #print(f'The computer guessed the number within  {count} attempts. The number is {number}')
            break #конец игры выход из цикла (loop exit)
    return count

optimal_predict(5)

