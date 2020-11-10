#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(start=-1.3, stop=2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
        # r = np.sqrt(c[0]**2+c[1]**2)
        # angle = np.arctan2(c[0], c[1])
    return np.array([(np.sqrt(c[0]**2+c[1]**2), np.arctan2(c[0], c[1])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()


def ex04():
    points = np.linspace(start=-1, stop=1, num=250)
    points = list(points)
    pointsy = []
    for x in points:
        y = (x**2)*np.sin(1/(x**2))+x
        pointsy.append(y)
    plt.plot(points, pointsy)
    plt.show()



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(ex04())
    pass
