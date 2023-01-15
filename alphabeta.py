from copy import deepcopy
from algorithm import Algorithm

class Alphabeta(Algorithm):
    """La classe Alphabeta

    Args:
        Algorithm: Heritage
    """
    def __init__(self, player, depth):
        """Le constructeur de Alphabeta

        Args:
            player (str): le joueur en cours
            depth (int): la profondeur
        """
        super().__init__(player, depth)

    def alphabeta(self,state,alpha,beta,d):
        """la fonction alphabeta

        Args:
            state (State): un etat
            alpha (float): La variable alpha
            beta (float): La variable beta
            d (int): la profondeur

        Returns:
            [type]: [description]
        """
        new_state = deepcopy(state)
        self.nombre_noeud_visites += 1
        if d == 0 or new_state.isOver():
            return new_state.getScore(new_state.joueur_actif)
        else:
            if new_state.joueur_actif == self.player:
                for move in new_state.getMove(new_state.joueur_actif):
                    next_state = new_state.play(move)
                    alpha = max(alpha,self.alphabeta(next_state,alpha,beta,d-1))
                    if alpha >= beta:
                        return alpha
                return alpha
            else:
                for move in new_state.getMove(new_state.joueur_actif):
                    next_state = new_state.play(move)
                    beta = min(beta,self.alphabeta(next_state,alpha,beta,d-1))
                    if alpha >= beta:
                        return beta
                return beta
    
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
            value = self.alphabeta(nextstate,float("-inf"),float("inf"),deepness-1)
            if value > bestvalue:
                bestvalue = value
                bestaction = action
        return bestaction