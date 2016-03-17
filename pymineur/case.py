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
        """
        Cette méthode modifie le statut de la case lorsque son contenu est dévoilé.
        """
        # TODO: À compléter

    def ajouter_mine(self):
        """
        Cette méthode permet d'ajouter une mine à la case en modifiant un attibut.
        """
        # TODO: À compléter

    def contient_mine(self):
        """
        Méthode qui retourne si la case est minée ou non.

        Returns:
            bool: True si la case est minée, False autrement.
        """
        # TODO: À compléter
        return False

    def est_a_devoiler(self):
        """
        Retourne si la case peut être dévoilée.

        Returns:
            bool: True si la case n'a pas encore été dévoilée, False autrement
        """
        # TODO: À compléter
        return True

    def ajouter_une_mine_voisine(self):
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
        """
        Méthode qui indique si la case est voisine d'une mine ou nom
        Returns:
            bool: True si la case est voisine d'une mine, False autrement.
        """
        # TODO: À compléter
        return True