"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Загадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        count: Число попыток
    """
    
    count=0
    predict_number=np.random.randint(1,101) #предлагаем вариант числа
    
    """Сравниваем вариант числа и загаданное число. Если загаданное число больше варианта, 
    то новый вариант предлагаем в середине промежутка между исходным и 100.
    Если меньше, то новый вариант предлагаем в середине промежутка между исходным и 0.
    Далее перебираем числа в этом промежутке с шагом 1 или 2.
    """
    
    if number > predict_number:
        predict_number = predict_number + (100-predict_number)//2 
        
        while True:
            count+=1
            if number > predict_number:
                predict_number += 2
            
            elif number < predict_number:
                predict_number -= 1
            
            else:          
                break
            
    elif number < predict_number:
        predict_number = predict_number - (100-predict_number)//2
            
        while True:
            count+=1
            if number > predict_number:
                predict_number += 1
            
            elif number < predict_number:
                predict_number -= 2
            
            else:          
                break
    else:
        return count
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        score: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
