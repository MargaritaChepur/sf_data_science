import numpy as np
number = np.random.randint(1, 100)
count = 0
"""_summary_
    """

while True:
    count+=1
    guess_num = int(input("Загадано число от 1 до 100. Введите ваш ответ "))
    if guess_num > number:
        print("Число слишком большое")
    elif guess_num < number:
        print("Число слишком маленькое")
    else:
        print("Вы угадали число {} с {} попытки".format(number, count))
        break
    
