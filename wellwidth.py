import numpy as np

# Constants
h = 6.62607015e-34  # J·s
c = 3e8  # m/s
hbar = 1.054571e-34  # J·s
m0 = 9.10938356e-31  # kg
lambda_transition = 1.55e-6  # m
E_transition = h * c / lambda_transition
E_gap = 0.75 * 1.60218e-19  # Convert eV to J
me_star_e1 = 0.043 * m0
mh_star_hh = 0.384 * m0

# Calculate the ideal quantum well width algebraically
def compute_ideal_width_algebraic():
    return np.sqrt((np.pi**2 * hbar**2 / (2 * (E_transition - E_gap))) * (1/me_star_e1 + 1/mh_star_hh))

# Get the result
ideal_width_algebraic_corrected = compute_ideal_width_algebraic()

# Print the result
print(f"Ideal quantum well width using corrected electron effective mass and heavy-hole effective mass: {ideal_width_algebraic_corrected*1e9:.2f} nm")
