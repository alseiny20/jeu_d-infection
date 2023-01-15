import matplotlib.pyplot as plt

from demo import demo


game = None
nombre_noeud_visites, nombre_tours = [],[]

for i in range(3):
    game, nombre_noeud_visites, nombre_tours = demo(7,i+1,i+1,0)

    # plt.figure()
    fig, ax = plt.subplots()
    ax.plot(nombre_tours, nombre_noeud_visites)

    ax.set(xlabel='Tour', ylabel='Les nœuds visites',
        title='Les nœuds visites par tour avec Negamax avec une profondeur egale a '+ str(+i+1))
    # ax.grid()
    name = "../images/courbe_negamax_"+str(i+1)+".png"
    fig.savefig(name)
    # plt.show()