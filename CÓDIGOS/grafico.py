import numpy as np
from matplotlib import pyplot as plt
from numpy.polynomial import Polynomial

def trajectory(file, color, ax, first_plot, distance):
    data = np.loadtxt(file, comments='#')
    data = data.transpose()
    x = data[1]
    y = data[2]
    coefficients = Polynomial.fit(x, y, 2).convert()
    print(f"Fit Coefficients for {file}: {coefficients}")
    ax.plot(x, y, 'o', color=color)
    ax.set_ylim(-1, 10)
    ax.set_xlim(-1, 30) 
    ax.set_xlabel(distance)

    if first_plot:
        ax.set_ylabel("Height (m)")

fig, axs = plt.subplots(1, 4, figsize=(15, 5), sharey=True, sharex=True)

distance_labels = ["20,14m","22,10m", "21,26m", "17,97m"]

trajectory(r"C:\Users\icjunior\Desktop\RocketPET\dados\lançamento1\lancamento.dat", "#220753", axs[0], first_plot=True, distance=distance_labels[0])
trajectory(r"C:\Users\icjunior\Desktop\RocketPET\dados\lançamento2\lancamento.dat", "#fa6e98", axs[1], first_plot=False, distance=distance_labels[1])
trajectory(r"C:\Users\icjunior\Desktop\RocketPET\dados\lançamento3\lancamento.dat", "#07AD60", axs[2], first_plot=False, distance=distance_labels[2])
trajectory(r"C:\Users\icjunior\Desktop\RocketPET\dados\lançamento4\lancamento.dat", "#e77020", axs[3], first_plot=False, distance=distance_labels[3])

axs[0].set_title("Trajectory 1 (P= 3-4atm)")
axs[1].set_title("Trajectory 2 (P= 3-4atm)") 
xticks = axs[1].xaxis.get_major_ticks()
xticks[-4].label1.set_visible(False)

axs[2].set_title("Trajectory 3 (P= 3-4atm)")
xticks = axs[2].xaxis.get_major_ticks()
xticks[-4].label1.set_visible(False)

axs[3].set_title("Trajectory 4 (P= 4-5atm)")
xticks = axs[3].xaxis.get_major_ticks()
xticks[-4].label1.set_visible(False)

fig.suptitle("RocketPET: McQueen", fontsize=16)

plt.tight_layout()
plt.subplots_adjust(top=0.85, wspace=0)

plt.savefig(r"C:\Users\icjunior\Desktop\RocketPET\IMAGENS\trajetorias_grafico.jpg")
plt.show()
