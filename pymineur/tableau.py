
from pymineur.case import Case
import random


class Tableau:

    def __init__(self):

        self.dimension_y = input("Combien de rangées voulez-vous? (5 par défaut)")

        self.dimension_x = input("Combien de colonnes voulez-vous? (5 par défaut)")

        self.nombre_mines = input("Combien de mines voulez-vous? (5 par défaut)")
        while not int(self.nombre_mines) in range(int(self.dimension_x) * int(self.dimension_y)):
            print("Ce nombre de mines est invalide.")
            self.nombre_mines = input("Combien de mines voulez-vous? (5 par défaut)")

        self.dimension_x = int(self.dimension_x)
        self.dimension_y = int(self.dimension_y)
        self.nombre_mines = int(self.nombre_mines)

        self.nombre_cases_sans_mine_a_devoiler = self.dimension_y * self.dimension_x - self.nombre_mines

        # Le dictionnaire de case, vide au départ, qui est rempli par la fonction initialiser_tableau().
        self.dictionnaire_cases = {}
        self.liste_cases_minees = []

        self.initialiser_tableau()

    def initialiser_tableau(self):
        y = 1
        x = 1
        while y in range(self.dimension_y + 1):
            while x in range(self.dimension_x + 1):
                self.dictionnaire_cases[x, y] = Case()
                x += 1
            x = 1
            y += 1

        mines_placees = 0
        while mines_placees != self.nombre_mines:
            y = random.randint(1, self.dimension_y)
            x = random.randint(1, self.dimension_x)
            if (x, y) in self.liste_cases_minees:
                continue
            else:
                self.liste_cases_minees += (x, y)
                self.dictionnaire_cases[(x, y)].ajouter_mine()
                cases_voisines = self.obtenir_voisins(x, y)
                for case in cases_voisines:
                    if case in self.dictionnaire_cases:
                        self.dictionnaire_cases[case].ajouter_une_mine_voisine()
                mines_placees += 1

    def obtenir_voisins(self, coord_x, coord_y):
        voisinage = ((coord_x - 1, coord_y - 1), (coord_x -1, coord_y), (coord_x - 1, coord_y + 1),
                     (coord_x, coord_y - 1),           (coord_x, coord_y + 1),
                     (coord_x + 1, coord_y - 1),  (coord_x + 1, coord_y),  (coord_x + 1, coord_y + 1))
        liste_coordonnees_cases_voisines = list(voisinage)
        for (x, y) in list(voisinage):
            if not self.valider_coordonnees(x, y):
                liste_coordonnees_cases_voisines.remove((x, y))

        return liste_coordonnees_cases_voisines

    def valider_coordonnees(self, coord_x, coord_y):
        if coord_x in range(self.dimension_x + 1):
            if coord_y in range(self.dimension_y + 1):
                if coord_x < 1 or coord_y < 1:
                    return False
                else:
                    return True
            return False
        return False

    def valider_coordonnees_a_devoiler(self, coord_x, coord_y):
        return coord_x in (1, self.dimension_x) and coord_y in (1, self.dimension_y) and \
               Case.est_a_devoiler == True

    def afficher_solution(self):
        for x in range(self.dimension_x + 1):
            if x == 0:
                for y in range(self.dimension_y + 1):
                    if y == 0:
                        print("  ", end=" ")
                    else:
                        print("{0:2d} ".format(y), end="")
                print("\n")
            else:
                for y in range(self.dimension_y + 1):
                    if y == 0:
                        print("{0:2d} ".format(x), end=" ")
                    else:
                        if self.dictionnaire_cases[(x, y)].contient_mine():
                            print("B ", end= " ")
                        else :
                            print(self.dictionnaire_cases[(x, y)].obtenir_nombre_mines_voisines(), end="  ")

                print("\n")

    def afficher_tableau(self):
        for x in range(self.dimension_x + 1):
            if x == 0:
                for y in range(self.dimension_y + 1):
                    if y == 0:
                        print("  ", end=" ")
                    else:
                        print("{0:2d} ".format(y), end="")
                print("\n")
            else:
                for y in range(self.dimension_y + 1):
                    if y == 0:
                        print("{0:2d} ".format(x), end=" ")
                    else:
                        if self.dictionnaire_cases[(x, y)].est_a_devoiler():
                            print("_ ", end= " ")
                        else:
                            if not self.dictionnaire_cases[(x, y)].contient_mine():
                                print(self.dictionnaire_cases[(x, y)].obtenir_nombre_mines_voisines(), end="  ")
                            else:
                                print("B", end="  ")

                print("\n")

    def contient_cases_a_devoiler(self):
        if self.nombre_cases_sans_mine_a_devoiler == 0:
            return False
        else:
            return True

    def devoiler_case(self, coord_x, coord_y):
        if not self.dictionnaire_cases[(coord_x, coord_y)].contient_mine:
            pass
        else:
            if self.dictionnaire_cases[(coord_x, coord_y)].est_a_devoiler():
                self.dictionnaire_cases[(coord_x, coord_y)].devoiler()
                self.nombre_cases_sans_mine_a_devoiler -= 1
                if self.dictionnaire_cases[(coord_x, coord_y)].obtenir_nombre_mines_voisines() == 0:
                    voisins = self.obtenir_voisins(coord_x, coord_y)
                    for c, (x, y) in enumerate(voisins):
                        self.devoiler_case(x, y)

    def case_contient_mine(self, coord_x, coord_y):
        if self.dictionnaire_cases[coord_x, coord_y].contient_mine():
            return True
        else:
            return False


if __name__ == '__main__':

    # Ce bout de code est là pour vous aider à tester votre première tentative d'implémentation du tableau. Vous
    # pouvez l'utiliser en exécutant le fichier tableau.py. N'oubliez pas toutefois que l'exécution principale
    # du programme devra se faire avec pymineur.__main__.py

    tableau_test = Tableau()

    tableau_test.afficher_tableau()
    tableau_test.afficher_solution()