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
c,d=np.shape(positions.round())# récupère le nombre de set de coordonnées (donc le nombre de balise)


for i in range (a):
    for j in range (b):
        if test[i,j]==1:
            plan.create_rectangle(w*j/a,h*i/b,w*(j+1)/a,h*(i+1)/b,fill='red')# crée les rectangles correspondants aux murs
for k in range (c):
    plan.create_rectangle(positions.round()[k,0],positions.round()[k,1],positions.round()[k,0]+w/a,positions.round()[k,1]+h/b,fill='green')# crée les points représentant les agents

TKI_Principal.mainloop ( )
# problème au niveau des echelles puisque le canvas fait 500x500 alors que les coordonnées vont de 0 à 2
