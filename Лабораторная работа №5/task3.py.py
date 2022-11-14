from random import randint
def get_unique_list_numbers() -> list[int]:
    size = 15
    min_ = -10
    max_ = 10
    list_= []
    while len(list_) != size:
        rand_val = randint(min_, max_)
        if rand_val not in list_:
            list_ .append(rand_val)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
