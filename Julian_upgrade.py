"""               Made by Florain Marcoz and Malezieux Julien                """
"""                      All Rights Reserved | No adds                       """
#IMPORT-------------------------------------------------------------------------
from random import*
from math import*
from tkinter import*
#FENETRE------------------------------------------------------------------------
fen =Tk()
fen.geometry("950x600")
fen.title("Les Maths Polaire (V1.3.3)")
fen.config(bg="#3D8771")
#IMAGES-------------------------------------------------------------------------
de1=PhotoImage(file="Images/d1.gif")
de2=PhotoImage(file="Images/d2.gif")
de3=PhotoImage(file="Images/d3.gif")
de4=PhotoImage(file="Images/d4.gif")
de5=PhotoImage(file="Images/d5.gif")
de6=PhotoImage(file="Images/de6.gif")
#VARIABLE-----------------------------------------------------------------------
B = 0
#FONCTION-----------------------------------------------------------------------
#ACCEUIL------------------------------------------------------------------------
def Page_Acceuil():
    Regle = Button(fen,text="Comment jouer ?  ",command=Page_Regle,font=("calibri","15"))
    Regle.place(x=100,y=200)
    Lancer_Une_Partie = Button(fen,text="Lancer une partie  ",command=Page_Jeux,font=("calibri","15"))
    Lancer_Une_Partie.place(x=100,y=250)
    Graphique = Button(fen,text="Options graphique",command=Page_Graphics,font=("calibri","15"))
    Graphique.place(x=100,y=300)
    global Regle,Lancer_Une_Partie,Graphique
#ACCEUIL_KILL-------------------------------------------------------------------
def Page_Acceuil_Kill():
    Regle.destroy()
    Lancer_Une_Partie.destroy()
    Graphique.destroy()
#REGLE--------------------------------------------------------------------------
def Page_Regle():
    tex0 = Label(fen, text="Comment jouer ?",bg="#3D8771",font=("calibri","20","bold","underline"))
    tex0.place(x=50,y=145)
    tex1 = Label(fen, text="Les trous sont aux centres de la banquise",bg="#3D8771",font=("calibri","18"))
    tex1.place(x=50,y=180)
    tex2 = Label(fen, text="Les ours restent toujours autours d'un trou afin d'attrapper un phoque.",bg="#3D8771",font=("calibri","18"))
    tex2.place(x=50,y=210)
    tex3 = Label(fen, text="Soustraire à 7 le nombre des ours pour chaque banquise",bg="#3D8771",font=("calibri","18"))
    tex3.place(x=50,y=240)
    Retour = Button(fen,text="Retour",bg="#D27C8B",command=Page_RegleKill,font=("justify"))
    Retour.place(x=650,y=500)
    global tex0,tex1,tex2,tex3,Retour
    Page_Acceuil_Kill()
#REGLE_KILL---------------------------------------------------------------------
def Page_RegleKill():
    tex0.destroy()
    tex1.destroy()
    tex2.destroy()
    tex3.destroy()
    Retour.destroy()
    Page_Acceuil()
#GAME---------------------------------------------------------------------------
def Page_Jeux():
    #Ours
    text1 = Label(fen, text="Nombre d'ours:",bg="#3D8771")
    text1.place(x=50,y=270)
    reponse1=Entry(width=20)
    reponse1.place(x=170,y=270)
    #Phoques
    text2 = Label(fen, text="Nombre de phoques:",bg="#3D8771")
    text2.place(x=50,y=295)
    reponse2=Entry(width=20)
    reponse2.place(x=170,y=295)
    #Trous
    text3 = Label(fen, text="Nombre de trous:",bg="#3D8771")
    text3.place(x=50,y=320)
    reponse3=Entry(width=20)
    reponse3.place(x=170,y=320)
    #Canvas
    if B == 0:
        can = Canvas(fen, width=250, height=250)
        can.place(x=550, y=180)
        can.configure(bg="skyblue")
    elif B == 1:
        can = Canvas(fen, width=250, height=250)
        can.place(x=550, y=180)
        can.configure(bg="#FE4747")
    elif B == 2:
        can = Canvas(fen, width=250, height=250)
        can.place(x=550, y=180)
        can.configure(bg="#B4D23A")
    else:
        print ("Erreur Graphique")
    #Bouton
    Retour = Button(fen,text="Retour",bg="#D27C8B",command=Page_JeuxKill1)
    Retour.place(x=650,y=500)
    Jouer = Button(fen,text="Jouer",bg="#D27C8B",command=play)
    Jouer.place(x=585,y=500)
    #Résultats
    resultat1 = Label(fen, text="-",bg="#3D8771")
    resultat1.place(x=370,y=370)
    resultat2 = Label(fen, text="-",bg="#3D8771")
    resultat2.place(x=370,y=390)
    resultat3 = Label(fen, text="-",bg="#3D8771")
    resultat3.place(x=370,y=410)
    #Correction
    textOurs = Label(fen, text="Avez-vous la bonne réponse pour le nombre Ours ?",bg="#3D8771")
    textOurs.place(x=50,y=370)
    textPhoque = Label(fen, text="Avez-vous la bonne réponse pour le nombre Phoques ?",bg="#3D8771")
    textPhoque.place(x=50,y=390)
    textTrou = Label(fen, text="Avez-vous la bonne réponse pour le nombre de Trous ?",bg="#3D8771")
    textTrou.place(x=50,y=410)
    global text1,text2,text3,reponse1,reponse2,reponse3,can,Retour,Jouer
    global resultat1,resultat2,resultat3,textOurs,textPhoque,textTrou
    #Fonction
    Page_Acceuil_Kill()
