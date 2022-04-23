class Robot():
    def __init__(self,name,health,shield,energy) -> None:
        self.name = name
        self.health = health
        self.shield_level = shield
        self.energy = energy
        self.weapons_list = []
        self.is_operational = True
        self.can_attack_this_round = True
        print(f'    ....{self.name} is powered up and on online...')

    
    def attack(self,dinosaur,weapon):
        self.target_dinosaur = dinosaur
        self.weapon = weapon

    def equip_robot(self,weapons_list):
        self.weapons_list = weapons_list
        print(f'{self.name} has been equipped with:')
        for weapon in self.weapons_list:
            print(f'    {weapon.name} --> Damage Rating: {weapon.attack_power} Energy Cost: {weapon.attack_cost}')
