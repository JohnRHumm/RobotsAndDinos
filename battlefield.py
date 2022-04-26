from numpy import int64
from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
import random
from validate_input import get_valid_integer
from gameplay import attack_result
import time
import os
import string
if os.name == 'nt':
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11),7)

class Battlefield:
    def __init__(self) -> None:
        self.jungle_swarm = Herd('Jungle Swarm')
        self.alpha_squad = Fleet("Alpha Squad")
        self.round_number = 0
        self.combatants_on_each_side = 0
      
   # This function controls the sequence of the game
    def run_game(self):
        os.system('cls')
        self.display_welcome()
        time.sleep(5)
        self.number_of_combatants()
        self.setup_the_robots()
        time.sleep(5)
        self.setup_the_dinosaurs()
        time.sleep(5)
        self.user_picks_side()
        time.sleep(5)
        self.battle()
        time.sleep(5)
        self.display_winners()

    # Step 1
    def display_welcome(self):
        print("""
The rapid and uncontrolled advancement of genetics research led to the rebirth of savage dinsosaurs which quickly
evolved and swarmed the Earth. In response, DARPA created an advanced line of Robot Marines equipped with devastating
weapons and artificIal intelligence to defend the Earth. The self-aware robots identified humans to be their primary threat
and exterminated all civilization. AI Robots and Genetically Programed Dinosaurs now battle for control of the planet.\n
Welcome to the year 2205 \33[0;0m \n ******************************************************************************************** """)

    # Step 2: Ask user for the number of combatants
    def number_of_combatants(self):
        message_display = ('Pick the number of combatants you want on each side')
        upper_limit = 100
        user_selection = get_valid_integer(f'{message_display} (Pick 1 - {upper_limit}): ',range(1,upper_limit+1),True)
        self.combatants_on_each_side = user_selection
        return

    # Step 3: Define robots, weapons, arm robots, and put into Fleet--> alpha_squad
    def setup_the_robots(self):
         weapon_group_1 = ['Laser Gun','Eye Beams','Plasma Sword']
         weapon_group_2 = ['Flame Thrower','Laser Cannon','Sonic Blast']
         weapon_group_3  = ['Magnetic Pulse','Guided Missle','Gamma Ray']        
         for index in range(self.combatants_on_each_side):
             random_name = (f'Robo-{random.choice(range(1,100))}-{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}-{random.choice(range(1,100))}')
             attack_1 = Weapon(random.choice(weapon_group_1),random.choice(range(15,251)),5)
             attack_2 = Weapon(random.choice(weapon_group_2),random.choice(range(30,501)),15)
             attack_3 = Weapon(random.choice(weapon_group_3),random.choice(range(50,1001)),30)
             health = random.choice(range(50,1501))
             shield = random.choice(range(50,1201))
             energy = random.choice(range(100,1001))
             recharge = random.choice(range(5,101))
             robo = Robot(random_name,health,shield,energy,recharge)
             robo.list_status()
             robo.equip_robot([attack_1,attack_2,attack_3])
             self.alpha_squad.create_fleet(robo)
         self.alpha_squad.calc_fleet_health()
         self.alpha_squad.max_fleet_health = self.alpha_squad.fleet_health
         print(f'****{self.alpha_squad.name} Assembled****')
         print(f'\033[1;37;44m---- ROBOTS READY FOR BATTLE ----\033[0m \n')
        
 
     # Step 4: Define dinos, type of attacks, assign attack modes to dino, and put into Herd--> jungle_swarm
    def setup_the_dinosaurs(self):

         attack_group_1 = ['Tail Whip','Charge','Roar']
         attack_group_2 = ['Stomp','Bite','Razor Claws']
         attack_group_3  = ['Horn','Clubbed Tail','Chomp']        
        
         for index in range(self.combatants_on_each_side):
             random_name = (f'Dino-{random.choice(range(1,100))}-{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}-{random.choice(range(1,100))}')
             attack_1 = Weapon(random.choice(attack_group_1),random.choice(range(15,251)),5)
             attack_2 = Weapon(random.choice(attack_group_2),random.choice(range(30,501)),15)
             attack_3 = Weapon(random.choice(attack_group_3),random.choice(range(50,1251)),30)
             health = random.choice(range(100,2251))
             hide = random.choice(range(50,251))
             endurance = random.choice(range(100,1201))
             recovery = random.choice(range(5,151))
             dino = Dinosaur(random_name,health,hide,endurance,recovery)
             dino.list_status()
             dino.dino_attack([attack_1,attack_2,attack_3])
             self.jungle_swarm.create_herd(dino)
         self.jungle_swarm.calc_herd_health()
         self.jungle_swarm.max_herd_health = self.jungle_swarm.herd_health    
         print(f'****{self.jungle_swarm.name} is on the Prowl****')
         print(f'\033[1;37;42m---- DINOSAURS READY FOR BATTLE ---- \033[0m \n')
     
    # Step 5: User pics which side they want to play
    def user_picks_side(self):
        message = (f'Pick your Game Play Options')
        print('1: Play as dinosaurs computer is robots')
        print('2: Play as robots computer is dinosaurs')
        print('3: Play as dinosaurs and robots')
        print('4: Computer plays both sides')
        user_selection = get_valid_integer(f'{message} (Pick 1 - 4): ',range(1,5),True)

        if user_selection == 1:
            self.jungle_swarm.user_picks_options = True
            self.alpha_squad.user_picks_options = False
            print('You are the Dinosaurs')
        elif user_selection == 2:
            self.jungle_swarm.user_picks_options = False
            self.alpha_squad.user_picks_options = True
            print('You are the Robots')
        elif user_selection == 3:
            self.jungle_swarm.user_picks_options = True
            self.alpha_squad.user_picks_options = True
            print('You are playing boths sides. Guaranteed victory!')
        else:
            self.jungle_swarm.user_picks_options = False
            self.alpha_squad.user_picks_options = False
            print('Sit back and relax. Watch the computer duke it out!')
        

    # Step 6: A battle is made up of a round which contains several turns
    def battle(self):
        print("----Let's get ready to Rumble!!!!!----\n Robots vs Dinosaurs!")
        print(f'\033[1;37;44m Number of Robots: {self.alpha_squad.number_of_robots_alive} Overall Health: {self.alpha_squad.fleet_health} \033[0m')
        print(f'\033[1;37;42m Number of Dinosaurs: {self.jungle_swarm.number_of_dinosaurs_alive} Overall Health: {self.jungle_swarm.herd_health}\033[0m')
        while self.jungle_swarm.number_of_dinosaurs_alive > 0 and self.alpha_squad.number_of_robots_alive > 0:
            self.round_number += 1
            self.game_round()
        return

    # Step 7: Display the results of battle
    def display_winners(self):
        self.alpha_squad.calc_fleet_health()
        print('\033[1;37;44m ----Final Robot status summary---- \033[0m')
        print(f'Robots Operational: {self.alpha_squad.number_of_robots_alive} Overall Health: {self.alpha_squad.fleet_health}')
        for robot in self.alpha_squad.robot_list:
            if robot.is_operational:
                print(f'Name: {robot.name} Health: {robot.health} Shield: {robot.shield} Number of Kills: {robot.number_of_kills} Total Damage: {robot.damage_inflicted}')
            else:
                print(f'Name: {robot.name} was terminated by {robot.killed_by} and the killing blow was {robot.killed_with}')
            time.sleep(1)
        self.jungle_swarm.calc_herd_health()
        print('\033[1;37;42m----Final Dinosaur status summary---- \033[0m')
        print(f'Dinosaurs Alive: {self.jungle_swarm.number_of_dinosaurs_alive} Overall Health: {self.jungle_swarm.herd_health}')
        for dinosaur in self.jungle_swarm.dinosaur_list:
            if dinosaur.is_alive:
                print(f'Name: {dinosaur.name} Health: {dinosaur.health}  Number of Kills: {dinosaur.number_of_kills} Total Damage: {dinosaur.damage_inflicted}')
            else:
                print(f'Name: {dinosaur.name} was terminated by {dinosaur.killed_by} and with {dinosaur.killed_with}')
            time.sleep(1)
        if self.alpha_squad.number_of_robots_alive > 0:
            print('\033[1;37;44mThe robots have defeated the last of genetically altered dinosaurs!\033[0m')
            if self.alpha_squad.user_picks_options and not self.jungle_swarm.user_picks_options:
                print('CONGRATULATIONS!! YOU HAVE WON!')
            elif not self.alpha_squad.user_picks_options and self.jungle_swarm.user_picks_options:
                print('Sorry! You have lost')
            else:
                pass
            print("""
    As the remaining robots gather around the fallen dinosaurs, a long buried bit of python code
    within the robot AI activates a termination fail safe designed by the DARPA engineers.
    The robot's explode in huge fireballs, leaving the Earth silent and ending the 
    last great war of human civilization.""")

        if self.jungle_swarm.number_of_dinosaurs_alive > 0:
            print('\033[1;37;42mThe dinosaurs have defeated the last of robot marines!\033[0m')
            if self.jungle_swarm.user_picks_options and not self.alpha_squad.user_picks_options:
                print('CONGRATULATIONS!! YOU HAVE WON!')
            elif not self.jungle_swarm.user_picks_options and self.alpha_squad.user_picks_options:
                  print('Sorry! You have lost')
            else:
                pass
            print("""
    As the remaining dinosaurs gather around the burning robots, a fireball errupts in the sky from
    the upper edge of the atmosphere. As the genetically altered dinosaurs look up, they track 
    a rapidly moving asteroid that impacts the Earth in a gigantic explosion!!!""")
        
        print('\033[1;37;41m Game over. Thank you for playing \033[0m')

    # A round is the peiord containg all the dinosaur/robot attacks by each alive/operational dino/robot
    # Each dino/robot gets 1 attack per round unless it is killed before it attacks. Once either the number
    # of functioning robots or alive dinosaurs gets to 0, the loop stops
    def game_round(self):
        print(f"\33[0;31;47m----Start of Round {self.round_number}----\33[0m")
        time.sleep(3)
        self.setup_round()
        turn_number = 0
        while self.alpha_squad.number_of_robots_can_attack_this_round > 0 or self.jungle_swarm.number_of_dinosaurs_can_attack_this_round > 0:
            if self.alpha_squad.number_of_robots_alive < 1 or self.jungle_swarm.number_of_dinosaurs_alive < 1:
                return
            else:
                turn_number = self.game_turn(turn_number)

    # Recharges the energy (robots)/ endurance (dinosaurs) for each functioning member of the groups. Energy/endurance
    # determines which weapons/attack types are availible in a given round
    def setup_round(self):
        self.alpha_squad.reset_robot_can_attack()
        self.alpha_squad.calc_fleet_health()
        print('\033[1;37;44m ----Robot status summary---- \033[0m')
        print(f'Robots Operational: {self.alpha_squad.number_of_robots_alive} Overall Health: {self.alpha_squad.fleet_health}')
        for robot in self.alpha_squad.robot_list:
            robot.recharge_energy()
            robot.list_status()
            time.sleep(.25)
        self.jungle_swarm.reset_dinosaur_can_attack()
        self.jungle_swarm.calc_herd_health()
        print('\033[1;37;42m----Dinosaur status summary---- \033[0m')
        print(f'Dinosaurs Alive: {self.jungle_swarm.number_of_dinosaurs_alive} Overall Health: {self.jungle_swarm.herd_health}')
        for dinosaur in self.jungle_swarm.dinosaur_list:
            dinosaur.recover_endurance()
            dinosaur.list_status()
            time.sleep(.25)
        return
        
    # A turn is one attack seqeunce either robot or dinosaur.
    def game_turn(self,turn_num):
        turn_num += 1
        time.sleep(1)
        self.alpha_squad.calc_fleet_health()
        self.jungle_swarm.calc_herd_health()
        print(f'\033[1;37;46m Round: {self.round_number} Turn: {turn_num}\033[0m')
        print(f'\033[1;37;44m Robots: {self.alpha_squad.number_of_robots_alive} Overall Health: {int(100* self.alpha_squad.fleet_health/self.alpha_squad.max_fleet_health)}% \033[0m')
        print(f'\033[1;37;42m Dinosaurs: {self.jungle_swarm.number_of_dinosaurs_alive} Overall Health: {int(100* self.jungle_swarm.herd_health/self.jungle_swarm.max_herd_health)}% \033[0m')
        attacker = self.determine_who_attacks()
        if attacker == 'Robots':
            self.robots_turn()
        elif attacker == 'Dinosaurs':
            self.dinosaurs_turn()
        else:
            pass
        time.sleep(3)
        return turn_num

    # Randomly determine who can attack at the start of a turn. Note a dino/robot can
    # only attack once per turn which is controlled by the .can_attack_this_round variable
    # in the robot/dino Class
    def determine_who_attacks(self):
        attack_list = ['Robots','Dinosaurs']
        if self.alpha_squad.number_of_robots_can_attack_this_round < 1:
            attacker = 'Dinosaurs'
        elif self.jungle_swarm.number_of_dinosaurs_can_attack_this_round < 1:
            attacker = 'Robots'
        else:
            attacker = random.choice(attack_list)
        return attacker

    # Dinosaur attack turn. Get which dinosaur strikes, which robot to hit, and what attack style to use
    # from the user
    def dinosaurs_turn(self):
        print('\033[1;37;42m----Dinosaur Attack----\033[0m')
        dino_index = self.which_dino_from_list('Select the attacking dinosaur','attack')
        robot_index = self.which_robot_from_list('Pick which Robot to strike','defend')    
        attack_index = self.which_dino_attack_from_list(dino_index,'Select dinosaur attack')
        self.dinosaur_attack(dino_index,robot_index,attack_index)

    # Robt attack turn. Get which robot strikes, which dino to hit, and what weapon to use
    # from the user
    def robots_turn(self):
        print('\033[1;37;44m----Robot Attack----\033[0m')
        robot_index = self.which_robot_from_list('Select the attacking robot','attack')  
        dino_index = self.which_dino_from_list('Pick which dinosaur to strike','defend')
        weapon_index = self.which_robot_weapon_from_list(robot_index,'Select robot weapon')
        self.robot_attack(robot_index,dino_index,weapon_index)
 
    # Result of dino attack. Robots have shields which have to be destroyed before health can be damaged
    def dinosaur_attack(self,dino_num,robot_num,attack_num):
        damage_modifier = attack_result()
        attack_damage = round(self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].attack_power * damage_modifier)
        if damage_modifier < 0:
            print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} missed so bad it hurt itself')
            print(f'It caused {-attack_damage} health to itself')
            if (-attack_damage > self.jungle_swarm.dinosaur_list[dino_num].health):
                self.jungle_swarm.dinosaur_list[dino_num].health = 0
            else:    
                self.jungle_swarm.dinosaur_list[dino_num].health -= -attack_damage
            print(f'\033[1;37;42m{self.jungle_swarm.dinosaur_list[dino_num].name} has {self.jungle_swarm.dinosaur_list[dino_num].health} health remaining\033[0m')
        else:
            print(f'Dinosaur attack damage is: {attack_damage}')
            self.jungle_swarm.dinosaur_list[dino_num].damage_inflicted += attack_damage
            if self.alpha_squad.robot_list[robot_num].shield_level < 1:
                print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has damaged {self.alpha_squad.robot_list[robot_num].name} health by {attack_damage} points')
                self.alpha_squad.robot_list[robot_num].health -= attack_damage
                if self.alpha_squad.robot_list[robot_num].health < 1:
                    self.alpha_squad.robot_list[robot_num].health = 0
                health_percentage = round((self.alpha_squad.robot_list[robot_num].health/self.alpha_squad.robot_list[robot_num].max_health) * 100)
                print(f'\033[1;37;44m{self.alpha_squad.robot_list[robot_num].name} has {self.alpha_squad.robot_list[robot_num].health} health reamining ({health_percentage}%)\033[0m')
            else:
                if self.alpha_squad.robot_list[robot_num].shield_level > attack_damage:
                    print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has damaged {self.alpha_squad.robot_list[robot_num].name} shield by {attack_damage} points')
                    self.alpha_squad.robot_list[robot_num].shield_level -= attack_damage
                    shield_percentage = round((self.alpha_squad.robot_list[robot_num].shield_level/self.alpha_squad.robot_list[robot_num].max_shield_level) * 100)
                    print(f'\033[1;37;44m{self.alpha_squad.robot_list[robot_num].name} has {self.alpha_squad.robot_list[robot_num].shield_level} shield reamining ({shield_percentage}%)\033[0m')
                elif self.alpha_squad.robot_list[robot_num].shield_level == attack_damage:
                    print(f'\033[1;37;44m{self.jungle_swarm.dinosaur_list[dino_num].name} has destroyed {self.alpha_squad.robot_list[robot_num].name} shield\033[0m')
                    self.alpha_squad.robot_list[robot_num].shield_level -= attack_damage
                else:
                    attack_damage -= self.alpha_squad.robot_list[robot_num].shield_level
                    print(f'{self.jungle_swarm.dinosaur_list[dino_num].name} has destroyed {self.alpha_squad.robot_list[robot_num].name} shield and caused {attack_damage} to the robots health')
                    self.alpha_squad.robot_list[robot_num].health -= attack_damage
                    if self.alpha_squad.robot_list[robot_num].health < 1:
                        self.alpha_squad.robot_list[robot_num].health = 0
                    self.alpha_squad.robot_list[robot_num].shield_level = 0
                    health_percentage = round((self.alpha_squad.robot_list[robot_num].health/self.alpha_squad.robot_list[robot_num].max_health) * 100)
                    print(f'\033[1;37;44m{self.alpha_squad.robot_list[robot_num].name} has {self.alpha_squad.robot_list[robot_num].health} health reamining ({health_percentage}%)\033[0m')
        self.jungle_swarm.dinosaur_list[dino_num].can_attack_this_round = False
        self.jungle_swarm.number_of_dinosaurs_can_attack_this_round -= 1
        self.jungle_swarm.dinosaur_list[dino_num].endurance -= self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].attack_cost
        if self.alpha_squad.robot_list[robot_num].health < 1:
            print(f'\33[1;37;41m {self.alpha_squad.robot_list[robot_num].name} has been terminated \33[0m')
            if self.alpha_squad.robot_list[robot_num].can_attack_this_round:
                self.alpha_squad.number_of_robots_can_attack_this_round -= 1
            self.alpha_squad.robot_list[robot_num].can_attack_this_round = False
            self.alpha_squad.robot_list[robot_num].is_operational = False
            self.alpha_squad.number_of_robots_alive -= 1
            self.alpha_squad.robot_list[robot_num].killed_by = self.jungle_swarm.dinosaur_list[dino_num].name
            self.alpha_squad.robot_list[robot_num].killed_with = self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].name
            self.jungle_swarm.dinosaur_list[dino_num].number_of_kills +=1
        
        if self.jungle_swarm.dinosaur_list[dino_num].health < 1:
            print(f'\33[1;37;41m {self.jungle_swarm.dinosaur_list[dino_num].name} has been died \33[0m')
            self.jungle_swarm.dinosaur_list[dino_num].is_alive = False
            self.jungle_swarm.number_of_dinosaurs_alive -= 1
            self.jungle_swarm.dinosaur_list[dino_num].killed_by = 'Self'
            self.jungle_swarm.dinosaur_list[dino_num].killed_with = self.jungle_swarm.dinosaur_list[dino_num].attack_type[attack_num].name

        print('')
        time.sleep(1)
        return
    
    # Result of robo attack. Dinosaurs have hide ratings, which unlike shields are not destroyed but instead take a fixed
    # amount off each attack
    def robot_attack(self,robot_num,dino_num,weapon_num):
        damage_modifier = attack_result()
        attack_damage = round(self.alpha_squad.robot_list[robot_num].weapons_list[weapon_num].attack_power * damage_modifier)
        if damage_modifier < 0:
            print(f'Robot {self.alpha_squad.robot_list[robot_num].name} missed so bad it hurt itself')
            print(f'It caused {-attack_damage} health to itself')
            if -attack_damage >  self.alpha_squad.robot_list[robot_num].health:
                 self.alpha_squad.robot_list[robot_num].health = 0
            else:     
                self.alpha_squad.robot_list[robot_num].health -= -attack_damage
            health_percentage = round((self.alpha_squad.robot_list[robot_num].health/self.alpha_squad.robot_list[robot_num].max_health) * 100)
            print(f'\033[1;37;44m{self.alpha_squad.robot_list[robot_num].name} has {self.alpha_squad.robot_list[robot_num].health} health reamining ({health_percentage}%)\033[0m')
        elif attack_damage <= self.jungle_swarm.dinosaur_list[dino_num].hide_strength:
            print("The robot's attack could not penetrate the dinosaur's tough skin\nNo damage was inflicted on the dinosaur")
            health_percentage = round((self.jungle_swarm.dinosaur_list[dino_num].health/self.jungle_swarm.dinosaur_list[dino_num].max_health) * 100)
            print(f'\033[1;37;42m Dinosaur {self.jungle_swarm.dinosaur_list[dino_num].name} has {self.jungle_swarm.dinosaur_list[dino_num].health} health remaining ({health_percentage}%)\033[0m')
        else:
            print(f"Robot attack damage is: {attack_damage} but the dinosaur's tough skin reduced the attack by {self.jungle_swarm.dinosaur_list[dino_num].hide_strength}")
            attack_damage -= self.jungle_swarm.dinosaur_list[dino_num].hide_strength
            self.alpha_squad.robot_list[robot_num].damage_inflicted += attack_damage
            self.jungle_swarm.dinosaur_list[dino_num].health -= attack_damage
            if self.jungle_swarm.dinosaur_list[dino_num].health < 1:
                self.jungle_swarm.dinosaur_list[dino_num].health = 0
            health_percentage = round((self.jungle_swarm.dinosaur_list[dino_num].health/self.jungle_swarm.dinosaur_list[dino_num].max_health) * 100)
            print(f'\033[1;37;42m {self.jungle_swarm.dinosaur_list[dino_num].name} has {self.jungle_swarm.dinosaur_list[dino_num].health} health reamining ({health_percentage}%)\033[0m')
        self.alpha_squad.robot_list[robot_num].can_attack_this_round = False
        self.alpha_squad.number_of_robots_can_attack_this_round -= 1
        self.alpha_squad.robot_list[robot_num].energy -= self.alpha_squad.robot_list[robot_num].weapons_list[weapon_num].attack_cost
        if self.jungle_swarm.dinosaur_list[dino_num].health < 1:
            print(f'\33[1;37;41m {self.jungle_swarm.dinosaur_list[dino_num].name} has been killed \33[0m')
            if self.jungle_swarm.dinosaur_list[dino_num].can_attack_this_round:
                self.jungle_swarm.number_of_dinosaurs_can_attack_this_round -= 1
            self.jungle_swarm.dinosaur_list[dino_num].can_attack_this_round = False
            self.jungle_swarm.dinosaur_list[dino_num].is_alive = False
            self.jungle_swarm.number_of_dinosaurs_alive -= 1
            self.jungle_swarm.dinosaur_list[dino_num].killed_by = self.alpha_squad.robot_list[robot_num].name
            self.jungle_swarm.dinosaur_list[dino_num].killed_with = self.alpha_squad.robot_list[robot_num].weapons_list[weapon_num].name
            self.alpha_squad.robot_list[robot_num].number_of_kills += 1
        
        if self.alpha_squad.robot_list[robot_num].health < 1:
            print(f'\33[1;37;41m {self.alpha_squad.robot_list[robot_num].name} has been terminated \33[0m')
            self.alpha_squad.robot_list[robot_num].is_operational = False
            self.alpha_squad.number_of_robots_alive -= 1
            self.alpha_squad.robot_list[robot_num].killed_by = 'Self'
            self.alpha_squad.robot_list[robot_num].killed_with = self.alpha_squad.robot_list[robot_num].weapons_list[weapon_num].name

        print('')
        time.sleep(1)
        return

    # Sets up user list for dinos. Depends if attack or defend. If attack only show dinos that can attack
    # in the round. If defend then only dinos left alive
    def which_dino_from_list(self,message,type_of_list):
        index = 0
        dinosaur_list = []
        for dinosaur in self.jungle_swarm.dinosaur_list:
            if type_of_list == 'attack':
                list_condition = dinosaur.can_attack_this_round
            else:
                list_condition = dinosaur.is_alive
            if list_condition:
                dinosaur_list.append(dinosaur)
                index += 1
                print(f'    {index}: Dinosaur: {dinosaur.name} --> Health: {dinosaur.health} Hide Strength: {dinosaur.hide_strength} Endurance: {dinosaur.endurance} ')
        if type_of_list == 'attack':
            user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.jungle_swarm.user_picks_options)
        else:
            user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.alpha_squad.user_picks_options)
        print(f'You have selected Dinosaur #{user_selection}: {dinosaur_list[user_selection-1].name}')
        selected_dino = dinosaur_list[user_selection-1]
        dino_index =  self.jungle_swarm.dinosaur_list.index(selected_dino)
        return dino_index
    
    # Sets up user list for dino attacks. 
    def which_dino_attack_from_list(self,dino_index,message):
        index = 0
        attack_list = []
        for attack_type in self.jungle_swarm.dinosaur_list[dino_index].attack_type:
            if attack_type.attack_cost < self.jungle_swarm.dinosaur_list[dino_index].endurance:
                attack_list.append(attack_type)
                index += 1
                print(f'    {index}: Attack: {attack_type.name} Damage Rating: {attack_type.attack_power} Endurance Cost: {attack_type.attack_cost}')
        user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.jungle_swarm.user_picks_options)
        print(f'You have selected attack #{user_selection}: {attack_list[user_selection-1].name}')
        selected_attack = attack_list[user_selection-1]
        attack_index = self.jungle_swarm.dinosaur_list[dino_index].attack_type.index(selected_attack)
        return attack_index
    
    # Sets up user list for robots. Depends if attack or defend. If attack only show robots that can attack
    # in the round. If defend then only robots left in operation
    def which_robot_from_list(self,message,type_of_list):
        index = 0
        robot_list = []
        for robot in self.alpha_squad.robot_list:
            if type_of_list == 'attack':
                list_condition = robot.can_attack_this_round
            else:
                list_condition = robot.is_operational
            if list_condition:
                robot_list.append(robot)
                index += 1
                print(f'    {index}: Robot: {robot.name} --> Health: {robot.health} Shield: {robot.shield_level} Energy: {robot.energy}')
        if type_of_list == 'attack':
            user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.alpha_squad.user_picks_options)
        else:
            user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.jungle_swarm.user_picks_options)
        print(f'You have selected Robot #{user_selection}: {robot_list[user_selection-1].name}')
        selected_robot = robot_list[user_selection-1]
        robot_index =  self.alpha_squad.robot_list.index(selected_robot)
        return robot_index
        
    # Sets up user list for robot weapon
    def which_robot_weapon_from_list(self,robot_index,message):
        index = 0
        weapon_list = []
        for weapon in self.alpha_squad.robot_list[robot_index].weapons_list:
            if weapon.attack_cost < self.alpha_squad.robot_list[robot_index].energy:
                weapon_list.append(weapon)
                index += 1
                print(f'    {index}: Attack: {weapon.name} Damage Rating: {weapon.attack_power} Endurance Cost: {weapon.attack_cost}')
        user_selection = get_valid_integer(f'{message} (Pick 1 - {index}): ',range(1,index+1),self.alpha_squad.user_picks_options)
        print(f'You have selected weapon #{user_selection}: {weapon_list[user_selection-1].name}')
        selected_weapon = weapon_list[user_selection-1]
        weapon_index = self.alpha_squad.robot_list[robot_index].weapons_list.index(selected_weapon)
        return weapon_index
   
    
    
    

   

