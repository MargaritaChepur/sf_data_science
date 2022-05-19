import numpy as np
def random_predict(number:int=1) -> int:
    """Guess number by computer and count number of trials
    """
    count=0
    
    while True:
        count+=1
        predict_number=np.random.randint(1,101)
        if number==predict_number:
            break
        
    return count

print("number of counts {}".format(random_predict()))

