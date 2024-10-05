import re
from datetime import datetime


def get_days_from_today(date:str) -> int:
    """
    This function calculate the number of days between the given and current dates.

    :param param1: string  
    :returns: int
    """
    if isinstance(date, str) and date:
        # Check if the format of given string is in right date format
        date_pattern = r"^(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})$"
        if re.fullmatch(date_pattern, date):
        # Check if the number of days in a month is valid (1-31) and the number of months is valid (1-12).
            date_pattern_check_month_day_numbers = r"^(?P<year>[0-9]{4})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|1[0-9]|2[0-9]|3[0-1])$"
            if re.fullmatch(date_pattern_check_month_day_numbers, date):
                # Convert given string to datetime object as following '2020-10-09'
                format = "%Y-%m-%d"
                datetime_obj = datetime.strptime(date, format)

                # Get a current date
                current_date = datetime.now()

                # Calculate difference between given date and current_date in days
                difference = datetime_obj.date() - current_date.date()
                return difference.days
            else:
                return "The number of monthes must be in the range: (1-12) and the number of days must be in the range: (1-31)"    
        else:
            return "Bad date format given. The date should be a string in this format: 'YYYY-MM-DD' "
    else:
        return "Bad type given. The date should be a string in this format: 'YYYY-MM-DD'"    


date1 = "1994-12-12"
date2 = '2024-10-09'
date3 = '12-10-2024'
date4 = '2024-10-04'
date5 = 2022
date6 = "12.12.1994"
date7 = "2026-02-75"
date8 = ""
date9 = "some text.."
date10 = "2024-10-04 2024-10-04"
print('date1: : ', get_days_from_today(date1)) # -
print('date2: : ', get_days_from_today(date2)) # 5
print('date3: : ', get_days_from_today(date3)) # another format than expected
print('date4: : ', get_days_from_today(date4)) # 0 same day
print('date5: : ', get_days_from_today(date5)) # not string
print('date6: : ', get_days_from_today(date6)) # 
print('date7: : ', get_days_from_today(date7)) # 
print('date8: : ', get_days_from_today(date8)) # 
print('date9: : ', get_days_from_today(date9)) # 
print('date10: : ', get_days_from_today(date10)) # 

# _______________________________________________
# Condition: 
# current_date = datetime.now() is '2024-1-04'

# Test case 1: Dates with negative difference (past date). Expected difference is -10890 days
assert get_days_from_today(date1) == -10889, "Test case 1 failed"

# Test case 2: Dates with positive difference (future date). Expected difference is 4 days. 
assert get_days_from_today(date2) == 5, "Test case 2 failed"

# Test case 3: Dates in wrong format '12-10-2024'. Expected response: "Bad date format given. The date should be a string in this format: 'YYYY-MM-DD' "
assert get_days_from_today(date3) == "Bad date format given. The date should be a string in this format: 'YYYY-MM-DD' ", "Test case 3 failed"

# Test case 4: Dates with zero difference (same day). Expected difference is 0 days.
assert get_days_from_today(date4) == 0, "Test case 4 failed"

print("All tests passed!")

