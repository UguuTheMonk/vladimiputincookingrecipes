"""
Module principal du package pymineur. C'est ce module que nous allons exécuter pour démarrer votre jeu.
"""

print("Bonjour asdfojaserjhfgvaserfe")
from pymineur.partie import Partie

if __name__ == '__main__':
    # Création d'une instance de Partie.
    partie = Partie()

    # Démarrage de cette partie.
    partie.jouer()

    input('Appuyer sur ENTER pour quitter.')
