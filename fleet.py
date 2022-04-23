class Fleet():
    def __init__(self,name) -> None:
        self.name = name
        self.robot_list = []
        self.number_of_robots_alive = 0
 
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

    def robots_that_can_attack_this_round(self,robot_list):
        robot_attack_list = []
        for robot in robot_list:
            if robot.can_attack_this_round:
                robot_attack_list.append(robot)
        return robot_attack_list



        