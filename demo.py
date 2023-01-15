from copy import deepcopy
from alphabeta import Alphabeta
from minimax import Minimax
from state import State
from state import joueurs

def demo(taille=5, deep_x=2, deep_o=2, algorithm=2):
    """La demonstration de l'application

    Args:
        taille (int, optional): nombre de lignes et colonne. Par défaut à 5 ex: 5X5.
        deep_x (int, optional): La profondeur de X. Par défaut à 2.
        deep_o (int, optional):  La profondeur de Y. Par défaut à 2.
        algorithm (int, optional): ALGO a utilise: 2=Alphabeta 0=Minimax et 1=Negamax. Par défaut 2.
    """
    if taille >= 2 and deep_x > 0 and deep_o > 0:
        board_init = []
        for i in range(taille):
            board_init.append([])
            for j in range(taille):
                if i == 0 and j == 0:
                    board_init[i].append(joueurs[0])
                elif i == 0 and j == taille-1:
                    board_init[i].append(joueurs[1])
                elif i == taille-1 and j == 0:
                    board_init[i].append(joueurs[1])
                elif i == taille-1 and j == taille-1:
                    board_init[i].append(joueurs[0])
                else:
                    board_init[i].append(' ')
       
        h = []
        player = joueurs[0];
        game = State(board_init,player,taille=taille)
        game.afficher_grille()
    
        algo = None
        nombre_noeud_visites = []
        nombre_tours = []
        
        while game.isOver() == False:
            h.append(game)
            player = game.joueur_actif
            print(player)
            deep = deep_x if game.joueur_actif == joueurs[0] else deep_o
            # print(f"La profondeur est : {deep}")
            if algorithm == 2:
                ab = Alphabeta(game.joueur_actif, deep)
                bestMove = ab.getBestMove(game,deep)
                algo = ab
            else:
                mm = Minimax(game.joueur_actif,deep,algorithm)
                bestMove = mm.getBestMove(game,deep)
                algo = mm
            if bestMove == None and (game.nombre_o+game.nombre_x < taille**2):
                print(f"le joueur {player} passe le tour")
                game.joueur_actif = game.get_adversaire()
                game.has_passed = True
                game.turn += 1
            else:
                game = game.play(bestMove)
                if game.has_passed == False:
                    player = game.joueur_actif
                print(bestMove)
                print(f"{game.nombre_x}-{game.nombre_o}   {game.turn} ==> {game.getScore(player)}")
                game.afficher_grille()
            
            nombre_noeud_visites.append(algo.nombre_noeud_visites)
            nombre_tours.append(game.turn)
            
            if game.belongsTo(h,player):
                break
        return game, nombre_noeud_visites, nombre_tours
        
    else:
        raise ValueError("la taille doit etre superieure a 1 et les deux profondeurs doivent etre superieure a 0")


if __name__ == '__main__':
    import sys
    import os
    
    if len(sys.argv) != 5:
        print("Fourniser les bons parametres: [taille] [profondeur_x] [profondeur_y] [algo]")
        print("taille: int, profondeur_x: int, profondeur_y: int, algo: int")
        print(f"Exemple: python3 {os.path.basename(sys.argv[0])} 5 2 2 2")
    else:
        game, nombre_noeud_visites, nombre_tours = demo(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        game.afficher_grille()
        if game.nombre_x > game.nombre_o:
            print(f"le joueur {joueurs[0]} a gagne avec le score {game.getScore(joueurs[0])}")
        elif game.nombre_x < game.nombre_o:
            print(f"le joueur {joueurs[1]} a gagne avec le score {game.getScore(joueurs[1])}")
        else:
            print(f"Egalite entre les deux!!!")
        # print(f"Le nombre des noeuds visites sont: {nombre_noeud_visites}")
        # print(nombre_noeud_visites)
        # print(nombre_tours)
