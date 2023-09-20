import tkinter as tk
from PIL import Image, ImageTk

# Fonction pour gérer le clic sur le bouton
def on_button_click():
    entry_text = entry.get()
    label.config(text=f"Texte saisi : {entry_text.upper()}")

# Fenêtre principale
main_window = tk.Tk()

# Configuration de la fenêtre
main_window.config(width=400, height=300)
main_window.title('Fenêtre principale')

# Création du LabelFrame
labelFrame = tk.LabelFrame(main_window, text='Premier LabelFrame dans Tk')
labelFrame.pack(fill="both", expand="yes")

# Champ d'entrée
entry = tk.Entry(labelFrame)
entry.pack()

# Bouton
button = tk.Button(labelFrame, text="Cliquez-moi", command=on_button_click)
button.pack()

# Étiquette pour afficher le texte saisi
label = tk.Label(labelFrame, text="")
label.pack()

# Canvas dans la frame
canvas = tk.Canvas(main_window, height=800, width=800)
canvas.pack()

# Charger une image
image = Image.open("olivier.jpg")
image = image.resize((800, 800), Image.ADAPTIVE)  # Redimensionner l'image si nécessaire
photo = ImageTk.PhotoImage(image)

# Afficher l'image sur le canevas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# conserver une référence à l'image pour éviter qu'elle ne soit garbage collected
canvas.image = photo

# Boucle principale pour afficher la fenêtre
main_window.mainloop()
