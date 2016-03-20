"""
Module contenant la description de la classe Case. Une case peut contenir une mine
et être dans différents états de dévoilement.
"""


class Case:
    """
    Documentation de la classe Case
    Attributes:
        est_minee (bool): Vrai si la case contient une mine, False autrement
        est_devoilee (bool): Vrai si la case a été dévoilée, False autrement
        nombre_mines_voisines (int): Le nombre de mines présentes dans le voisinage de la case.
    """

    def __init__(self):
        # Création des attributs avec des valeurs par défaut
        self.est_minee = False
        self.est_devoilee = False
        self.nombre_mines_voisines = 0

    def devoiler(self):
        self.est_devoile = True
        # TODO: À compléter

    def ajouter_mine(self):
        self.est_minee = True
        # TODO: À compléter

    def contient_mine(self):
        if self.est_minee == True:
            return True
        else:
            return False

    def est_a_devoiler(self):
        if self.est_devoilee == False:
            return True
        else:
            return False

    def ajouter_une_mine_voisine(self):
        self.nombre_mines_voisines += 1
        """
        Méthode qui incrémente l'attribut nombre_mines_voisines
        """
        # TODO: À compléter

    def obtenir_nombre_mines_voisines(self):

        """
        Méthode qui retourne le nombre de mines voisines de cette case.
        Returns:
            int: nombre de mines voisines de cette case
        """
        # TODO: À compléter
        return 0

    def est_voisine_d_une_mine(self):
        if self.nombre_mines_voisines == 0:
            return False
        else:
            return True