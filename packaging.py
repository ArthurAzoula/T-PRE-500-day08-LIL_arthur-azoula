import tkinter as tk
from PIL import Image, ImageTk

# Function to update the live score
def update_score():
    score.set(score.get() + 10)

# Function to update the life bar
def update_life():
    life.set(life.get() - 10)
    if life.get() <= 0:
        game_over_label.config(text="Game Over", font=("Arial", 24), fg="red")

# Create the main window
root = tk.Tk()
root.title("Game GUI")

# Initialize variables
score = tk.IntVar()
life = tk.IntVar()
score.set(0)
life.set(100)

# Create a frame for the game elements
game_frame = tk.Frame(root, bg="lightblue")
game_frame.pack(pady=20)

# Score label
score_label = tk.Label(game_frame, text="Score:", font=("Arial", 16), bg="lightblue")
score_label.pack(side=tk.LEFT, padx=10)
score_display = tk.Label(game_frame, textvariable=score, font=("Arial", 16), bg="lightblue")
score_display.pack(side=tk.LEFT, padx=10)

# Life bar
life_label = tk.Label(game_frame, text="Life:", font=("Arial", 16), bg="lightblue")
life_label.pack(side=tk.LEFT, padx=10)
life_bar = tk.Label(game_frame, textvariable=life, bg="red", width=20, font=("Arial", 16))
life_bar.pack(side=tk.LEFT, padx=10)

# Menu button
menu_button = tk.Button(root, text="Menu", font=("Arial", 16))
menu_button.pack()

# Time display
time_label = tk.Label(root, text="Time: 00:00", font=("Arial", 16))
time_label.pack()

# Inventory
inventory_label = tk.Label(root, text="Inventory:", font=("Arial", 16))
inventory_label.pack()
inventory_listbox = tk.Listbox(root, font=("Arial", 14))
inventory_listbox.pack()

# Image
image = Image.open("background.jpg")
image = image.resize((800, 800), Image.ADAPTIVE)  # Redimensionner l'image si nécessaire
photo = ImageTk.PhotoImage(image)

# Canvas dans la frame
canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Game Over label (hidden initially)
game_over_label = tk.Label(root, text="", font=("Arial", 24), fg="red")
game_over_label.pack()
game_over_label.grid_forget()

# Update score and life every second (for demonstration purposes)
root.after(1000, update_score)
root.after(2000, update_life)

# Start the main loop
root.mainloop()
