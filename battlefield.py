
from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
import random

def get_valid_integer(message,number_range):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        user_input = int(input(message))
        if user_input not in number_range:
            print(f'Please enter an integer 1-{number_range[-1]}')
        else:
            waiting_for_valid_response = False
    return user_input


def get_y_or_n_from_user(input_message):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        user_input = (input(input_message)).upper()  
        if user_input == 'Y' or user_input == 'N':
            waiting_for_valid_response = False
        elif user_input == 'YES':
            user_input = 'Y'
            waiting_for_valid_response = False
        elif user_input == 'NO':
            user_input = 'N'
            waiting_for_valid_response = False
        else:
            print(f'You entered {user_input}')    
            print('Your response must be either a y (Yes) or n (No)')  
    return user_input


class Battlefield:
    def __init__(self) -> None:
        self.jungle_swarm = Herd('Jungle Swarm')
        self.alpha_squad = Fleet("Alpha Squad")
        self.round_number = 0
        
    
    def run_game(self):
        self.display_welcome()
        self.setup_the_robots()
        
        self.setup_the_dinosaurs()
        self.battle()

    def display_welcome(self):
        print("""
The rapid and uncontrolled advancement of genetics research led to the rebirth of savage dinsosaurs which quickly
evolved and swarmed the Earth. In response, DARPA created an advanced line of Robot Marines equipped with devastating
weapons and artificIal intelligence to defend the Earth. The self-aware robots identified humans to be their primary threat
and exterminated all civilization. AI Robots and Genetically Programed Dinosaurs now battle for control of the planet.\n
Welcome to the year 2205\n ______________________________________________\n""" )

    def battle(self):
        print("----Let's get ready to Rumble!!!!!----\n Robots vs Dinosaurs!")
        while self.jungle_swarm.number_of_dinosaurs_alive > 0 and self.alpha_squad.number_of_robots_alive > 0:
            self.round_number += 1
            self.game_round()

    def game_round(self):
        print(f"----Start of Round {self.round_number}----")
        self.setup_round()
        turn_number = 0
        while self.alpha_squad.number_of_robots_can_attack_this_round > 0 or self.jungle_swarm.number_of_dinosaurs_can_attack_this_round > 0:
            turn_number = self.game_turn(turn_number)

    def setup_round(self):
        self.alpha_squad.reset_robot_can_attack()
        print('----Robot status summary----')
        for robot in self.alpha_squad.robot_list:
            robot.recharge_energy()
            robot.list_status()
        self.jungle_swarm.reset_dinosaur_can_attack()
        print('----Dinosaur status summary----')
        for dinosaur in self.jungle_swarm.dinosaur_list:
            dinosaur.recover_endurance()
            dinosaur.list_status()
        return
        
    def game_turn(self,turn_num):
        turn_num += 1
        print(f'Round: {self.round_number} Turn: {turn_num}')
        attacker = self.determine_who_attacks()
        if attacker == 'Robots':
            self.robots_turn()
        elif attacker == 'Dinosaurs':
            self.dinosaurs_turn()
        else:
            pass


        return turn_num


        return turn

    def determine_who_attacks(self):
        attack_list = ['Robots','Dinosaurs']
        if self.alpha_squad.number_of_robots_can_attack_this_round < 1:
            attacker = 'Dinosaurs'
        elif self.jungle_swarm.number_of_dinosaurs_can_attack_this_round < 1:
            attacker = 'Robots'
        else:
            attacker = random.choice(attack_list)
        return attacker


    def dinosaurs_turn(self):
        print('----Dinosaur Attack----')
        index = 0
        dino_index = 0
        dinosaur_index_list = []
        for dinosaur in self.jungle_swarm.dinosaur_list:
            if dinosaur.can_attack_this_round:
                dinosaur_index_list.append(dino_index)
                index += 1
                dinosaur.make_dinosaur_selection_list(index)
            dino_index += 1
        user_selection = get_valid_integer(f'Select the attacking dinosaur (Pick 1 - {index}): ',range(1,index+1))
        print(f'You have selected Dinosaur #{user_selection}: {self.jungle_swarm.dinosaur_list[dinosaur_index_list[user_selection-1]].name}')
        dino_attack_index = dinosaur_index_list[user_selection-1]
        
        index = 0
        robot_index = 0
        robot_index_list = []
        for robot in self.alpha_squad.robot_list:
            if robot.is_operational:
                robot_index_list.append(robot_index)
                index += 1
                robot.which_robot_to_attack(index)
            robot_index += 1
        user_selection = get_valid_integer(f'Pick which Robot to strike (Pick 1 - {index}): ',range(1,index+1))
        print(f'You have selected Robot #{user_selection}: {self.alpha_squad.robot_list[robot_index_list[user_selection-1]].name}')
        robot_to_be_attacked_index = robot_index_list[user_selection-1]
       
        index = 0
        attack_index = 0
        attack_index_list = []
        for attack_type in self.jungle_swarm.dinosaur_list[dino_attack_index].attack_type:
            if attack_type.attack_cost < self.jungle_swarm.dinosaur_list[dino_attack_index].endurance:
                attack_index_list.append(attack_index)
                index += 1
                self.jungle_swarm.dinosaur_list[dino_attack_index].make_dinosaur_attack_list(index,attack_index)
            attack_index += 1
        user_selection = get_valid_integer(f'Pick which attack to use (Pick 1 - {index}): ',range(1,index+1))
        print(f'You have selected attack #{user_selection}: {self.jungle_swarm.dinosaur_list[dino_attack_index].attack_type[attack_index_list[user_selection - 1]].name}')
        attack_to_use_index = attack_index_list[user_selection - 1]
        self.dinosaur_attack(dino_attack_index,robot_to_be_attacked_index,attack_to_use_index)

        

    def attack_result(self):
        result_of_attack = random.choice(['Big Miss','Miss','Glancing Blow','Average Hit','Solid Hit','Critical Hit','Devastating Blow'])
        print(f'Result of attack is.....{result_of_attack}')
        if result_of_attack == 'Big Miss':
            damage_factor = -0.25
        elif result_of_attack == 'Miss':
            damage_factor = 0
        elif result_of_attack == 'Glancing Blow':
            damage_factor = 0.2
        elif result_of_attack == 'Average Hit':
            damage_factor = 0.5
        elif result_of_attack == 'Solid Hit':
            damage_factor = 0.75
        elif result_of_attack == 'Critical Hit':
            damage_factor = 1.0
        else:
            damage_factor = 1.25
        
        return damage_factor


    def dinosaur_attack(self,dino_num,robot_num,attack_num):
        damage_modifier = self.attack_result()
        attack_damage = round(self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].attack_power * damage_modifier)
        if damage_modifier < 0:
            print('Your dinosaur missed so bad it hurt itself')
            print(f'It caused {-attack_damage} health itself')
        else:
            if self.alpha_squad.robot_list[robot_num].shield_level < 1:
                print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has damaged {self.alpha_squad.robot_list[robot_num].name} health by {attack_damage} points')
                self.alpha_squad.robot_list[robot_num].health -= attack_damage
            else:
                if self.alpha_squad.robot_list[robot_num].shield_level > attack_damage:
                    print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has damaged {self.alpha_squad.robot_list[robot_num].name} shield by {attack_damage} points')
                    self.alpha_squad.robot_list[robot_num].shield_level -= attack_damage
                elif self.alpha_squad.robot_list[robot_num].shield_level == attack_damage:
                    print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has destroyed {self.alpha_squad.robot_list[robot_num].name} shield')
                    self.alpha_squad.robot_list[robot_num].shield_level -= attack_damage
                else:
                    attack_damage -= self.alpha_squad.robot_list[robot_num].shield_level
                    print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has destroyed {self.alpha_squad.robot_list[robot_num].name} shield and caused {attack_damage} to the robots health')
                    self.alpha_squad.robot_list[robot_num].health -= attack_damage
        self.jungle_swarm.dinosaur_list[dino_num].can_attack_this_round = False
        self.jungle_swarm.number_of_dinosaurs_can_attack_this_round -= 1
        self.jungle_swarm.dinosaur_list[dino_num].endurance -= self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].attack_cost
        if self.alpha_squad.robot_list[robot_num].health < 0:
            print(f'{self.alpha_squad.robot_list[robot_num].name} has been terminated')
            self.alpha_squad.robot_list[robot_num].can_attack_this_round = False
            self.alpha_squad.robot_list[robot_num].is_operational = False
        
        if self.jungle_swarm.dinosaur_list[dino_num].health < 0:
            print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has been died')
            self.jungle_swarm.dinosaur_list[dino_num].is_alive = False
        return
        
        




    def robots_turn(self):
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
        robot_1 = Robot('T-800',200,75,100,5)
        robot_1.list_status()
        robot_2 = Robot('T-1000',150,150,150,10)
        robot_2.list_status()
        robot_3 = Robot('T-X',200,200,200,20)
        robot_3.list_status()
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
        print(f'---- ROBOTS READY FOR BATTLE ----\n')

        
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
            dino_1 = Dinosaur('Triceratops',250,10,100,10)
            dino_1.list_status()
            dino_2 = Dinosaur('Ankylosaurus',275,20,150,15)
            dino_2.list_status()
            dino_3 = Dinosaur('Tyrannosaurus',350,40,200,20)
            dino_3.list_status()
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
            print(f'---- DINOSAURS READY FOR BATTLE ----\n')



