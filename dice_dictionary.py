# Playing around with a dictionary to keep track of dice rolls in a D&D game for future number crunching.
# Types would be 'melee', 'ranged', 'ability', 'save', 'initiative'
dice_rolls = {
    "Bob": {
        'roll1': {
            "type": "melee",
            "difficulty": 15,
            "skill": False,            
            "stat":{
                "stat": "strength",
                "modifier": 1
            },
            "proficiency": {
                "prof": True,
                "mod": 3,
            },
            "roll": {
                "dice": 16,
                "n_a_d": {
                    "nad": "n",
                    "dice": False
                },
            },
            "total": 20,
            "result": True
        },
        'roll2': {
            "type": "save",
            "difficulty": 15,
            "skill": False,            
            "stat":{
                "stat": "constitution",
                "modifier": 2
            },
            "proficiency": {
                "prof": True,
                "mod": 3,
            },
            "roll": {
                "dice": 4,
                "n_a_d": {
                    "nad": "a",
                    "dice": 13
                },
            },
            "total": 18,
            "result": True
        },
    },
    "Grace": {
        'roll1': {
            "type": "ability",
            "difficulty": 18,
            "skill": "arcana",            
            "stat":{
                "stat": "intelligence",
                "modifier": 3
            },
            "proficiency": {
                "prof": False,
                "mod": 0,
            },
            "roll": {
                "dice": 16,
                "n_a_d": {
                    "nad": "d",
                    "dice": 8
                },
            },
            "total": 11,
            "result": False
        },
        'roll2': {
            "type": "initiative", 
            # Not sure exactly the best way to track initiative rolls
            "difficulty": False,
            "skill": False,            
            "stat":{
                "stat": "dexterity",
                "modifier": 1
            },
            "proficiency": {
                "prof": False,
                "mod": 0,
            },
            "roll": {
                "dice": 12,
                "n_a_d": {
                    "nad": "n",
                    "dice": False
                },
            },
            "total": 13,
            "result": True
        },
    }
}