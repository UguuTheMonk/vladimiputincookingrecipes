
class Case:

    def __init__(self):
        self.est_minee = False
        self.est_devoilee = False
        self.nombre_mines_voisines = 0

    def devoiler(self):
        self.est_devoilee = True

    def ajouter_mine(self):
        self.est_minee = True

    def contient_mine(self):
        return self.est_minee

    def est_a_devoiler(self):
        return not self.est_devoilee

    def ajouter_une_mine_voisine(self):
        self.nombre_mines_voisines += 1

    def obtenir_nombre_mines_voisines(self):
        return self.nombre_mines_voisines

    def est_voisine_d_une_mine(self):
        if self.nombre_mines_voisines == 0:
            return False
        else:
            return True
