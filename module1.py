from tkinter import *
fen =Tk()
fen.geometry("1000x1000")
fen.title("Finder (v1.2)")
fen.config(bg="#26c6f2")
r = 1
#IMPORT
from random import*
from math import*
#VARIABLE-----------------------------------------------------------------------
a=0
#LES PHOTOS
de1=PhotoImage(file="Images/d1.gif")
de2=PhotoImage(file="Images/d2.gif")
de3=PhotoImage(file="Images/d3.gif")
de4=PhotoImage(file="Images/d4.gif")
de5=PhotoImage(file="Images/d5.gif")
de6=PhotoImage(file="Images/de6.gif")
#FONCTION-----------------------------------------------------------------------
def retour():
    global r
    global SortieR
    SortieR=Button(fen,text="Retour",bg="#26c6f2",command=back)
    SortieR.place(x=550,y=100)
    r = 1
def back():
    global SortieR
    SortieR.destroy()
    tex0.destroy()
    tex1.destroy()
    tex2.destroy()
    tex3.destroy()
    menu()
def menu():
    global Titre
    global Jouer
    global Regle
    Titre=Label(fen,text="La Banquise !",bg="#26c6f2",font=("calibri","30"))
    Titre.place(x=350,y=30)
    Jouer=Button(fen,text="Lancer une partie",bg="#26c6f2",command=lapartie)
    Jouer.place(x=150,y=100)
    Regle=Button(fen,text="Les Règles",bg="#26c6f2",command=regle)
    Regle.place(x=150,y=130)

def menukill():
    Jouer.destroy()
def lapartie():
    global can
    global verification
    global resultat1
    global resultat2
    global resultat3
    global reponse1
    global reponse2
    global reponse3
    global textO
    global textT
    global textP
    global tex0
    global tex1
    global tex2
    global tex3
    #BOITES UTILISATEUR---------------------------------------------------------
    text1 = Label(fen, text="Nombre d'ours:",bg="#26c6f2")
    text1.place(x=50,y=270)
    reponse1=Entry(width=20)
    reponse1.place(x=170,y=270)
    text2 = Label(fen, text="Nombre de phoques:",bg="#26c6f2")
    text2.place(x=50,y=295)
    reponse2=Entry(width=20)
    reponse2.place(x=170,y=295)
    text3 = Label(fen, text="Nombre de trous:",bg="#26c6f2")
    text3.place(x=50,y=320)
    reponse3=Entry(width=20)
    reponse3.place(x=170,y=320)
    #SOLUTIONS------------------------------------------------------------------
    resultat1 = Label(fen, text="-",bg="#26c6f2")
    resultat1.place(x=370,y=370)
    resultat2 = Label(fen, text="-",bg="#26c6f2")
    resultat2.place(x=370,y=390)
    resultat3 = Label(fen, text="-",bg="#26c6f2")
    resultat3.place(x=370,y=410)
    #CORRECTION-----------------------------------------------------------------
    textO = Label(fen, text="Avez-vous la bonne réponse pour le nombre Ours ?",bg="#26c6f2")
    textO.place(x=50,y=370)
    textP = Label(fen, text="Avez-vous la bonne réponse pour le nombre Phoques ?",bg="#26c6f2")
    textP.place(x=50,y=390)
    textT = Label(fen, text="Avez-vous la bonne réponse pour le nombre de Trous ?",bg="#26c6f2")
    textT.place(x=50,y=410)
    #BOUTONS--------------------------------------------------------------------
    #REJOUER
    Lancer = Button(fen, text="Lancer une partie!", command = play,bg="#D27C8B",activebackground="red")
    Lancer.place(x=550,y=500)
    #VERIFIER
    verification = Button(fen, text="Vérifier", command = verifG,bg="#26c6f2")
    #SORTIE
    sortie = Button(fen, text="Quitter le jeu", command = fen.destroy,bg="#D27C8B")
    sortie.place(x=720,y=500)
    #CANVAS-------------------------------------------------------------------------
    can = Canvas(fen, width=250, height=250)
    can.place(x=550, y=180)
    can.configure(bg="skyblue")
    #LANCER FONCTION
    menukill()
def regle():
    global tex0
    global tex1
    global tex2
    global tex3
    #REGLE---------------------------------------------------------------
    tex0 = Label(fen, text="Comment jouer ?",bg="#26c6f2",font=("calibri","20"))
    tex0.place(x=50,y=145)
    tex1 = Label(fen, text="Les trous sont aux centres de la banquise",bg="#26c6f2")
    tex1.place(x=50,y=180)
    tex2 = Label(fen, text="Les ours restent autours du trou afin d'attraper un phoque.",bg="#26c6f2")
    tex2.place(x=50,y=200)
    tex3 = Label(fen, text="Faire 7 - Total des ours pour trouver les phoques.",bg="#26c6f2")
    tex3.place(x=50,y=220)
    retour()
    Regle.destroy()
    menukill()
def play():
    cube1()
    verification.place(x=330,y=295)
def cube1():
    global ours
    global phoque
    global trou
    cube1 = randint(1,6)
    ours = 0
    trou = 0
    phoque = 0
    i = 0
    while i != 3 :
        cube1 = randint(1,6)
        if i == 0:
            x = 50
            y = 50
        elif i == 1:
            x = 125
            y = 125
        elif i == 2:
            x = 200
            y = 200
        if cube1 == 1:
            ours = ours + 0
            phoque = phoque + 6
            trou = trou + 1
            face1=can.create_image(x, y, image=de1)
        elif cube1 == 2:
            ours = ours + 2
            phoque = phoque + 5
            trou = trou + 0
            face2=can.create_image(x, y, image=de2)
        elif cube1 == 3:
            ours = ours + 2
            phoque = phoque + 4
            trou = trou + 1
            face3=can.create_image(x, y, image=de3)
        elif cube1 == 4:
            ours = ours + 4
            phoque = phoque + 3
            trou = trou + 0
            face4=can.create_image(x, y, image=de4)
        elif cube1 == 5:
            ours = ours + 4
            phoque = phoque + 2
            trou = trou + 1
            face5 = can.create_image(x, y, image=de5)
        elif cube1 == 6:
            ours = ours + 6
            phoque = phoque + 1
            trou = trou + 0
            face6=can.create_image(x, y, image=de6)
        i = i+1

def verifG():
    global oursG
    global rep1
    #OURS
    oursG = ours
    resultat1.config(text=oursG)
    rep1 = str(reponse1.get())
    rep1 = int(rep1)
    print(rep1)
    if rep1 == oursG :
        textO.config(text="Félicitations ! Vous avez trouvé le bon nombre d'Ours !")
    else:
        textO.config(text="Désolé ! C'est une mauvaise réponse")
	#PHOQUE
    phoqueG = phoque
    resultat2.config(text=phoqueG)
    rep2 = str(reponse2.get())
    rep2 = int(rep2)
    if rep2==phoqueG:
        textP.config(text="Félicitations ! Vous avez trouvé le bon nombre de Phoque !")
    else:
        textP.config(text="Désolé ! C'est une mauvaise réponse")
    #TROU
    rep3 = 0
    trouG = trou
    resultat3.config(text=trouG)
    rep3 = str(reponse3.get())
    rep3 = int(rep3)
    if rep3==trouG:
        textT.config(text="Félicitations ! Vous avez trouvé le bon nombre de Trous !")
    else:
        textT.config(text="Désolé ! C'est une mauvaise réponse")
#LAUNCHER
a = (a+1)
if a == 1:
	menu()
else:
	print("erreur")

#FIN PROGRAMME------------------------------------------------------------------
fen.mainloop()
