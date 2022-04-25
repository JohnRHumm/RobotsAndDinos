# RobotsAndDinos

Created Dinosaur class to hold dinosaur infomration including health, hide strength, and endurance
    Health is the amount of damage a dinosaur can take before dying
    Hide Strength reduces the amount of damage inflicted by opponent due to the dino's thick skin
    Endurance determines what kinds of attack a dinosaur can use in a given round every attack depletes endurance
    Endurance recovery rate is the amount of endurance recovered each round

Created Robot class to hold robot infomration including health, shield, and energy
    Health is the amount of damage a robot can take before being terminated
    Shield protects the robot and must be destroyed before Health can be redueced
    Energy determines what kinds of attack a robot can use in a given round every weapon depletes energy
    Engergy recovery rate is the amount of energy recovered each round

Created Weapon class to hold information on robot weapons and dinosaur attacks
    attack_power is the base damage rating
    attack_cost is the amount of endurance or power is costs to use the attack/weapon

Created Herd class to store a group of Dinosaurs

Created Fleet class to store a group of Robots

Created Battlefield class which is the main gameflow
    User selects which side they want to play (or both or computer automated)
    Game consists of turns which are defined as all attacks by alive dinosaurs and functioning robots
    Each turn consists of several rounds where a round is an individual attack by dinosaur or robot 
        there can be at most 6 turns per round (3 robots and 3 dinosaurs at the start of the game).
        When robots or dinosaurs are eliminated they can no longer attack and the number of turns decrease
    The order of attack is randomly determined each round, however only one attack per dinosaur/robot is permited
        per turn. 
    A turn consists of selecting the attacking dino/robot, which dino/robot to be attacked and the method of attack/weapon
        The severity of attack is randomly generated and returns a scalar value that depends on the severity of the hit
        This attack severity factor is multiplied by the base damage rating of the method of attack/weapon to yield
        an attack damage value
    For dinosaurs the attack damage value is reduced by their hide rating and result is subtracted from health. 
        Robot attacks less than the hide rating do no damage
    For robots the attack damage value is first applied to shield until destoryed and then to health
    Once a dinosaur/robot health is below 1, it is eliminated from play and can no longer attack
    Play continues until one side is eliminated
    Computer controlled sides randomly selects the attacker which opponent to attack and the attack style/weapon

gampeplay.py contains the result_of_attack method to randomly determine the severity attack. It returns the damage 
    severity multiplier

validate_input.py contains the validate_integer method which limits the user input to only the range of valid 
    integers for each selection. Helps to minimize the potential for software crashes. Also contains a boolean 
    which randomly selects choice. If the user_select_option is set to False it will randomly return an integer.
    This option is used when the computer controls a side 

main.py starts the game