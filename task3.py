import re

def normalize_phone(phone_number):
    """
    Normalize a phone number to the international format `+380XXXXXXXXX`.

    This function removes special characters (e.g., parentheses, dashes, spaces), letters, and 
    ensures the phone number is in the correct international format for Ukraine (+380). 
    It handles different cases, such as numbers starting with '0', '380', or missing country code, 
    and formats them appropriately.

    Parameters:
    phone_number (str): The input phone number to be normalized.

    Returns:
    (str) A normalized phone number in the format `+380XXXXXXXXX`.
    """

    pattern = re.compile(r"[\(\)\.\-\s\\]+|[a-z]|[A-Z]")
    country_code_pattern = r""
    repl = ''
    formatted_phone_number = re.sub(pattern, repl, phone_number)

    if re.search(r"(^0)", formatted_phone_number): # check if there no code 
        return f"+38{formatted_phone_number}"
    elif re.search(r"(^380)", formatted_phone_number): # there code but not in a ful format like `38093455678`->
        return f"+{formatted_phone_number}"  
    else: # re.search(r"(^+380)")
        return formatted_phone_number
            

# Test for phone numbers starting with `0` (should add `+38`)
assert normalize_phone("     0503451234") == "+380503451234", "Test case 1 failed"
assert normalize_phone("(050)8889900") == "+380508889900", "Test case 1 failed"

# Test for phone numbers starting with `38` (should add `+`)
assert normalize_phone("380501234567") == "+380501234567", "Test case 2 failed"
assert normalize_phone("38050-111-22-22") == "+380501112222", "Test case 2 failed"

# Test for phone numbers in correct format (should return phone)
assert normalize_phone("+380501234567") == "+380501234567", "Test case 4 failed"
assert normalize_phone("+380938289234") == "+380938289234", "Test case 1 failed"

# Test for phone numbers in conteining letters or characters (should remove it)
assert normalize_phone("067\\t123 4567") == "+380671234567", "Test case 4 failed"
assert normalize_phone("(095) 234-5678\\n") == "+380952345678", "Test case 1 failed"
assert normalize_phone("+380 44 123 4567yui") == "+380441234567", "Test case 4 failed"


# To handle a case when phone number starts after 0 (without +380)
# elif re.search(r"(^[1-9]{9})", formatted_phone_number): #
#     return f"+380{formatted_phone_number}" 

# Test for phone numbers starting with number like 93 71 72 55 (should add `+380`)
# assert normalize_phone("  93-71-72-55") == "+38093717255", "Test case 3 failed"
# assert normalize_phone("(50)8889900") == "+380508889900", "Test case 3 failed" 