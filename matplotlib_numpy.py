import numpy as np
import matplotlib.pyplot as plt

# task 01

x_values = np . linspace ( 1 , 10 , 10) # Permet de découper entre deux points (a,b) en part égales, en fonction du nombre de découpage (a,b,c)

print(x_values)

# task 02

# Coordonnées des points
x_points = [0, 1, 2, 3]
y_points = [12, 32, 42, 52]

plt.scatter(x_points, y_points, label="Points")

plt.title("Points dans un graphique")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")

# Affiche la légende
plt.legend()

# Affiche le graphique
### plt.show() ###

# task 03

def displayPoints(points):
    
    if not points:
        raise ValueError('Le tableau ne peut pas être vide')
    
    x_label, y_label = zip(*points)

    plt.plot(x_label, y_label, marker='o', linestyle='', c='yellow')

    plt.title('Chart of points')
    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')

    plt.grid(True)

    plt.show()  

points = [(0, 12), (1, 10), (2, 15), (3, 8)]
displayPoints(points)

