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

        self.dimension_rangee = 5
        self.dimension_colonne = 5
        self.nombre_mines = 5

        self.nombre_cases_sans_mine_a_devoiler = self.dimension_rangee * self.dimension_colonne - self.nombre_mines

        # Le dictionnaire de case, vide au départ, qui est rempli par la fonction initialiser_tableau().
        self.dictionnaire_cases = {}

        self.initialiser_tableau()

    def initialiser_tableau(self):
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

    def obtenir_voisins(self, rangee_x, colonne_y):
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
        VOISINAGE = ((-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1))

        liste_coordonnees_cases_voisines = []

        # TODO: Générer la liste des coordonnées valides des cases voisine. Le tuple VOISINAGE est là pour vous aider.

        return liste_coordonnees_cases_voisines

    def valider_coordonnees(self, rangee_x, colonne_y):
        """
        Valide les coordonnées reçues en argument. Les coordonnées sont considérées valides si elles se trouvent bien
        dans les dimensions du tableau.
        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut valider les coordonnées
            colonne_y (int): Numéro de la colonne de la case dont on veut valider les coordonnées
        Returns:
            bool: True si les coordonnées (x, y) sont valides, False autrement
        """

        # TODO: À compléter

        return True

    def valider_coordonnees_a_devoiler(self, rangee_x, colonne_y):
        """
        Valide que les coordonnées reçues en argument sont celles d'une case que l'on peut dévoiler (donc qui n'a pas
        encore été dévoilée.
        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut valider les coordonnées
            colonne_y (int): Numéro de la colonne de la case dont on veut valider les coordonnées
        Returns
            bool: True si la case à ces coordonnées (x, y) peut être dévoilée,
            False autrement (donc si elle a déjà été dévoilée).
        """
        # TODO: À compléter

        return True

    def afficher_solution(self):
        """
        Méthode qui affiche la tableau solution à l'écran. La solution montre les mines pour les cases qui en contiennent
        et la valeur du nombre de mines voisines pour les autres cases.
        """
        # TODO: À compléter

    def afficher_tableau(self):
        """
        Méthode qui affiche la tableau à l'écran. Le tableau montre le contenu des cases dévoilées (mine ou
        nombre de mines voisines) ou un espace vide (comme _) pour les cases non dévoilées.
        """
        # TODO: À compléter

    def contient_cases_a_devoiler(self):
        """
        Méthode qui indique si le tableau contient des cases à dévoiler
        Returns:
            bool: True s'il reste des cases à dévoiler, False autrement.

        """
        # TODO: À compléter
        return True

    def devoiler_case(self, rangee_x, colonne_y):
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

    def case_contient_mine(self, rangee_x, coordonnee_y):
        """
        Méthode qui vérifie si la case dont les coordonnées sont reçues en argument contient une mine.
        Args:
            rangee_x (int) : Numéro de la rangée de la case dont on veut vérifier si elle contient une mine
            colonne_y (int): Numéro de la colonne de la case dont on veut vérifier si elle contient une mine
        Returns
            bool: True si la case à ces coordonnées (x, y) contient une mine, False autrement.

        """
        # TODO: À compléter

        return False

if __name__ == '__main__':

    # Ce bout de code est là pour vous aider à tester votre première tentative d'implémentation du tableau. Vous
    # pouvez l'utiliser en exécutant le fichier tableau.py. N'oubliez pas toutefois que l'exécution principale
    # du programme devra se faire avec pymineur.__main__.py

    tableau_test = Tableau()

    tableau_test.afficher_tableau()
    tableau_test.afficher_solution()