from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self) -> None:
        team_dinosaurs = Herd()
        team_robots = Fleet()
    
    def run_game(self):
        self.display_welcome()
        self.setup_the_robots()

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dinosaurs_turn(self,dinosaur):
        pass

    def robots_trun(self,robot):
        pass

    def show_dinosaur_options(self):
        pass

    def show_robot_options(self):
        pass

    def display_winners(self):
        pass

    def setup_the_robots(self):
        laser_gun = Weapon('Laser Gun',20,5)
        plasma_sword = Weapon('Plasma Sword',25,5)

        laser_cannon = Weapon('Laser Cannon',40,20)
        flame_thrower = Weapon('Flame Thrower',30,15)
        
        missle = Weapon('Guided Missle',50,40)
        magnetic_pulse = Weapon('Magnetic Pulse',40,35)
        gamma_ray = Weapon('Gamma Ray',60,75)
        
        print('---- Activating Robots ----')
        robot_1 = Robot('T-800',200,75,100)
        robot_2 = Robot('T-1000',150,150,150)
        robot_3 = Robot('T-X',200,200,200)
        print('---- Robots Activated ----\n')

        print('---- Arming Robots ----')
        robot_1.equip_robot([laser_gun,flame_thrower,magnetic_pulse])
        robot_2.equip_robot([laser_gun,laser_cannon,missle])
        robot_3.equip_robot([plasma_sword,laser_cannon,gamma_ray])
        print('---- Robots Armed ----\n')




