import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear figura
fig, ax = plt.subplots(figsize=(4,6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 5)
ax.set_aspect("equal")
ax.axis("off")

# Tallo
ax.plot([0, 0], [0, 3], color="#ccff33", linewidth=6)

# Hojas
ax.fill([-0.2, -1, 0], [1, 0.5, 0.5], color="#228B22", alpha=0.6)
ax.fill([0.2, 1, 0], [1.2, 0.8, 0.5], color="#228B22", alpha=0.6)

# Pétalos
petalos = []
for angle in np.linspace(0, 2*np.pi, 7)[:-1]:
    petalo = plt.Circle((0.3*np.cos(angle), 3 + 0.3*np.sin(angle)),
                        radius=0.5, color="#ffb6c1", alpha=0.8)
    ax.add_patch(petalo)
    petalos.append(petalo)

# Animación
def animar(frame):
    escala = 1 + 0.1*np.sin(frame/10)
    for i, petalo in enumerate(petalos):
        angle = np.linspace(0, 2*np.pi, 7)[:-1][i]
        petalo.center = (0.3*escala*np.cos(angle), 3 + 0.3*escala*np.sin(angle))
        petalo.set_radius(0.5*escala)

ani = FuncAnimation(fig, animar, frames=200, interval=50)

# Guardar GIF
ani.save("tulipan.gif", writer="pillow", fps=20)
print("✅ GIF generado: tulipan.gif")
