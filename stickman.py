import tkinter as tk

# Fonction pour animer les bras
def animate_arms():
    # Obtenir les coordonnées actuelles des bras
    left_arm_coords = canvas.coords(left_arm)
    right_arm_coords = canvas.coords(right_arm)
    
    # Déplacer les bras vers le haut et vers le bas
    if left_arm_coords[1] == 170:
        canvas.move(left_arm, 0, -10)
        canvas.move(right_arm, 0, -10)
    else:
        canvas.move(left_arm, 0, 10)
        canvas.move(right_arm, 0, 10)
    
    # Planifier l'animation pour la prochaine frame
    canvas.after(500, animate_arms)

# Création de la fenêtre principale
main_window = tk.Tk()
main_window.title("Stickman")
main_window.geometry("400x400")

canvas = tk.Canvas(main_window, height=400, width=400)
canvas.pack()

# Dessiner le stickman
head = canvas.create_oval(100, 50, 200, 150, fill="lightgreen", width=0)
body = canvas.create_line(150, 150, 150, 250, fill='green', width=4)
left_arm = canvas.create_line(150, 170, 100, 220, fill="blue", width=4)
right_arm = canvas.create_line(150, 170, 200, 220, fill="red", width=4)
left_leg = canvas.create_line(150, 250, 100, 300, fill="yellow", width=4)
right_leg = canvas.create_line(150, 250, 200, 300, fill="purple", width=4)

# Démarrez l'animation des bras
animate_arms()

# Boucle principale
main_window.mainloop()
