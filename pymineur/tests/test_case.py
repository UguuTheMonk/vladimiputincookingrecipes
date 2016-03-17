""" Exemples de tests unitaires pour la classe Case. Aucun test n'est à remettre, mais vous êtes fortement encouragés
à vous en programmer pour valider votre code
"""

from pymineur.case import Case


def test_devoiler():

    case_test = Case()
    case_test.devoiler()

    assert case_test.est_devoilee, "La case est dévoilée, le test doit être réussi."


def test_mine():

    case_test = Case()
    case_test.ajouter_mine()

    assert case_test.est_minee, "La case est minée, le test doit être réussi."



if __name__ == '__main__':

    # Exécution des tests unitaires.

    test_devoiler()
    test_mine()