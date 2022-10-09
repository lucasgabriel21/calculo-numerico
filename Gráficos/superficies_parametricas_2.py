import numpy as np
from numpy import cos, sin, pi, sqrt
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d

# Parâmetros
a = 2
b = sqrt(2)
theta = np.linspace(0, 2*pi, 50)
u = np.linspace(0, 5, 50)

# Meshgrid para criar malha do gráfico
u, theta = np.meshgrid(u, theta)

# Equações paramétricas:
x = u
y = a*cos(theta)
z = b*sin(theta)

# Ajuste da figura
fig = plt.figure('Superfície paramétrica')
ax = fig.add_subplot(111, projection='3d')

# Plot dos dados
h = ax.plot_surface(x, y, z, cmap='jet', edgecolor='k')

# Colorbar para visualização
# fig.colorbar(h)

# Adicionar labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title('Superfície')

# Ajuste de eixos
# ax.axis('square')

# Apresenta a figura
plt.show()
