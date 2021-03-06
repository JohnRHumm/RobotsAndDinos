class Robot():
    def __init__(self,name,health,shield,energy,energy_recharge) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.shield_level = shield
        self.max_shield_level = shield
        self.energy = energy
        self.max_energy = energy
        self.weapons_list = []
        self.is_operational = True
        self.can_attack_this_round = True
        self.energy_recharge_rate = energy_recharge
        self.killed_by = ''
        self.killed_with = ''
        self.damage_inflicted = 0
        self.number_of_kills = 0
        print(f'    ....{self.name} is powered up and on online...')

   
    def equip_robot(self,weapons_list):
        self.weapons_list = weapons_list
        print(f'{self.name} has been equipped with:')
        for weapon in self.weapons_list:
            print(f'    {weapon.name} --> Damage Rating: {weapon.attack_power} Energy Cost: {weapon.attack_cost}')
    
    def list_status(self):
        if self.is_operational:
            print(f'    Robot: {self.name} --> Health: {self.health} Shield: {self.shield_level} Energy: {self.energy} Recharge Rate: {self.energy_recharge_rate}')
        else:
            print(f'    Robot {self.name} is destroyed')

    def recharge_energy(self):
        if self.is_operational:
            self.energy += self.energy_recharge_rate
            if self.energy > self.max_energy:
                self.energy = self.max_energy
  

    
   

