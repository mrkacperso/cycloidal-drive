# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
from math import sqrt, cos, sin
import numpy as np


def get_settings():
    """
    :return: rotor_radius, roller_radius, eccentricity, num_of_rollers
    """
    rotor_radius = float(30)
    roller_radius = float(4)
    eccentricity = float(1)
    num_of_rollers = 11

    return rotor_radius, roller_radius, eccentricity, num_of_rollers


def plot_cycloid(cycloid_settings, num_points):
    R = cycloid_settings[0]     # Rotor Radius
    Rr = cycloid_settings[1]    # Roller Radius
    E = cycloid_settings[2]     # Eccentricity
    N = cycloid_settings[3]     # Number of Rollers

    # ax = plt.figure(figsize=(8, 8)).add_subplot()

    t = np.linspace(0, 2 * np.pi, num_points)   # generate points

    ax = plt.figure(figsize=(8, 8)).add_subplot()

    psi = np.arctan((np.sin((1 - N) * t)) / ((R / (E * N)) - np.cos((1 - N) * t)))
    # E is added to offset the Rotor to test fit with rollers
    x = (R * np.cos(t)) - (Rr * np.cos(t + psi)) - (E * np.cos(N * t)) + E
    y = (-R * np.sin(t)) + (Rr * np.sin(t + psi)) + (E * np.sin(N * t))

    ax.plot(x, y, label="Rotor")

    # Creating Rotor Radius (the circle which the rollers sit on [position away from the origin]) and Plotting Result
    Rt = np.linspace(0, 2 * np.pi, 150)  # Number of Points.
    Rx = R * np.cos(Rt)
    Ry = R * np.sin(Rt)
    ax.plot(Rx, Ry, '--g', label="Roller Position (R)")

    # Creating Roller Equation and Plotting All Rollers on Plot
    theta = np.linspace((np.pi / 2), (5 / 2 * np.pi), (N + 1))  # Dividing 2π by number of roller
    Rrt = np.linspace(0, 2 * np.pi, 150)  # Number of Points

    for index, radian in enumerate(theta):
        Rrx = Rr * np.cos(Rrt) + (R * np.sin(radian))
        Rry = Rr * np.sin(Rrt) + (R * np.cos(radian))

        if index == 0:
            ax.plot(Rrx, Rry, 'r', label="Roller")
        else:
            ax.plot(Rrx, Rry, 'r')

    ax.set(aspect=1)  # Locks the axes so the curve is show properly
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cycloid_settings = get_settings()

    print(f'Rotor radius:\t\t{cycloid_settings[0]}mm\n'
          f'Rollers radius:\t\t{cycloid_settings[1]}mm\n'
          f'Eccentricity:\t\t{cycloid_settings[2]}mm\n'
          f'Number of rollers:\t\t{cycloid_settings[2]}')

    plot_cycloid(cycloid_settings, 1000)

