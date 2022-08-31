"""
Quantity Symbol Value


Example to interpret value:
---------------------------
Newtonian constant of gravitation
 $ G $
 Numerical value                 6.674 30 x 10-11 m^3 kg^-1 s^-2
 Standard uncertainty	         0.000 15 x 10-11 m^3 kg^-1 s^-2
 Relative standard uncertainty	 2.2 x 10-5
 Concise form	                 6.674 30(15) x 10-11 m^3 kg^-1 s^-2

References:
    https://physics.nist.gov/cuu/Constants/index.html
    https://web.archive.org/web/20181119214326/https://www.bipm.org/utils/common/pdf/CGPM-2018/26th-CGPM-Resolutions.pdf
All ascii values: https://physics.nist.gov/cuu/Constants/Table/allascii.txt
"""
# Avogadro’s number N_A 6.022 140 76 × 10^23 / mol^-1   [1/mole]
AVOGADRO_NUMBER_N_A = 6.02214076 * (10**23)
# Boltzmann’s constant kB 1.380649 × 10^−23 J/K  [joule/kelvin]
BOLTZMANN_CONSTANT_kB = 1.380649
# Coulomb constant k e = 1/ 4πε_0 8.987551787...×10^9 N ⋅m^2 ⋅C^−2 [(Newton * meters * meters) / (coulombs * coulombs)]
Coulomb_constant_k_e = 8.987551787 * (10 ** 9)
# Elementary charge e 1.602 176 634 × 10^−19 C   [coulombs]
ELEMENTARY_CHARGE_e = 1.602176634 * (10 ** -19)
# Electron mass m e 9.109 383 7015(28) × 10^−31 kg  [kilograms]
ELECTRON_CHARGE_m_e = 9.1093837015 * (10 ** -31)
# Gravitational constant G 6.67430... × 10^−11 N ⋅m^2 ⋅kg^−2  [(Newton * meters * meters) / (kilograms * kilograms)]
GRAVITATIONAL_CONSTANT_G = 6.67430 * (10 ** -11)
# Neutron mass m n 1.674 927 498 04(74) × 10^−27 kg  [kilograms]
NEUTRON_MASS_m_n = 1.67492749804 * (10 ** -27)
# Permeability of free space µ_0      4π × 10^−7  T ⋅m/A
#                                or   1.256 637 062 12 x 10 ^-6 N/A^2  [Newton/ (Ampere * Ampere)]
PERMEABILITY_mu_0 = 1.25663706212
# Permittivity of free space (vacuum electric permittivity) ε_0 = 1/ µ_0c^2
#                                            8.854 187 8128 ×10^−12  C^2 / N ⋅m2  [(coulombs * coulombs * Newoton) * (meters * meteres)]

PERMITTIVITY_e_0 = 8.8541878128
# Planck’s constant h 6.62607015 * 10^−34 J ⋅s  [joules * seconds]
#                                          or m^2 kg/s [(meters * meters * kilograms)/(seconds)]
PLANCK_CONSTANT_h = 6.62607015 * (10 ** -34)
# Proton mass m p 1.672 621 923 69(51) × 10^−27 kg  [kilograms]
PROTON_MASS_m_p = 1.67262192369 * (10 ** -27)
# Speed of light (in vacuum) c 299 792 458 × 10^8 m/s  [meters/seconds]
SPEED_OF_LIGHT_c = 299792458
