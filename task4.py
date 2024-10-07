from datetime import datetime, timedelta


users = [
    {'name':'Bob', 'birthday':'1990.10.12'}, # + Bob
    {'name':'Alice', 'birthday':'1989.10.5'}, 
    {'name':'Jack', 'birthday':'2001.11.01'},
    {'name':'Ibo', 'birthday':'2001.05.05'},
    {'name':'Yakov', 'birthday':'2001.09.30'},
    {'name':'Claire', 'birthday':'2000.10.14'}, # + Claire
    {'name':'Vincent', 'birthday':'1985.10.07'}, # + Vincent
    {'name':'Liloo', 'birthday':'1980.10.15'}
    ]


def get_upcoming_birthdays(users):
    """
    The function should determine list of people whose birthdays are in next 7 days including the current day.
    If the birthday falls on a weekend, the date of the greeting is moved to the following Monday.

    Parameters:
    users (str): A list of dictionaries containing the names and birthdates of people.

    Returns:
    (list of dict) The function returns a list of dictionaries, where each dictionary contains information
    about the person: name and date of congratulation whose data is in the string format 'year.month.date').
    """

    format = "%Y.%m.%d"

    # Convert birthday dates from str to datetime object
    for user in users:
        user['birthday'] = datetime.strptime(user['birthday'], format).date()
    
    current_date = datetime.today().date()
    
    # Find users whose birthdays are within the next 7 days
    upcoming_birthdays = []
    for user in users:
        # Create birthday for the current year
        current_year_birthday = user['birthday'].replace(year=current_date.year)
        
        # If the birthday has already passed, skip to next year
        if current_year_birthday < current_date:
            current_year_birthday = current_year_birthday.replace(year=current_date.year + 1)

        # Calculate the difference between the current date and the birthday
        difference = (current_year_birthday - current_date).days

        # Check if the birthday is within the next 7 days
        if 0 <= difference <= 7:
            # Check if the birthday falls on a weekend (Saturday or Sunday)
            if current_year_birthday.weekday() in [5, 6]:  # Saturday or Sunday
                # Move to next Monday
                next_monday = current_year_birthday + timedelta(days=(7-current_year_birthday.weekday()))
                upcoming_birthdays.append({'name': user['name'], 'congratulation_date': datetime.strftime(next_monday, format)})
            else:
                upcoming_birthdays.append({'name': user['name'], 'congratulation_date': datetime.strftime(current_year_birthday, format)})

    return upcoming_birthdays    

print(get_upcoming_birthdays(users))


