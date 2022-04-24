class Herd():
    def __init__(self,name) -> None:
        self.name = name
        self.dinosaur_list = []
        self.number_of_dinosaurs_alive = 0
        self.number_of_dinosaurs_can_attack_this_round = 0
 
    def create_herd(self,dinosaur):
        self.dinosaur_list.append(dinosaur)
        self.number_of_dinosaurs_alive += 1
        print(f'    {dinosaur.name} has been added to {self.name}')

    def dinosaurss_left_alive(self):
        alive_dinosaurs = []
        for dinosaur in self.dinosaur_list:
            if dinosaur.is_alive:
                alive_dinosaurs.append(dinosaur)
        return alive_dinosaurs

    def reset_dinosaur_can_attack(self):
        for dinosaur in self.dinosaur_list:
            if dinosaur.is_alive:
                dinosaur.can_attack_this_round = True
                self.number_of_dinosaurs_can_attack_this_round += 1

    

