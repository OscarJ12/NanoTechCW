import math
# Constants
hbar = 1.054571e-34  # Reduced Planck's constant in J.s
m0 = 9.10938356e-31  # Free electron rest mass in kg
me_star = 0.043 * m0  # Effective mass of electron in kg
mhh_star = 0.384 * m0  # Effective mass of heavy hole in kg
L = 13.88e-9  # Quantum well width in meters

# Function to calculate the energy of confined states
def confined_energy(n, m_star, L):
    return (hbar**2 * math.pi**2 * n**2) / (2 * m_star * L**2)

# Calculate energies for the first and second confined electron states
E_1e = confined_energy(1, me_star, L)  # n = 1
E_2e = confined_energy(2, me_star, L)  # n = 2

# Calculate energies for the first and second confined heavy hole states
E_1hh = confined_energy(1, mhh_star, L)  # n = 1
E_2hh = confined_energy(2, mhh_star, L)  # n = 2

print("Electron E1:", E_1e, "Electron E2:", E_2e, "Hole E1:", E_1hh, "Hole E2:", E_2hh)