#GAME_KILL1---------------------------------------------------------------------
def Page_JeuxKill1():
    text1.destroy()
    reponse1.destroy()
    resultat1.destroy()
    text2.destroy()
    reponse2.destroy()
    resultat2.destroy()
    text3.destroy()
    reponse3.destroy()
    resultat3.destroy()
    textOurs.destroy()
    textPhoque.destroy()
    textTrou.destroy()
    Jouer.destroy()
    can.destroy()
    Retour.destroy()
    #Fonction
    Page_Acceuil()
#GAME_KILL2---------------------------------------------------------------------
def Page_JeuxKill2():
    text1.destroy()
    reponse1.destroy()
    resultat1.destroy()
    text2.destroy()
    reponse2.destroy()
    resultat2.destroy()
    text3.destroy()
    reponse3.destroy()
    resultat3.destroy()
    can.destroy()
    Retour.destroy()
    Jouer.destroy()
    textOurs.destroy()
    textPhoque.destroy()
    textTrou.destroy()
    Recommencer.destroy()
    #Fonction
    Page_Acceuil()
#GRAPHIQUE----------------------------------------------------------------------
def Page_Graphics():
    global vert,fondBan,fond
    texte0 = Label(fen,bg="#3D8771",text="Paramètres :",font=("calibri","18","bold","underline"))
    texte0.place(x=50,y=140)
    canvas= Label(fen,bg="#3D8771",text="Tapis de jeu",font=("calibri","15"))
    canvas.place(x=120,y=180)
    canvasBleu = Button(fen,bg="#D27C8B",text="Bleu ",command=CanvasBleu)
    canvasBleu.place(x=120,y=220)
    canvasRouge = Button(fen,bg="#D27C8B",text="Rouge",command=CanvasRouge)
    canvasRouge.place(x=170,y=220)
    canvasVert = Button(fen,bg="#D27C8B",text="Vert ",command=CanvasVert)
    canvasVert.place(x=230,y=220)
    Retour = Button(fen,bg="#D27C8B",text="Retour",command=Page_GraphicsKill)
    Retour.place(x=650,y=500)
    Page_Acceuil_Kill()
    global texte0,Retour,canvas,canvasBleu,canvasRouge,canvasVert
#GRAPHIQUE_KILL-----------------------------------------------------------------
def Page_GraphicsKill():
    texte0.destroy()
    canvas.destroy()
    canvasBleu.destroy()
    canvasRouge.destroy()
    canvasVert.destroy()
    Retour.destroy()
    Page_Acceuil()
#SOUS_GRAPHIQUE-----------------------------------------------------------------
def CanvasBleu():
    B = 0
    global B
def CanvasRouge():
    B = 1
    global B
def CanvasVert():
    B = 2
    global B

#LAUNCHER_GAME-------------------------------------------------------------------
def play():
    cube1()
    verification = Button(fen, text="Vérifier ?", command = verifG,bg="#3D8771")
    verification.place(x=330,y=295)
    Recommencer = Button(fen,text="Recommencer",bg="#D27C8B",command=restart)
    Retour.destroy()
    Jouer.destroy()
    global verification,Recommencer
#BANQUISE_1---------------------------------------------------------------------
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

#VERIFICATION-------------------------------------------------------------------
def verifG():
    #OURS
    oursG = ours
    resultat1.config(text=oursG)
    rep1 = str(reponse1.get())
    rep1 = int(rep1)
    if rep1==oursG:
        textOurs.config(text="Félicitations ! Vous avez trouvé le bon nombre d'Ours !")
    else:
        textOurs.config(text="La réponse qu'il fallait trouver pour les ours était:")
    #PHOQUE
    phoqueG = phoque
    resultat2.config(text=phoqueG)
    rep2 = str(reponse2.get())
    rep2 = int(rep2)
    if rep2==phoqueG:
        textPhoque.config(text="Félicitations ! Vous avez trouvé le bon nombre de Phoque !")
    else:
        textPhoque.config(text="La réponse qu'il fallait trouver pour les phoques était:")
    #TROUS
    trouG = trou
    resultat3.config(text=trouG)
    rep3 = str(reponse3.get())
    rep3 = int(rep3)
    if rep3==trouG:
        textTrou.config(text="Félicitations ! Vous avez trouvé le bon nombre de Trous !")
    else:
        textTrou.config(text="La réponse qu'il fallait trouver pour les trous était:")
    #BOUTON
    Retour = Button(fen,text="Retour",bg="#D27C8B",command=Page_JeuxKill2)
    Retour.place(x=655,y=500)
    Recommencer.place(x=550,y=500)
    verification.destroy()
    global Retour
#RECOMMENCER--------------------------------------------------------------------
def restart():
    Recommencer.destroy()
    play()
#
#LAUNCHER-----------------------------------------------------------------------
#
a = 1
if a == 1:
    Page_Acceuil()
else:
    print=("Erreur de lancement de la variable a")
#PARTIE_GLOBAL------------------------------------------------------------------
Titre = Label(fen,text="Les Maths Polaires",bg="red",font=("calibri","45"))
Titre.place(x=50,y=20)
Sortie = Button(fen, text="Quitter le jeu.", command = fen.destroy,bg="#D27C8B")
Sortie.place(x=720,y=500)
#END----------------------------------------------------------------------------
fen.mainloop()