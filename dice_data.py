import json
import random
import pandas
from statistics import mean

def the_data():
    """Pulls the roll data from 'dice_rolls.json'

    Returns:
        A dictionary with the dice rolls.
    """
    with open('dice_rolls.json', 'r') as f:
        data = json.load(f)
        return data

def get_many_numbers():
    """A quick way to get 100 integers between 1 and 20.

        Returns:
            A list with 100 integers between 1 and 20.
        """
    nums = []
    for i in range(99):
        y=random.randrange(1,21)
        nums.append(y)
    return nums

def get_single_number():
    """Get one integer between 1 and 20.

        Returns:
            An integer between 1 and 20.
        """
    num = random.randrange(1,21)
    return num

def print_player_data(data=the_data(),name=None):
    """Prints player rolls.
    Full disclosure here: this was mostly created for me to test that I did this right.
    "Why didn't you use PyTest, Steve?" Why don't you mind ya business, random person!

    Args:
        data: the dictionary from 'the_data'
        name: the name of the player from 'the_data' as a string. Case-sensitive!

        An example: print_player_data(data=the_data(),name="Grace")
    """
    for roll_key, roll_value in data[f"{name}"].items():
        print(f'{roll_key}')
        for key, value in roll_value.items():
            print(f"  {key}: {value}")
        print()

def pull_player_data(data=the_data(),name=None):
    """Pulls the dictionary data for player rolls.

    Args:
        data: the dictionary from 'the_data'
        name: the name of the player from 'the_data' as a string. Case-sensitive!

    Returns:
        A dictionary with the roll data for the specified player.
    Example:
        print_player_data(name="Grace")
    """
    required_info = {}
    for key, value in data[name].items():
        required_info.update({key:value})
    return required_info

def player_d20_roll_results(name=None):
    """Extracts the "final" d20 rolls that each player made.
    Takes Advantage/Disadvantage into consideration

    Args:
        name: the name of the player you want to pull data for. Case-sensitive!

    Returns:
          a list of integers representing the dice rolls of the player requested.
    Example:
         player_d20_roll_results(name="Grace")
    """
    player_data = pull_player_data(data=the_data(),name=name)
    numbers = []
    for roll,details in player_data.items():
        if details["roll"]["n_a_d"]["nad"]=="a":
            numbers.append(details["roll"]["n_a_d"]["dice"])
        elif details["roll"]["n_a_d"]["nad"] == "d":
            numbers.append(details["roll"]["n_a_d"]["dice"])
        else:
            numbers.append(details["roll"]["dice"])
    return numbers

def date_results(name=None,date=None):
    """Pulls the dice results for a specific date.

        Args:
            name: the name of the player
            date: the date as a string, "day,month,year", e.g., "03,12,2023" for December 3, 2023.
        Returns:
            A list of integers representing the dice rolls for the given date.
        Example:
            date_results(name='Bob',date="19,11,2023")
    """
    player_data = pull_player_data(data=the_data(),name=name)
    numbers = []
    for roll, details in player_data.items():
        if details["date"]==date:
                if details["roll"]["n_a_d"]["nad"] == "a":
                    numbers.append(details["roll"]["n_a_d"]["dice"])
                elif details["roll"]["n_a_d"]["nad"] == "d":
                    numbers.append(details["roll"]["n_a_d"]["dice"])
                else:
                    numbers.append(details["roll"]["dice"])
    return numbers

def sort_dates(name=None,date=None):
    """Pulls the dice rolls for a specific date.

        Args:
            name: the name of the player
            date: the date as a string, "day,month,year", e.g., "03,12,2023" for December 3, 2023.
        Returns:
            A dictionary of roll data pertaining to the given date.
        Example:
            sort_dates(name="Grace",date="19,11,2023")
    """
    player_data = pull_player_data(name=name)
    rolls = {}
    roll_num = 1
    for roll, details in player_data.items():
        if details["date"] == date:
            rolls[f"{roll_num}"]=details
            roll_num+=1
    return rolls

def the_mean(data=None):
    """Finds the mean of all of a player's rolls.

    Args:
        data: the 'player_data' function.

    Returns:
        an integer that represents the mean of all the player's rolls.
    Example:
        the_mean(data=player_d20_roll_results(name="Bob"))
    """
    numbers = data
    meany = mean(numbers)
    round_mean = round(meany)
    return round_mean

# Messing around with Pandas, please ignore.
# pd = pandas.DataFrame.from_dict(the_data(),orient="index")
# print(pd)