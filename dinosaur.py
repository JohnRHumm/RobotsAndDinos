from unicodedata import name

class Dinosaur():
    def __init__(self,name,health,hide,endurance) -> None:
        self.name = name
        self.health = health
        self.hide_level = hide
        self.endurance = endurance
        self.attack_type = []
        self.is_alive = True
        self.can_attack_this_round = True
        print(f'    ....{self.name} is awake and angry...')
   
    def attack(self,robot,attack_type):
        self.target_robot = robot
        self.attack_type = attack_type

    def dino_attack(self,weapons_list):
        self.weapons_list = weapons_list
        print(f'{self.name} has the following attacks:')
        for weapon in self.weapons_list:
            print(f'    {weapon.name} --> Damage Rating: {weapon.attack_power} Endurance Cost: {weapon.attack_cost}')

