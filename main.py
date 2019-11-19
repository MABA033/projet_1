import argparse


def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description='mon programme consiste à la création d\'un jeu quoridor entre 2 joueurs')
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument(
    'idul', nargs='+', metavar= 'idul', help = print('usage: main.py [-h] [-l] idul\n' + 'positional arguments:\n idul          IDUL du joueur.' + 'optional arguments:\n-h, --help    show this help message and exit\n -l, --lister  Lister les identifiants de vos 20 dernières parties.'), type = int
)

    return parser.parse_args()
