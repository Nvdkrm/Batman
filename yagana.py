import tkinter as tk
from tkinter import messagebox
import random

# Variable pour suivre si l'utilisateur a répondu
answered = False

# Fonction appelée lorsque l'utilisateur clique sur "Bien sûr, avec plaisir"
def on_yes_click():
    global answered
    answered = True
    
    # Affichage du message final avec un effet
    label_final.config(text="Parfait ! Je viendrai te chercher avec la Batmobile. 🦇", font=("Arial", 18, "bold"), fg="#ffffff")
    label_final.place(relx=0.5, rely=0.4, anchor="center")
    
    # Animation de la Batmobile
    label_final.after(1000, show_batmobile)

    # Désactivation des boutons après la réponse
    btn_yes.config(state="disabled")
    btn_no.config(state="disabled")

# Fonction pour afficher l'image de la Batmobile et l'animer
def show_batmobile():
    # Ajouter une image de la Batmobile
    batmobile_image = tk.PhotoImage(file="batmobile.png")  # Remplacer par le chemin de l'image
    batmobile_label.config(image=batmobile_image)
    batmobile_label.image = batmobile_image
    batmobile_label.place(relx=0.5, rely=0.6, anchor="center")
    
    # Animer la Batmobile pour qu'elle "arrive" à l'utilisateur
    batmobile_label.after(500, move_batmobile)

# Déplacer l'image de la Batmobile pour simuler un mouvement
def move_batmobile():
    x_move = random.randint(-50, 50)
    y_move = random.randint(-50, 50)
    batmobile_label.place(x=batmobile_label.winfo_x() + x_move, y=batmobile_label.winfo_y() + y_move)

# Fonction appelée lorsque l'utilisateur survole ou tente de cliquer sur "Lol non merci"
def on_no_hover(event):
    new_x = random.randint(0, root.winfo_width() - btn_no.winfo_width() - 20)
    new_y = random.randint(0, root.winfo_height() - btn_no.winfo_height() - 20)
    btn_no.place(x=new_x, y=new_y)

# Fonction appelée lorsqu'on tente de fermer la fenêtre
def on_close():
    if not answered:
        messagebox.showwarning("Attention", "Vous devez d'abord donner votre réponse avant de quitter !")
    else:
        root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Surprise...!")
root.geometry("800x600")  # Taille de la fenêtre
root.resizable(False, False)  # Empêche le redimensionnement

# Configure la fermeture personnalisée
root.protocol("WM_DELETE_WINDOW", on_close)

# Fond coloré
root.configure(bg="#282c34")  # Couleur gris foncé moderne

# Conteneur pour le texte et les boutons
container = tk.Frame(root, bg="#3a3f4b", bd=5, relief="ridge")
container.pack(pady=50)

# Titre
label = tk.Label(
    container,
    text="Aimerais-tu faire un date avec Batman ?",
    font=("Arial", 18, "bold"),
    bg="#3a3f4b",
    fg="#ffffff"
)
label.pack(pady=20)

# Bouton "Bien sûr, avec plaisir"
btn_yes = tk.Button(
    container,
    text="Bien sûr, avec plaisir",
    command=on_yes_click,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="raised"
)
btn_yes.pack(pady=10)

# Bouton "Lol non merci, je suis pas un bolosse"
btn_no = tk.Button(
    root,
    text="Lol non merci, je suis pas un bolosse",
    bg="#f44336",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised",
    wraplength=150
)
btn_no.place(x=200, y=300)

# Déplacement du bouton "Non" au survol
btn_no.bind("<Enter>", on_no_hover)
btn_no.bind("<Button-1>", on_no_hover)

# Label pour afficher la réponse finale
label_final = tk.Label(root, text="", bg="#282c34", fg="#ffffff", font=("Arial", 16, "bold"))

# Label pour afficher l'image de la Batmobile
batmobile_label = tk.Label(root)

# Lancement de l'interface
root.mainloop()