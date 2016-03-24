"""
Module contenant la description de la classe Tableau. Un tableau est utilisé pour jouer une partie du jeu Démineur.
"""

from pymineur.case import Case
import random


class Tableau:
    """
    Documentation de la classe Tableau, implémentée avec un dictionnaire de cases

    Attributes:
        dimension_rangee (int): Nombre de rangées du tableau
        dimension_colonne (int): Nombre de colonnes du tableau
        nombre_mines (int): Nombre de mines cachées dans le tableau

        nombre_cases_sans_mine_a_devoiler (int) : Nombre de cases sans mine qui n'ont pas encore été dévoilées
            Initialement, ce nombre est égal à dimension_rangee * dimension_colonne - nombre_mines

        dictionnaire_cases (dict): Un dictionnaire de case en suivant le format suivant:
            Les clés sont les positions du tableau (un tuple x, y), x étant le numéro de la rangée,
            y étant le numéro de la colonne.
            Les éléments sont des objets de la classe Case.

    """

    def __init__(self):

        self.dimension_y = 5
        self.dimension_x = 5
        self.nombre_mines = 5

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
                cases_voisines = enumerate(self.obtenir_voisins(x, y))
                for cases_voisines in self.dictionnaire_cases:
                    self.dictionnaire_cases[cases_voisines].ajouter_une_mine_voisine()
                mines_placees += 1
            """
        Initialise le tableau à son contenu initial en suivant les étapes suivantes:
            1) On crée chacune des cases du tableau.
            2) On y ajoute ensuite les mines dans certaines cases qui sont choisies au hasard.
            3) À chaque fois qu'on ajoute une mine dans une case, vous devriez incrémenter dans chacune des cases
            voisines un attribut qui représentera le nombre de mines voisines pour ces cases.
        """
        # TODO: À compléter
        # Une bonne fonction du module random à utiliser dans cette méthode est randint(a,b) qui retourne un entier
        # aléatoire entre a et b inclusivement.

    def obtenir_voisins(self, coord_x, coord_y):
        """
        Retourne une liste de coordonnées correspondant aux cases voisines d'une case. Toutes les coordonnées retournées
        doivent être valides (c'est-à-dire se trouver à l'intérieur des dimensions du tableau).

        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut connaître les cases voisines
            colonne_y (int): Numéro de la colonne de la case dont on veut connaître les cases voisines

        Returns:
            list : Liste des coordonnées (tuple x, y) valides des cases voisines de la case dont les coordonnées
            sont reçues en argument
        """
        VOISINAGE = ((coord_x - 1, coord_y - 1), (coord_x -1, coord_y), (coord_x - 1, coord_y + 1),
                     (coord_x, coord_y - 1),           (coord_x, coord_y + 1),
                     (coord_x + 1, coord_y - 1),  (coord_x + 1, coord_y),  (coord_x + 1, coord_y + 1))

        liste_coordonnees_cases_voisines = list(VOISINAGE)
        for c, (x, y) in enumerate(liste_coordonnees_cases_voisines):
            est_valide = self.valider_coordonnees(x, y)
            if not est_valide:
                del liste_coordonnees_cases_voisines[c]
            else:
                pass

        # TODO: Générer la liste des coordonnées valides des cases voisine. Le tuple VOISINAGE est là pour vous aider.

        return liste_coordonnees_cases_voisines

    def valider_coordonnees(self, coord_x, coord_y):
        """
        Valide les coordonnées reçues en argument. Les coordonnées sont considérées valides si elles se trouvent bien
        dans les dimensions du tableau.
        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut valider les coordonnées
            colonne_y (int): Numéro de la colonne de la case dont on veut valider les coordonnées
        Returns:
            bool: True si les coordonnées (x, y) sont valides, False autrement
        """

        return coord_x in (1, self.dimension_x) and coord_y in (1, self.dimension_y)

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
                            print("X ", end= " ")
                        else :
                            print(self.dictionnaire_cases[(x, y)].obtenir_nombre_mines_voisines(),
                                                         end=" ")

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
                        else :
                            print(self.dictionnaire_cases[(x, y)].obtenir_nombre_mines_voisines(),
                                                         end=" ")

                print("\n")

        #for (colonne, rangee) in self.dictionnaire_cases:
            #if colonne == 0:
            #    print("{0:2d} ". format(colonne), end=" ")
            #elif not self.dictionnaire_cases[colonne, rangee].est_devoilee():
            #    print(" {0} ".format("_"), end=" ")
            #else:
            #    print(" {0} ".format(self.dictionnaire_cases[colonne, rangee].nombre_mines_voisines), end=" ")


        """
        Méthode qui affiche la tableau à l'écran. Le tableau montre le contenu des cases dévoilées (mine ou
        nombre de mines voisines) ou un espace vide (comme _) pour les cases non dévoilées.
        """
        # TODO: À compléter

    def contient_cases_a_devoiler(self):
        if self.nombre_cases_sans_mine_a_devoiler == 0:
            return False
        else:
            return True


        """
        Méthode qui indique si le tableau contient des cases à dévoiler
        Returns:
            bool: True s'il reste des cases à dévoiler, False autrement.

        """
        # TODO: À compléter

    def devoiler_case(self, coord):
        self.dictionnaire_cases[coord].devoiler()
        """
        Méthode qui dévoile le contenu de la case dont les coordonnées sont reçues en argument. Si la case ne
        contient pas de mine, on décrémente l'attribut qui représente le nombre de cases sans mine à dévoiler. Aussi,
        si cette case n'est voisine d'aucune mine, on peut dévoiler ses voisins. L'énoncé propose deux façons différentes
        de faire ce dévoilement. Une façon de faire utilise des appels récursifs à la méthode devoiler_case. L'autre
        méthode dévoile les cases dans les axes vertical et horizontal tant que ces cases ne contiennent aucune mine.
            rangee_x (int) : Numéro de la rangée de la case à dévoiler
            colonne_y (int): Numéro de la colonne de la case à dévoiler
        """
        # TODO: À compléter

    def case_contient_mine(self, coord_x, coord_y):
        if self.dictionnaire_cases[coord_x, coord_y].contient_mine():
            return True
        else:
            return False
        """
        Méthode qui vérifie si la case dont les coordonnées sont reçues en argument contient une mine.
        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut vérifier si elle contient une mine
            colonne_y (int): Numéro de la colonne de la case dont on veut vérifier si elle contient une mine
        Returns
            bool: True si la case à ces coordonnées (x, y) contient une mine, False autrement.

        """

if __name__ == '__main__':

    # Ce bout de code est là pour vous aider à tester votre première tentative d'implémentation du tableau. Vous
    # pouvez l'utiliser en exécutant le fichier tableau.py. N'oubliez pas toutefois que l'exécution principale
    # du programme devra se faire avec pymineur.__main__.py

    tableau_test = Tableau()

    tableau_test.afficher_tableau()
    tableau_test.afficher_solution()