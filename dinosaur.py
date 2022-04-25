from unicodedata import name

class Dinosaur():
    def __init__(self,name,health,hide,endurance,recovery) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.hide_strength = hide
        self.endurance = endurance
        self.max_endurance = endurance
        self.recovery_rate = recovery
        self.attack_type = []
        self.is_alive = True
        self.can_attack_this_round = True
        print(f'    ....{self.name} is awake and angry...')
   
    def attack(self,robot,attack_type):
        self.target_robot = robot
        self.attack_type = attack_type

    def dino_attack(self,attack_list):
        self.attack_type = attack_list
        print(f'{self.name} has the following attacks:')
        for attack in self.attack_type:
            print(f'    {attack.name} --> Damage Rating: {attack.attack_power} Endurance Cost: {attack.attack_cost}')

    def list_status(self):
        if self.is_alive:
            print(f'    Dinosaur: {self.name} --> Health: {self.health} Hide Strength: {self.hide_strength} Endurance: {self.endurance} Recovery Rate: {self.recovery_rate}')
        else:
            print(f'    Dinosaur {self.name} is dead')
    
    def recover_endurance(self):
        if self.is_alive:
            self.endurance += self.recovery_rate
            if self.endurance > self.max_endurance:
                self.endurance = self.max_endurance
    
    # def make_dinosaur_selection_list(self,index):
    #     if self.is_alive:
    #         print(f'    {index}: Dinosaur: {self.name} --> Health: {self.health} Endurance: {self.endurance} ')
    #     else:
    #         print(f'    {index}: Dinosaur {self.name} is dead')
    
    # def make_dinosaur_attack_list(self,index,attack_index):
    #     print(f'    {index}: Attack: {self.attack_type[attack_index].name} Damage Rating: {self.attack_type[attack_index].attack_power} Endurance Cost: {self.attack_type[attack_index].attack_cost}')