""" Exemples de tests unitaires pour la classe Tableau. Aucun test n'est à remettre, mais vous êtes fortement encouragés
à vous en programmer pour valider votre code
"""

from pymineur.tableau import Tableau


def test_initialisation():

    tableau_test = Tableau()

    assert tableau_test.contient_cases_a_devoiler(), "Après l'initialisation, le tableau contient des cases à dévoiler"
    assert tableau_test.nombre_cases_sans_mine_a_devoiler == tableau_test.dimension_colonne * \
        tableau_test.dimension_rangee - tableau_test.nombre_mines, "Après l'initialisation, le nombre de cases à dévoiler est le bon."


def test_valider_coordonnees():

    tableau_test = Tableau()
    dimension_x, dimension_y = tableau_test.dimension_rangee, tableau_test.dimension_colonne

    assert tableau_test.valider_coordonnees(dimension_x, dimension_y), "Les coordonnées vont jusqu'aux dimensions maximales."
    assert not tableau_test.valider_coordonnees(dimension_x+1, dimension_y), "Les coordonnées sont invalides si x dépassent la dimension des rangées."
    assert not tableau_test.valider_coordonnees(dimension_x, dimension_y+1), "Les coordonnées sont invalides si y dépassent la dimension des colonnes."
    assert not tableau_test.valider_coordonnees(-dimension_x, dimension_y), "Les coordonnées sont invalides si x est négatif."
    assert not tableau_test.valider_coordonnees(0, 0), "Les coordonnées sont invalides si elles sont nulles."


if __name__ == '__main__':

    test_initialisation()
    test_valider_coordonnees()