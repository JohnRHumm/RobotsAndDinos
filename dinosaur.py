from unicodedata import name


class Dinosaur():
    def __init__(self,name,health,hide,endurance) -> None:
        self.name = name
        self.health = health
        self.hide_level = hide
        self.endurance = endurance
        self.attack_type = []
   
    def attack(self,robot,attack_type):
        self.target_robot = robot
        self.attack_type = attack_type



