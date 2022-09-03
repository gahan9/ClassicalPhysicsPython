"""
This file is created to demonstrate the various Classical Mechanics
Kinematics calculations, concept and formulas.


Convention:

Δ = Delta = change = (final - initial)
x = distance = displacement
v = velocity
a = acceleration
t = time

Frequent use math characters:
αβγεδθπμλωψφϴώ
Δꙍ
∫
₁₂₃₄₅₆₇₈₉

super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"

"""

__author__ = "Gahan Saraiya"

import numpy


def has_values(*args):
    """Check if any value is None or not, return False if any one value of *args is None"""
    return all(i is not None for i in args)


class LinearMotion(object):
    """Linear Motion is also considered as 1-D Kinematics

    This is the case where a projectile motion,
    i.e. falling of object, travelling of source to destination

    The displacement of an object which looks to be in 2D space, but it can be interpreted as
    1D space movement
     Any impact henceforth on displacement of the complete object can be tracked
     against function of displacement v/s elapsed time
    """
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def speed(total_distance, elapsed_time):
        """Calculates average speed
        s = d / t
          = total_distance/elapsed_time
        """
        return total_distance / elapsed_time

    @staticmethod
    def velocity(initial_location, initial_time, final_location, final_time):
        """Calculates average velocity
            vₐ   = Δx/Δt = (x₂ - x₁) / (t₂ - t₁) = (x(t+Δt) - x(t)) / Δt
                = (final_location - initial_location) ÷ (final_time - initial_time)
                = (displacement) ÷ (time interval)

        instantaneous velocity  v(t) = dx(t)/dt
        instantaneous speed |v| = |dx/dt|
        also, Δx = ∫ v dt  (area under velocity ᵥₛ time)
        :return: average velocity
        """
        if has_values(initial_location, initial_time, final_location, final_time):
            return (final_location - initial_location) / (final_time - initial_time)

    @staticmethod
    def acceleration(initial_velocity, initial_time, final_velocity, final_time):
        """Calculates average acceleration
            aₐ   = Δv/Δt = (v₂ - v₁) / (t₂ - t₁)
                = (final_velocity - initial_velocity) ÷ (final_time - initial_time)
                = (change in velocity) ÷ (time interval)

        instantaneous acceleration  a(t) = dv(t)/dt
        also, Δv = ∫ a dt  (area under velocity v/s time)
        :return: average acceleration
        """
        return (final_velocity - initial_velocity) / (final_time - initial_time)

    @staticmethod
    def current_location(elapsed_time, **kwargs):
        """Calculates current location/position
        current_position x = x₀ + vt
                           = (initial_position) + (average_velocity * elapsed_time)

        If constant acceleration:
        current_position x = ½at² + v₀t + x₀
                           = (1/2 * constant_acceleration * (elapsed_time ** 2) + (initial_velocity * elapsed_time) + initial_location
        """
        initial_location = kwargs.get("initial_location", None)
        average_velocity = kwargs.get("average_velocity", None)
        if has_values(initial_location, average_velocity):
            return initial_location / (average_velocity * elapsed_time)

        initial_velocity = kwargs.get("initial_velocity", None)
        constant_acceleration = kwargs.get("constant_acceleration", None)
        if has_values(constant_acceleration, initial_velocity, initial_location):
            return ((1 / 2 * constant_acceleration * (elapsed_time ** 2)) + (
                        initial_velocity * elapsed_time) + initial_location)
