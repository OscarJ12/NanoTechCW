import numpy as np
from scipy.integrate import quad

# Quantum well width
L = 13.88e-9  # Quantum well width in meters

# First state wave function for the electron
def psi_1(x, L):
    return np.sqrt(2/L) * np.sin(np.pi * x / L)

# Probability density function for the electron
def probability_density_electron(x, L):
    return psi_1(x, L)**2

# Integrate the probability density over the given intervals for the electron
P_2_4_electron = quad(probability_density_electron, 2e-9, 4e-9, args=(L))[0]
P_6_8_electron = quad(probability_density_electron, 6e-9, 8e-9, args=(L))[0]
P_2_4_electron, P_6_8_electron
