import random

def get_numbers_ticket(min:int, max: int, quantity: int) -> list:
    """
    This function ganerates a set of unique random numbers where all random numbers in the set must be unique.
    The total number of ganerated numbers specified by the quantity parameter. 
    All ganerated number will be in the range(min, max)

    Parameters:
    min (int): The minimum possible number in the range.
    max (int): The maximum possible number in the range.
    quantity (int): The number of unique random numbers to generate.

    Returns:
    (list) A list of unique random numbers within the specified range
    """
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int):
        random_seq = []
        for i in range(0, quantity):
            random_num = random.randrange(min, max)
            if random_num not in random_seq:
                random_seq.append(random_num)
        return random_seq
    else:
        # raise TypeError('Type of variables: `min`, `max` and `quantity` must be an integer') 
        return 'Type of variables: `min`, `max` and `quantity` must be an integer'   


print(get_numbers_ticket(1, 49, 'ftgjx'))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, -5, 6))
# print(get_numbers_ticket(1, 3, -5))
print(get_numbers_ticket(None, None, None))
print(get_numbers_ticket(0, 0, 0))
