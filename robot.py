class Robot():
    def __init__(self,name,health,shield) -> None:
        self.name = name
        self.health = health
        self.shield_level = shield
        self.weapons = []

    
    def attack(self,dinosaur,weapon):
        self.target_dinosaur = dinosaur
        self.weapon = weapon