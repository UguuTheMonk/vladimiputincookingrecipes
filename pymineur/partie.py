"""
Module contenant la description de la classe Partie qui permet de jouer une partie du jeu démineur.
Doit être démarré en appelant la méthode jouer(). Cette classe contient les informations sur une partie et
utilise un objet tableau_mines (une instance de la classe Tableau).
"""

from tableau import Tableau
import os

class Partie:
    """
    La classe Partie contient les informations sur une partie du jeu Démineur, qui se jouera avec
    un tableau de mines. Des méthodes sont disponibles pour faire avancer la partie et interagir
    avec l'utilisateur.

    Attributes:
        tableau_mines (Tableau): Le tableau de cases où les mines sont cachées avec lequel se
                déroule la partie.
    """

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
        tableau = Tableau()
        tableau.afficher_tableau()
        while not self.partie_terminee: # Va falloir remettre tout ça dans la prochaine méthode. dumbass
            coord_x = input("Veuillez entrer le numéro de colonne de la case. \n")
            coord_y = input("\nVeuillez entrer le numéro de rangée de la case.\n")
            if coord_x.isdigit() and coord_y.isdigit():
                coord = (int(coord_x), int(coord_y))
                print(coord)
                if coord in tableau.dictionnaire_cases.keys():
                    if tableau.dictionnaire_cases[coord].est_a_devoiler():
                        tableau.devoiler_case(int(coord_y), int(coord_x))
                        tableau.afficher_tableau()
                    else:
                        print("Cette case est déjà dévoilée")
                else:
                    print("Ces coordonnées sont hors du champ de jeu.")
            else :
                print("Ces coordonnées sont invalides.")
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
        """
        Méthode qui demande à l'utilisateur d'entrer la coordonnée de la case qu'il veut dévoiler.
        Cette coordonnée comporte un numéro de rangée et un numéro de colonne.
        Tant que les coordonnées ne sont pas valides, on redemande de nouvelles coordonnées.
        Une fois les coordonnées validées, on retourne les deux numéros sous forme d'entiers.

        Returns:
            int: Numéro de la rangée
            int: Numéro de la colonne

        """
        # TODO: À compléter

        return 1, 1

    def valider_coordonnees(self, coord_x, coord_y):
        """
        Méthode qui valide les coordonnées reçues en paramètres.
        Les coordonnées doivent 1) être des caractères numériques, 2) être à l'intérieur des valeurs possibles
        des rangées et des colonnes du tableau et 3) correspondre à une case qui n'a pas encore été dévoilée.

        Args:
            rangee_x (int):     Numéro de la rangée
            colonne_y (int):    Numéro de la colonne

        Returns:
            bool : True si les coordonnées sont valides, False autrement.
        """
        # TODO: À compléter.
        # Suggestion: Cette méthode pourrait appeler trois autres méthodes qui se séparent les trois types de
        # validation nécessaires. À vous de définir leur interface.
