import soft_information

SI_list = soft_information.parse_scenario('soft_information/data/si1.json')
positions, _ = soft_information.compute_positions(SI_list, nb_points=3)

print(positions.round())

import numpy as np 
from tkinter import *
# on créer dans une matrice la pièce que l'on souhaite modéliser 
test=np.array([[1,0,0,0,1],[1,0,0,1,1],[0,0,0,0,1],[1,1,0,0,0],[1,0,0,0,0]])

# données du canvas 
w=500
h=500
# toujours faire attention à ce que h et w soit égales au valeurs dans la fonction canvas


a,b=np.shape(test)

TKI_Principal = Tk( ) 
plan = Canvas ( TKI_Principal , height = 500 , width = 500 )
plan.pack()
print(test)
for i in range (a):
    for j in range (b):
        if test[i,j]==1:
            plan.create_rectangle(w*j/a,h*i/b,w*(j+1)/a,h*(i+1)/b,fill='red')

TKI_Principal.mainloop ( )
