from random import randint
def get_unique_list_numbers(min_: int = -10,
                            max_: int = 10,
                            size: int = 15) -> list[int]:

    list_ = []
    while len(list_) != size:
        rand_val = randint(min_, max_)
        if rand_val not in list_:
            list_ .append(rand_val)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
