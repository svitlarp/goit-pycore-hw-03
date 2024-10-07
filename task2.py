import random

def get_numbers_ticket(min_num:int, max_num: int, quantity: int) -> list:
    """
    This function ganerates a set of unique random numbers where all random numbers in the set must be unique.
    The total number of ganerated numbers specified by the quantity parameter. 
    All ganerated number will be in the range(min, max)

    Parameters:
    min_num (int): The minimum possible number in the range.
    max_num (int): The maximum possible number in the range.
    quantity (int): The number of unique random numbers to generate.

    Returns:
    (list) A list of unique random numbers within the specified range
    """
    if isinstance(min_num, int) and min_num >= 0 and isinstance(max_num, int) and max_num > 0 and isinstance(quantity, int):
        random_seq = []
        for i in range(0, quantity):
            random_num = random.randrange(min_num, max_num)
            if random_num not in random_seq:
                random_seq.append(random_num)
        return random_seq
    else:
        # raise TypeError('Type of variables: `min_num`, `max_num` and `quantity` must be an integer') 
        return 'Type of variables: `min_num`, `max_num` and `quantity` must be a positive integer'   


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1000, 10000, 6))
print(get_numbers_ticket(1, 49, 'ftgjx'))
print(get_numbers_ticket(1, -5, 6))
print(get_numbers_ticket(1, 3, -5))
print(get_numbers_ticket(None, None, None))
print(get_numbers_ticket(0, 0, 0))
