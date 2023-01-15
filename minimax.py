from copy import deepcopy
from algorithm import Algorithm

class Minimax(Algorithm):
    """La classe Minimax qui herite de la classe Algorithm

    Args:
        Algorithm: Heritage
    """
    
    def __init__(self, player, depth, type=0):
        """Le constructeur de Minimax

        Args:
            player (str): le joueur en cours
            depth (int): la profondeur
        """
        super().__init__(player, depth)
        self.type = type
    
    def minimax(self,state,d):
        """La fonction minimax qui trouve le meilleur scors

        Args:
            state (State): Un etat
            d (int): la profondeur

        Returns:
            float: retourne le meilleur score
        """
        new_state = deepcopy(state)
        self.nombre_noeud_visites += 1
        if d == 0 or new_state.isOver():
            return new_state.getScore(new_state.joueur_actif)
        else:
            if new_state.joueur_actif == self.player:
                b = float("-inf")
                for move in new_state.getMove(new_state.joueur_actif):
                    next_state = new_state.play(move)
                    m = self.minimax(next_state,d-1)
                    if b < m:
                        b = m
            else:
                b = float("inf")
                for move in new_state.getMove(new_state.joueur_actif):
                    next_state = new_state.play(move)
                    m = self.minimax(next_state,d-1)
                    if b > m:
                        b = m
            return b
        
    def getBestMove(self,state,deepness):
        """La fonction qui trouve le bon coup

        Args:
            state (State): un etat
            deepness (int): la profondeur

        Returns:
            Move: le meilleur coup
        """
        new_state = deepcopy(state)
        bestaction = None
        bestvalue = float("-inf")
        for action in new_state.getMove(new_state.joueur_actif):
            nextstate = new_state.play(action)
            value = 0
            if self.type == 0:
                value = self.minimax(nextstate,deepness-1)
            else:
                value = self.negamax(nextstate,deepness-1)
            if value > bestvalue:
                bestvalue = value
                bestaction = action
        return bestaction
                        
    def negamax(self,state,d):
        """La fonction qui trouve le bon coup

        Args:
            state (State): un etat
            d (int): la profondeur

        Returns:
            float: retourne le meilleur score
        """
        new_state = deepcopy(state)
        self.nombre_noeud_visites += 1
        if d == 0 or new_state.isOver():
            return new_state.getScore(self.player) if new_state.joueur_actif == self.player else - new_state.getScore(self.player)
        else:
            m = float("-inf")
            for move in new_state.getMove(self.player):
                next_state = new_state.play(move)
                m = max(m, - self.negamax(next_state,d-1))
            return m;