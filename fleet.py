class Fleet():
    def __init__(self,name) -> None:
        self.name = name
        self.robot_list = []
        self.number_of_robots_alive = 0
        self.number_of_robots_can_attack_this_round = 0
        self.user_picks_options = True
 
    def create_fleet(self,robot):
        self.robot_list.append(robot)
        self.number_of_robots_alive += 1
        print(f'    {robot.name} has been added to {self.name}')

    def robots_left_in_operation(self):
        functioning_robots = []
        for robot in self.robot_list:
            if robot.is_operational:
                functioning_robots.append(robot)
        return functioning_robots

    def reset_robot_can_attack(self):
        for robot in self.robot_list:
            if robot.is_operational:
                robot.can_attack_this_round = True
                self.number_of_robots_can_attack_this_round +=1

    




        