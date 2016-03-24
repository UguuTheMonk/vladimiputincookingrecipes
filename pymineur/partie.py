
from pymineur.tableau import Tableau


class Partie:

    def __init__(self):
        print("""
                 _______________.___.  _____  .___ _______  _______________ _____________.__.
                 \______   \__  |   | /     \ |   |\      \ \_   _____/    |   \______   \  |
                  |     ___//   |   |/  \ /  \|   |/   |   \ |    __)_|    |   /|       _/  |
                  |    |    \____   |    Y    \   |    |    \|        \    |  / |    |   \  |
                  |____|    / ______|____|__  /___|____|__  /_______  /______/  |____|_  /__|
                            \/              \/            \/        \/                 \/ \/
                                                                                    Par Samuel Parent
                                                                                        Hugues Le Moyne

                                            Bienvenue sur PyMineur!""")
        input("""                                        Appuyez sur ENTRÉE pour débuter!""")
        self.tableau_mines = Tableau()
        self.partie_terminee = False
        self.partie_gagnee = False

    def victoire(self):
        self.partie_terminee = True
        self.partie_gagnee = True

    def jouer(self):
        self.tableau_mines.afficher_tableau()
        while not self.partie_terminee:
            (coord_x, coord_y) = self.demander_coordonnees_case_a_devoiler()
            print((int(coord_x), int(coord_y)))
            self.tableau_mines.devoiler_case(int(coord_x), int(coord_y))
            if not self.tableau_mines.contient_cases_a_devoiler():
                self.victoire()
            else:
                self.tableau_mines.afficher_tableau()

        self.tableau_mines.afficher_solution()
        if self.partie_gagnee:
            print("Félicitations! Vous avez gagné la partie!")
        else :
            print("KABOOM! Vous venez d'exploser!\n"
                  "Meilleure chance la prochaine fois!")

    def demander_coordonnees_case_a_devoiler(self):
        coord_x = input("Veuillez entrer le numéro de rangée de la case.\n")
        coord_y = input("\nVeuillez entrer le numéro de colonne de la case.\n")
        if self.valider_coordonnees(coord_x, coord_y):
            return coord_x, coord_y
        else:
            self.demander_coordonnees_case_a_devoiler()

    def valider_coordonnees(self, coord_x, coord_y):
        if coord_x.isdigit() and coord_y.isdigit():
            coord = (int(coord_x), int(coord_y))
            if coord in self.tableau_mines.dictionnaire_cases.keys():
                if self.tableau_mines.dictionnaire_cases[coord].est_a_devoiler():
                    if self.tableau_mines.dictionnaire_cases[coord].contient_mine():
                        self.partie_terminee = True
                    return True
                else:
                    print("Cette case est déjà dévoilée.")
                    return False
            else:
                print("Ces coordonnées sont hors du champ de jeu.")
                return False
        else:
            print("Ce coordonnées sont invalides.")
            return False
