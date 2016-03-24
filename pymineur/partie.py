"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Doit être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une partie et
utilise un objet tableau_mines (une instance de la classe Tableau).
"""

from pymineur.tableau import Tableau
#import os

class Partie:

    def __init__(self):
        # Création d'une instance de la classe Tableau, qui sera manipulée par les méthodes de la classe.
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
        #os.system('cls')
        self.tableau_mines = Tableau()
        self.partie_terminee = False
        self.partie_gagnee = False

    def victoire(self):
        self.partie_gagnee = True

    def jouer(self):
        tableau = self.tableau_mines
        tableau.afficher_tableau()
        while not self.partie_terminee:
            coord = self.demander_coordonnees_case_a_devoiler()
            print(coord)
            tableau.devoiler_case(coord)
            tableau.afficher_tableau()

        """
        Tant que la partie n'est pas terminée, on joue la partie. À chaque tour:
            - On affiche le tableau de cases
            - On demande à l'utilisateur les coordonnées d'une case à dévoiler
            - On dévoile la case
            - On détecte si une mine a été actionnée

        Une fois la partie terminée, on affiche le tableau de cases complètement dévoilée
        et on indique un message sur l'issue de la partie (victoire ou défaite).

        """

        # TODO: À compléter

    def demander_coordonnees_case_a_devoiler(self):
        coord_x = input("Veuillez entrer le numéro de colonne de la case. \n")
        coord_y = input("\nVeuillez entrer le numéro de rangée de la case.\n")
        if self.valider_coordonnees(coord_x, coord_y):
            coord = (coord_x, coord_y)
            return coord
        else:
            self.demander_coordonnees_case_a_devoiler()


    def valider_coordonnees(self, coord_x, coord_y):
        if coord_x.isdigit() and coord_y.isdigit():
            coord = (int(coord_x), int(coord_y))
            if coord in tableau.dictionnaire_cases.keys():
                if tableau.dictionnaire_cases[coord].est_a_devoiler():
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
