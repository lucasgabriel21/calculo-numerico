import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d

# Parâmetros
Ro = 2
r = 1
tht = np.linspace(0, 2*pi, 50)
phi = np.linspace(0, 2*pi, 50)

# Meshgrid para criar malha do gráfico
tht, phi = np.meshgrid(tht, phi)

# Equações paramétricas:
x = (Ro + r*cos(tht))*cos(phi)
y = (Ro + r*cos(tht))*sin(phi)
z = r*sin(tht)

# Ajuste da figura
fig = plt.figure('Superfície paramétrica')
ax = fig.add_subplot(111, projection='3d')

# Plot dos dados
h = ax.plot_surface(x, y, z, cmap='jet', edgecolor='k')

# Colorbar para visualização
fig.colorbar(h)

# Adicionar labels
ax.set_xlabel('X')
ax.set_xlabel('Y')
ax.set_xlabel('Z')

# Título
ax.set_title('Superfície')

# Ajuste de eixos
# ax.axis('square')

# Apresenta a figura
plt.show()
