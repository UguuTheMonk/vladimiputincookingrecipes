
from pymineur.partie import Partie


if __name__ == '__main__':
    while True:
        partie = Partie()
        partie.jouer()
        rejouer = input("Appuyez sur une touche pour refaire une partie, ou faites N pour quitter.")
        rejouer = rejouer.lower()
        if rejouer == "n":
            break

