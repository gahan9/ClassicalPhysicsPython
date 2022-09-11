"""
This file is created to demonstrate the various Classical Mechanics
Kinematics calculations, concept and formulas.

All the basic units for input should follow below standard:

Measure   → Unit
----------------
length    → `m` meter
time      → `s` seconds
mass      → `gm` grams



Convention:

Δ = Delta = change = (final - initial)
x = distance = displacement
v = velocity
a = acceleration
t = time
θ = Angle of projection

Frequent use math characters:
αβγεδθπμλωψφϴώ
Δꙍ
∫
₁₂₃₄₅₆₇₈₉

super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"

"""

__author__ = "Gahan Saraiya"

import numpy as np


RADIAN_TO_NUMBER = np.pi/180  # multiply any degree with this value to represent it as anumber to make calculaiton easier.


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
    def velocity(initial_location=None, initial_time=None, final_location=None, final_time=None, angle=None):
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
        if has_values(angle):
            return np.tan(angle * RADIAN_TO_NUMBER)

    @staticmethod
    def acceleration(initial_velocity=None, initial_time=None, final_velocity=None, final_time=None, angle=None):
        """Calculates average acceleration
            aₐ   = Δv/Δt = (v₂ - v₁) / (t₂ - t₁)
                = (final_velocity - initial_velocity) ÷ (final_time - initial_time)
                = (change in velocity) ÷ (time interval)

        instantaneous acceleration  a(t) = dv(t)/dt
        also, Δv = ∫ a dt  (area under velocity v/s time)
        :return: average acceleration
        """
        if has_values(initial_velocity, initial_time, final_velocity, final_time):
            return (final_velocity - initial_velocity) / (final_time - initial_time)

    @staticmethod
    def current_location(elapsed_time, **kwargs):
        """Calculates current location/position
        current_position x = x₀ + vt
                           = (initial_position) + (average_velocity * elapsed_time)

        If constant acceleration:
        current_position x = ½at² + v₀t + x₀
                           = [(1/2 * constant_acceleration * (elapsed_time ** 2)) + (
                           initial_velocity * elapsed_time) + initial_location]
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


class ProjectileMotion(LinearMotion):
    @staticmethod
    def velocity_x(initial_velocity=None, angle=None):
        """
        Returns velocity on x-axis for projectile motion

        velocity on x-axis
            v₀ₓ = v₀cosθ
                = initial_velocity * np.cos(angle * RADIAN_TO_NUMBER)
        :return:
        """
        if has_values(initial_velocity, angle):
            return initial_velocity * np.cos(angle * RADIAN_TO_NUMBER)

    @staticmethod
    def velocity_y(initial_velocity=None, angle=None, acceleration=None, elapsed_time=0):
        """
        Returns velocity on y-axis for projectile motion

        velocity on y-axis
            v₀ᵧ = at + v₀sinθ
                = (acceleration * elapsed_time) + initial_velocity * np.sin(angle * RADIAN_TO_NUMBER)
        :return:
        """
        if has_values(initial_velocity, angle):
            result = initial_velocity * np.sin(angle * RADIAN_TO_NUMBER)
            if elapsed_time and acceleration:
                result += acceleration * elapsed_time
            return result

    def current_location_x(self, elapsed_time, **kwargs):
        """
        Calculates current position/location at current elapsed time
        in projectile motion on x-axis

        xₜ = v₀ₓ * t + xᵢ
          = [velocity_x * elapsed_time] + initial_location
          = [(v₀cosθ) * t] + xᵢ
        :return:
        """
        initial_velocity = kwargs.get("initial_velocity", None)  # v₀ₓ
        angle = kwargs.get("angle", None)  # θ
        velocity_x = kwargs.get("velocity_x", None)  # v₀ₓ
        initial_location = kwargs.get("initial_location", 0)  # xᵢ
        if has_values(velocity_x):
            return (velocity_x * elapsed_time) + initial_location
        if has_values(initial_velocity, angle):
            return (self.velocity_x(initial_velocity, angle) * elapsed_time) + initial_location

    def current_location_y(self, elapsed_time, **kwargs):
        """
        Calculates current position/location at current elapsed time
        in projectile motion on y-axis

            yₜ = ½at² + v₀ᵧ * t + yᵢ
              = (1/2 * acceleration * elapsed_time * elapsed_time) + (velocity_y * elapsed_time) + initial_location
              = ½at² + (v₀sinθ * t) + yᵢ
        :return:
        """
        angle = kwargs.get("angle", None)  # θ
        acceleration = kwargs.get("acceleration", None)  # a
        velocity_y = kwargs.get("velocity_y", None)  # v₀ᵧ
        initial_location = kwargs.get("initial_location", 0)  # yᵢ
        initial_velocity = kwargs.get("initial_velocity", None)  # v₀ₓ
        if has_values(acceleration, velocity_y, initial_location):
            return (1/2 * acceleration * elapsed_time * elapsed_time) + (velocity_y * elapsed_time) + initial_location
        if has_values(acceleration, initial_velocity, angle):
            return (1 / 2 * acceleration * elapsed_time * elapsed_time) + (
                        self.velocity_y(initial_velocity, angle) * elapsed_time) + initial_location


class CircularMotion(object):
    def __init__(self, *args, **kwargs):
        """
        Notations:
        Τ    → period (seconds to complete full circumference)
        F    → frequency = (1/Τ)  [1/second  or Hz]
        2π◦  → circumference in ◦radian
        ω    → angular velocity = (2π/T)
        v    → velocity = ((2π * r) / T) = ω * r
        |a꜀|   → centripetal acceleration  = (v²/r) = (ω²r)

        :param args:
        :param kwargs:
        """
        self.circumference = 2 * np.pi

    @staticmethod
    def frequency(period):
        """
        :param period:  Τ    → period (seconds to complete full circumference)
        :return: F    → frequency = (1/Τ)  [1/second  or Hz]
        """
        return 1/period

    @staticmethod
    def frequency_to_period(frequency):
        """
        :param frequency:
        :return: Τ    → period (seconds to complete full circumference)
        """
        return 1/frequency

    def angular_velocity(self, period=None, frequency=None):
        """Angular velocity ω

        :param period: Τ    → period (seconds to complete full circumference)
        :param frequency: F    → frequency = (1/Τ)  [1/second  or Hz]
        :return: ω    → angular velocity = (2π/T)
                                        = circumference / period
        """
        if period:
            return self.circumference / period
        if frequency:
            return self.circumference / self.frequency_to_period(frequency)

    def velocity(self, radius, angular_velocity=None, period=None):
        """
        Velocity v = ((2π * r) / T) = ω * r
                    = (circumference * radius) / period
                    = angular_velocity * radius
        :param radius: r
        :param angular_velocity: ω
        :param period: Τ
        :return:
        """
        if angular_velocity:
            return angular_velocity * radius
        if period and not angular_velocity:
            return self.angular_velocity(period=period) * radius

    def centripetal_acceleration(self, radius, velocity=None, angular_velocity=None, period=None):
        """
        Centripetal acceleration
        |a꜀| = (v²/r) = (ω²r)
            = ((velocity * velocity) / radius)
            = angular_velocity * angular_velocity * radius
        :param radius: r
        :param velocity: v
        :param angular_velocity: ω
        :param period: T
        :return: |a꜀|
        """
        if velocity:
            return (velocity ** 2) / radius
        if angular_velocity:
            return (angular_velocity ** 2) * radius
        if period:
            return (self.angular_velocity(period=period) ** 2) * radius
