class Herd():
    def __init__(self,name) -> None:
        self.name = name
        self.dinosaur_list = []
        self.number_of_dinosaurs_alive = 0
 
    def create_herd(self,dinosaur):
        self.dinosaur_list.append(dinosaur)
        self.number_of_dinosaurs_alive += 1
        print(f'    {dinosaur.name} has been added to {self.name}')

    def dinosaurss_left_alive(self):
        alive_dinosaurs = []
        for dinosaur in self.dinosaurs:
            if dinosaur.is_alive:
                alive_dinosaurs.append(dinosaur)
        return alive_dinosaurs

    def dinosaurs_that_can_attack_this_round(self,dinosaur_list):
        dinosaur_attack_list = []
        for dinosaur in dinosaur_list:
            if dinosaur.can_attack_this_round:
                dinosaur_attack_list.append(dinosaur)
        return dinosaur_attack_list
