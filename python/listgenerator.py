import random

def ListIntegerGenerator(number : int, min : int, max:int) -> list:
    return [random.randrange(min,max) for _ in range(number)]

def ListDescendingIntegerGenerator(number:int , min: int, max:int) -> list:
    list =  [random.randrange(min,max) for _ in range(number)]
    list.sort(reverse=True)
    return list

def ListStringGenerator(number : int, max_length : int) -> list:
    def random_string(length):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        result = ''.join(random.choice(alphabets) for _ in range(length))
        return result
    
    return [random_string(random.randint(3,max_length)) for _ in range(number)]

def ListFloatGenerator(number:int , min: float, max:float) -> list:
    return [round(random.uniform(min,max),2) for _ in range(number)]


