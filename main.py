import soft_information

SI_list = soft_information.parse_scenario('soft_information/data/si1.json')
positions, _ = soft_information.compute_positions(SI_list, nb_points=3)

print(positions.round())

# Objectif: prendre en photo un plan via son téléphone et l'integrer dans l'algo 

from PIL import Image as img
import numpy as np 

temp=img.open('/filedirectory').convert('L') 

image_array=np.array(temp)

from tkinter import *


# données du canvas 

# toujours faire attention à ce que h et w soit égales au valeurs dans la fonction canvas


a,b=np.shape(image_array)


TKI_Principal = Tk( ) 
plan = Canvas ( TKI_Principal , height = a , width = b )
plan.pack()

#c,d=np.shape(positions.round())# récupère le nombre de set de coordonnées (donc le nombre de balise)


for i in range (a):
    for j in range (b):
        if image_array[i,j]>=70 and image_array[i,j]<=90:
            plan.create_rectangle(j,i,j+1,i+1,fill='red')# crée les rectangles correspondants aux murs
for k in range (c):
    plan.create_rectangle(positions.round()[k,0],positions.round()[k,1],positions.round()[k,0]+w/a,positions.round()[k,1]+h/b,fill='green')# crée les points représentant les agents


TKI_Principal.mainloop ( )
# problème au niveau des echelles puisque le canvas fait 500x500 alors que les coordonnées vont de 0 à 2
