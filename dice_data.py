# The document for fooling around with the data.
# from dice_dictionary import dice_rolls as dr


def print_player_data(data=None,name=None):
    """Prints player rolls.

    Args:
        data: the dictionary from 'dr'
        name: the name of the player from 'dr' as a string. Case-sensitive!

        An example: print_player_data(data=dr,name="Grace")
    """
    for roll_key, roll_value in data[f"{name}"].items():
        print(f'{roll_key}')
        for key, value in roll_value.items():
            print(f"  {key}: {value}")
        print()

def pull_player_data(data=None,name=None):
    """Pulls the dictionary data for player rolls.

    Args:
        data: the dictionary from 'dr'
        name: the name of the player from 'dr' as a string. Case-sensitive!

        An example: print_player_data(data=dr,name="Grace")
    """
    required_info = {}
    # for roll_key, roll_value in data[name].items():
    for key, value in data[name].items():
        required_info.update({key:value})
    return required_info
