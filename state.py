from move import Move
from copy import deepcopy

joueurs = ['R', 'B'] # les joueurs

# Un tableau de tous les movements possibles d'un pion
mouvements = [
    {'x': -1, 'y': -1, 'type': 'clonage'},
    {'x': 0, 'y': -1, 'type': 'clonage'},
    {'x': 1, 'y': -1, 'type': 'clonage'},
    {'x': -1, 'y': 0, 'type': 'clonage'},
    {'x': 1, 'y': 0, 'type': 'clonage'},
    {'x': -1, 'y': 1, 'type': 'clonage'},
    {'x': 0, 'y': 1, 'type': 'clonage'},
    {'x': 1, 'y': 1, 'type': 'clonage'},
    
    {'x': -2, 'y': -2, 'type': 'sauter'},
    {'x': 0, 'y': -2, 'type': 'sauter'},
    {'x': 2, 'y': -2, 'type': 'sauter'},
    {'x': -2, 'y': 0, 'type': 'sauter'},
    {'x': 2, 'y': 0, 'type': 'sauter'},
    {'x': -2, 'y': 2, 'type': 'sauter'},
    {'x': 0, 'y': 2, 'type': 'sauter'},
    {'x': 2, 'y': 2, 'type': 'sauter'}
]

class State():
    """ la classe qui represente l'etat du jeu
    """

    def __init__(self, board, joueur_actif, nombre_x=2, nombre_o=2, turn=0, has_passed=False, taille=5):
        """le constructeur d'etat

        Args:
            board (str[][]): la valeur du tableau de double dimension
            joueur_actif (str): le joueur qui joue
            nombre_x (int, optionnel): nombre de pions du joueur X. Par défaut à 2.
            nombre_o (int, optionnel): nombre de pions du joueur O. Par défaut à 2.
            turn (int, optionnel): le nombre de tour joue. Par défaut à 0.
            has_passed (bool, optionnel): True si le joueur precedent a passer le tour. Par défaut à False.
            taille (int, optionnel): nombre de lignes et colonne. Par défaut à 5.
        """
        self.board = board
        self.joueur_actif = joueur_actif
        self.nombre_x = nombre_x
        self.nombre_o = nombre_o
        self.has_passed = has_passed
        self.turn = turn
        self.taille = taille
    
    def belongsTo(self, parties, player):
        """La fonction qui teste si la partie a ete joue

        Args:
            parties (State[]): Le tableau des etats joues
            player (Str): Le joueur

        Returns:
            bool: True si l'etat a ete joue sinon False
        """
        result = False
        for p in parties:
            if p.joueur_actif == player:
                result = True
                for i in range(self.taille):
                    for j in range(self.taille):
                        if self.board[i][j] != p.board[i][j]:
                            result = False;
                if result == True:
                    return result
        return result

    def isOver(self):
        """ isOver qui retourne un booléen indiquant si la partie est finie ou non
        
        Returns:
            [bool]: [True ou False]
        """
        
        if self.nombre_x == 0 or self.nombre_o == 0 or self.nombre_o+self.nombre_x == self.taille**2:
            return True
        return False

    def verif_interval(self, x, y, adversaire=" "):
        """ la fonction qui verifie la disponiblite de la case
            et la possibilite de la modifie.

        Args:
            x (int): l'indice de colonne
            y ([int): l'indice de ligne
            adversaire (str, optional): la case a modifie. Par défaut à " ".

        Returns:
            bool: True si les coordonnees respectent les conditions sinon False
        """
        return x < self.taille and x >= 0 and y < self.taille and y >= 0 and self.board[x][y] == adversaire       
    
    def getMove(self,joueur):
        """  une fonction qui prend un joueur en entrée et retour l’ensemble des coups possibles de ce joueur

        Args:
            joueur (str): un joueur

        Returns:
            Move[]: l’ensemble des coups possibles de ce joueur
        """
        result = []
        for i, ligne in enumerate(self.board):
            for j, v in enumerate(ligne):
                if v == joueur:
                    for z, mv in enumerate(mouvements[:8]):
                        if self.verif_interval(mv['x']+i, mv['y']+j):
                            move = Move(i,j,mv['x']+i,mv['y']+j,mv['type'])
                            result.append(move)
                        if self.verif_interval(mouvements[z+8]['x']+i, mouvements[z+8]['y']+j):
                            move = Move(i,j,mouvements[z+8]['x']+i,mouvements[z+8]['y']+j,mouvements[z+8]['type'])
                            result.append(move)
                        
        return result            

    def getScore(self,joueur):
        """La fonctione qui retourne le score du jeu par rapport au nombre de pions

        Args:
            joueur (str): un joueur

        Returns:
            float: (nombre de pion du joueur)/(le total des pions) 
        """
        return self.nombre_x/(self.nombre_o+self.nombre_x) if joueur == joueurs[0] else self.nombre_o/(self.nombre_o+self.nombre_x)
    
    def get_adversaire(self):
        """La fonction qui change du joueur

        Returns:
            str: un joueur
        """
        return joueurs[0] if self.joueur_actif == joueurs[1] else joueurs[1]
    
    def play(self,move):
        """La fonction prend un coup en entrée et retourne un nouvel état

        Args:
            move (Move): un coup

        Returns:
            State: un nouvel etat
        """
        new_state = deepcopy(self)
        adversseur = self.get_adversaire()
        new_state.board[move.pos_a_x][move.pos_a_y] = self.joueur_actif
        for m in mouvements[:8]:
            if self.verif_interval(move.pos_a_x+m['x'],move.pos_a_y+m['y'],adversseur):
                new_state.board[move.pos_a_x+m['x']][move.pos_a_y+m['y']] = self.joueur_actif
                if self.joueur_actif == joueurs[0]:
                    new_state.nombre_x += 1
                    new_state.nombre_o -= 1
                else:
                    new_state.nombre_o += 1
                    new_state.nombre_x -= 1
        if move.type == "sauter":
            new_state.board[move.pos_i_x][move.pos_i_y] = " "
        else:
            if self.joueur_actif == joueurs[0]:
                new_state.nombre_x += 1
            else:
                new_state.nombre_o += 1
        new_state.turn += 1
        new_state.joueur_actif = adversseur
        return new_state

    def afficher_grille(self):
        """La fonction qui affiche le tableau
        """
        print("\n")
        print(f"\t{'-' * 6 * self.taille}")
        for i in range(self.taille):
            print('\t|', end="")
            for j in range(self.taille):
                print(f"  {self.board[i][j]}  |", end="")
            print(f"\n\t{'-' * 6 * self.taille}")
