class Move(object):
    def __init__(self, pos_i_x, pos_i_y, pos_a_x, pos_a_y, type):
        self.pos_i_x = pos_i_x
        self.pos_i_y = pos_i_y
        self.pos_a_x = pos_a_x
        self.pos_a_y = pos_a_y
        self.type = type
    
    def __str__(self):
        return "("+ str(self.pos_i_x) +':'+ str(self.pos_i_y) +") => (" + str(self.pos_a_x) +':'+ str(self.pos_a_y) +") et type=" + self.type
