
# Importation du module Tkinter

from tkinter import *
import os

from menu1 import *



## Initialisation d'un changement de fenetre
def changer():
    interface.destroy()
    os.popen("python main.py")

# Creation de l'interface
interface = Tk()

# Personnalisation de l'interface

interface.title("Coeur de LEDs")    # Changement du titre de la fenetre
interface.geometry("1200x700")      # Reglage de la taille par defaut de l'interface
interface.iconbitmap("logo\logo.ico")    # Ajout d'une icone a l'application
interface.config(background="pink") # Changer la couleur d'arriere plan de l'interface

## Creation d'une Frame principale
frame=Frame(interface,bg="pink")

## Creation d'une Frame
boite=Frame(interface, bg="pink")

image=PhotoImage(file="logo\logo.PNG")
canevas=Canvas(boite,width=200,height=200,bg="pink")
canevas.create_image(100,100,image=image)
canevas.pack()
boite.pack(fill=X)

## Creation d'une seconde Frame pour stocker les boutons 
boite_2=Frame(interface,bg="pink")
label_title=Label(boite_2,text="Quel mode d'allumage souhaitez-vous pour faire briller les LEDs?", font=("calibri",30),bg="pink")
label_title.pack(expand=YES)

## Creation d'une sous-Frame
sous_boite=Frame(boite_2,bg="pink",width=300)
padding=200

## Creation des boutons de selections

    # Premier

bouton_1=Button(sous_boite,text="LED 1", font=("calibri",30),bg="pink",width=10,command=LEDune)
bouton_1.grid(row=0,column=0,sticky=W)

    # Deuxieme

bouton_2=Button(sous_boite,text="LED 2", font=("calibri",30),bg="pink",width=10,command=LEDdeux)
bouton_2.grid(row=0,column=1,sticky=W)

    # Troisieme

bouton_3=Button(sous_boite,text="LED 3", font=("calibri",30),bg="pink",width=10,command=LEDtrois)
bouton_3.grid(row=0,column=2,sticky=W)

    # Quatrieme

bouton_4=Button(sous_boite,text="LED 4", font=("calibri",30),bg="pink",width=10,command=LEDquatre)
bouton_4.grid(row=0,column=3,sticky=W)

    # Cinquieme

bouton_5=Button(sous_boite,text="LED 5", font=("calibri",30),bg="pink",width=10,command=LEDcinq)
bouton_5.grid(row=0,column=4,sticky=W)


    # sixieme

bouton_6=Button(sous_boite,text="LED 6", font=("calibri",30),bg="pink",width=10,command=LEDsix)
bouton_6.grid(row=1,column=0,sticky=W)

    # septieme

bouton_7=Button(sous_boite,text="LED 7", font=("calibri",30),bg="pink",width=10,command=LEDsept)
bouton_7.grid(row=1,column=1,sticky=W)

    # huitieme

bouton_8=Button(sous_boite,text="LED 8", font=("calibri",30),bg="pink",width=10,command=LEDhuit)
bouton_8.grid(row=1,column=2,sticky=W)

    # neuvieme

bouton_9=Button(sous_boite,text="LED 9", font=("calibri",30),bg="pink",width=10,command=LEDneuf)
bouton_9.grid(row=1,column=3,sticky=W)

    # dixieme

bouton_10=Button(sous_boite,text="LED 10", font=("calibri",30),bg="pink",width=10,command=LEDdix)
bouton_10.grid(row=1,column=4,sticky=W)




sous_boite.pack()

## Creation d'un bouton de fermeture de l'interface

bouton_fermeture=Button(boite_2,text="QUITTER", font=("calibri",30),bg="pink",width=10,command=changer)
bouton_fermeture.pack(side=BOTTOM)


boite_2.pack(expand=YES)


interface.mainloop()

