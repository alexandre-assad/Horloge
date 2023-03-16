
import asyncio
import time
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd


h = 16
m = 30
s = 0
horloge = (h,m,s)
alarme = (-1,-1,-1)
def afficher_heure(heure,mode):
    global horloge,h,m,s,Heure_entry
    if type(heure) != tuple:
        heure = list(heure.split(","))
    h = int(heure[0])
    m = int(heure[1])
    s = int(heure [2])
    horloge = (h,m,s)
    if mode == "12H":
        if h > 12:
            return "{}:{}:{} PM".format(h-12,m,s)
        else:
            return "{}:{}:{} AM".format(h,m,s)
    else:
        return "{}:{}:{}".format(h,m,s)
def changemod():
    global mode
    if mode == "24H":
        mode = "12H"
    else:
        mode = "24H"
async def tick():
    global horloge, h, m, s
    await asyncio.sleep(0.1)
    s+=1
    if s > 60:
        s = 0
        m += 1
        if m > 60:
            m = 0
            h+=1
            if h > 24:
                h = 0
    horloge = (h,m,s)
    return horloge

def regler_alarme(heure):
    global horloge,alarme,Alarme_entry
    if type(heure) != tuple:
        heure = list(heure.split(","))
        h = int(heure[0])
        m = int(heure[1])
        s = int(heure [2])
    alarme = (h,m,s)
    Alarme_entry.delete(0,END)
    return alarme
    
def pause():
    global pause_state
    if pause_state == "pause":
        pause_state = "unpause"
    else:
        pause_state="pause"
def clearheure(): #Efface le champs et applique la fonction pour actualiser l'heure
    global Heure_entry,mode
    afficher_heure(Heure_entry.get(),mode)
    Heure_entry.delete(0,END)
    
def config_heure():
    global horloge, heureText,alarme,alarmeText,pause_state
    if pause_state != "pause":
        horloge = asyncio.run(tick())
        print("a")
    if horloge == alarme:
        alarmeText.config(fg="blue")
        alarme = (-1,-1,-1)
    else:   
        alarmeText.config(fg="grey")
    heureText.config(text=str(afficher_heure(horloge,mode)))
    fenetre.after(999,config_heure)
alarme = (-1,-1,-1)
pause_state = "unpause"
mode = "24H"

fenetre = Tk()
fenetre.title("Accueuil")
fenetre.geometry("1080x720")
fenetre.minsize(480,360)
fenetre.config(background="grey")
frame = Frame(fenetre)
frame.config(background="grey")
frame.pack(expand=YES)
horloge = asyncio.run(tick())
AfficherText = Label(frame, text="L'heure Actuelle :",background="grey",font=("Arial",20))
AfficherText.grid(column=0,row=0)
heureText = Label(frame, text=str(afficher_heure(horloge,mode)),background="grey",font=("Arial",20))
heureText.grid(column=1,row=0)
ReglerHeureText = Label(frame, text="Regler l'heure :",background="grey",font=("Arial",20))
ReglerHeureText.grid(column=0,row=1)
Heure_entry= Entry(frame)
Heure_entry.grid(column=1,row=1)
ReglerHeureButton = Button(frame, text="Regler l'heure",font=("Arial",10),width=9, background="Blue",fg="white",command=lambda :clearheure())
ReglerHeureButton.grid(column=0,row=2)
ReglerAlarmeText = Label(frame, text="Mettre une alarme :",background="grey",font=("Arial",20))
ReglerAlarmeText.grid(column=0,row=3)
Alarme_entry= Entry(frame)
Alarme_entry.grid(column=1,row=3)
ReglerAlarmeButton = Button(frame, text="Regler alarme",font=("Arial",10),width=9, background="Blue",fg="white",command=lambda :regler_alarme(Alarme_entry.get()))
ReglerAlarmeButton.grid(column=0,row=4)
ChangerModeText = Label(frame, text="Mettre Mode 12H :",background="grey",font=("Arial",20))
ChangerModeText.grid(column=0,row=5)
Modebouton = Checkbutton(frame, text="Mode 12H",background="grey",command=changemod)
Modebouton.grid(column=1,row=5)
PauseText = Label(frame, text="Mettre en pause:",background="grey",font=("Arial",20))
PauseText.grid(column=0,row=6)
Pausebouton = Checkbutton(frame, text="Pause",background="grey",command=pause)
Pausebouton.grid(column=1,row=6)
alarmeText = Label(frame,text="L'ALARME SONNE... DING DONG",fg="grey",background="grey")
alarmeText.grid(column=0,row=7)
config_heure()
fenetre.mainloop()

    
        
# while True:
#     alarme = (-1,-1,-1)
#     pause_state = ""
#     mode = "24H"
#     action = int(input("""Que Voulez Vous faire ?
#     (0) Afficher l'heure
#     (1) Regler l'heure
#     (2) Mettre une alarme 
#     (3) Changer le mode 12H/24H
#     (4) Mettre en pause/depause
#     (5) Quitter                           
    
#     """))
#     if action == 0:
#         afficher_heure(horloge,mode)
#     elif action == 1:
#         newheure = tuple(input("Quel heure vous voulez, écrire de la forme (h,m,s)"))
#         afficher_heure(newheure,mode)
#     elif action == 2:
#         alarme = tuple(input("Quel heure pour l'alarme vous voulez, écrire de la forme (h,m,s)"))
        
#     elif action == 3:
#         if mode == "24H":
#             mode = "12H"
#         else:
#             mode = "24H"
#     elif action == 4:
#         if pause_state == "pause":
#             pause_state = ""
#         else:
#             pause_state = "pause"
#     elif action == 5:
#         break
#     if pause(pause_state) != True:
#         horloge = asyncio.run(tick())
#         afficher_heure(horloge,mode)
#     regler_alarme(alarme)