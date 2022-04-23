from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self) -> None:
        self.jungle_swarm = Herd('Jungle Swarm')
        self.alpha_squad = Fleet("Alpha Squad")
    
    def run_game(self):
        self.display_welcome()
        self.setup_the_robots()
        self.setup_the_dinosaurs()

    def display_welcome(self):
        print("""
The rapid and uncontrolled advancement of genetics research led to the rebirth of savage dinsosaurs which quickly
evolved and swarmed the Earth. In response, DARPA created an advanced line of Robot Marines equipped with devastating
weapons and artificIal intelligence to defend the Earth. The self-aware robots identified humans to be their primary threat
and exterminated all civilization. AI Robots and Genetically Programed Dinosaurs now battle for control of the planet.\n
Welcome to the year 2205\n-----------------------\n""" )

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
        eye_beams = Weapon('Eye Beams',25,5)
        plasma_sword = Weapon('Plasma Sword',30,5)

        flame_thrower = Weapon('Flame Thrower',30,15)
        laser_cannon = Weapon('Laser Cannon',40,20)
        sonic_blast = Weapon('Sonic Blast',50,25)
                
        magnetic_pulse = Weapon('Magnetic Pulse',40,35)
        missle = Weapon('Guided Missle',50,45)
        gamma_ray = Weapon('Gamma Ray',60,55)
        
        print('---- Activating Robots ----')
        robot_1 = Robot('T-800',200,75,100)
        robot_2 = Robot('T-1000',150,150,150)
        robot_3 = Robot('T-X',200,200,200)
        print('---- Robots Activated ----')

        print('---- Arming Robots ----')
        robot_1.equip_robot([laser_gun,flame_thrower,magnetic_pulse])
        robot_2.equip_robot([eye_beams,laser_cannon,missle])
        robot_3.equip_robot([plasma_sword,sonic_blast,gamma_ray])
        print('---- Robots Armed ----')

        print(f'****Forming {self.alpha_squad.name}****')
        self.alpha_squad.create_fleet(robot_1)
        self.alpha_squad.create_fleet(robot_2)
        self.alpha_squad.create_fleet(robot_3)
        print(f'****{self.alpha_squad.name} Assembled****')
        print(f'---- ROBOTS READY FOR BATTLE ----\n\n')

        
    def setup_the_dinosaurs(self):
            tail_whip = Weapon('Tail Whip',20,5)
            charge = Weapon('Charge',25,5)
            roar = Weapon('Roar',30,5)

            stomp = Weapon('Stomp',30,15)
            bite = Weapon('Bite',40,20)
            razor_claws = Weapon('Razor Claws',50,25)
            
            horn = Weapon('Horn',40,35)
            tail_club = Weapon('Tail Club',50,45)
            chomp = Weapon('Chomp',60,55)
            
            print('---- Awakening Dinosaurs ----')
            dino_1 = Dinosaur('Triceratops',250,10,100)
            dino_2 = Dinosaur('Ankylosaurus',275,20,150)
            dino_3 = Dinosaur('Tyrannosaurus',350,40,200)
            print('---- Dinosaurs Alert ----')

            print('---- Dinosaur Attack Modes  ----')
            dino_1.dino_attack([tail_whip,stomp,horn])
            dino_2.dino_attack([charge,bite,tail_club])
            dino_3.dino_attack([roar,razor_claws,chomp])
            print('---- Dinosaurs Ready to Hunt ----')

            print(f'****Gathering {self.jungle_swarm.name}****')
            self.jungle_swarm.create_herd(dino_1)
            self.jungle_swarm.create_herd(dino_2)
            self.jungle_swarm.create_herd(dino_3)
            print(f'****{self.jungle_swarm.name} is on the Prowl****')
            print(f'---- DINOSAURS READY FOR BATTLE ----\n\n')



