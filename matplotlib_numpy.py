import numpy as np
import matplotlib.pyplot as plt
import math

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

# task 04 

def plt_fct(func, x_min, x_max):
    x_values = np.linspace(x_min, x_max, 1000)
    
    # Utilisez np.vectorize pour appliquer la fonction func à chaque valeur x
    func_vectorized = np.vectorize(func)
    y_values = func_vectorized(x_values)

    plt.plot(x_values, y_values)
    plt.title("Graph function")
    plt.xlabel("X-Axis")
    plt.ylabel('Y-Axis')
    plt.grid(True)
    plt.show()

# Exemple 1: Tracer la fonction math.sin(x) dans la plage [0, 50]
plt_fct(math.sin, 0, 50)

# Exemple 2: Tracer la fonction f(x) = x^2 + 3x + 2 dans la plage [-100, 200]
def f(x):
    return x**2 + x*3 + 2
plt_fct(f, -100, 200)

# Exemple 3: Tracer la fonction f(x) = x^2 dans la plage [-10, 10]
plt_fct(lambda x: x**2, -10, 10)

# Exemple 4: Tracer la fonction f(x) = 1/x dans la plage [-100, 100]
plt_fct(lambda x: 1/x, -100, 100)

# Ici lambda va permettre de faire une fonction sans qu'on ai besoin de la déclaré, comme fait avec f(x), cela va directement être considéré comme une fonction et cette fonction va être appliqué pour chaque valeur de x

