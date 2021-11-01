class Rogue:

    weapons = [
        {
        "dagger": { 
            "damage": 16,
            "thrown": True
        }
        },
        {
            "crossbow": {
                "damage": 25,
                "thrown": False,
            }
        }
    ]
    stats = {
        'hp': 20,
        'dexterity': 5,
        'strength': 10,
        'int': 20
    }

    def __init__(self, name, race, weapons):
        self.name = name
        self.race = race
        self.weapons = weapons

    def backstab(self, enemy_hp, weapon_damage): 
        if 'dagger' in self.weapons[0]