class Robot():
    def __init__(self,name,health,shield,energy) -> None:
        self.name = name
        self.health = health
        self.shield_level = shield
        self.energy = energy
        self.weapons = []
        self.is_operational = True
        self.can_attack_this_round = True

    
    def attack(self,dinosaur,weapon):
        self.target_dinosaur = dinosaur
        self.weapon = weapon