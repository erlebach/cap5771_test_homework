"""
Work with DENCLUE clustering.
Do not use global variables!
"""

import pickle
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

#####     CHECK THE PARAMETERS     ########
######################################################################


def all_questions() -> dict[str, Any]:
    """Solve all questions."""
    answers = {}

    # Return the sum of 3 and 7
    answers["q1"] = 7

    # Return the first 8 Fibonacci numbers, starting with 0
    answers["q2"] = [0, 1, 1, 2, 3, 5, 8, 13]

    # Return a plot of y versus x, where
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 4, 9, 16, 25]
    answers["plot_original_cluster"] = plt.plot(x, y)

    # Create a scattergram with 300 points.
    # 1) N(1, 2)  (standard deviation= 2) with 100 points
    # 2) N(2, 3) with 200 points
    # Compute the mean and standard deviation of all the points.

    # Generating 100 points from N(1, 2), where 1 is the mean and 2 is the standard deviation
    points1 = np.random.normal(1, 2, 100)
    points2 = np.random.normal(2, 3, 200)
    # combine the two arrays into a single array of 300 points
    points = np.concatenate((points1, points2))
    # Compute the mean and standard deviation of all the points
    mean = np.mean(points)
    std = np.std(points)

    # Plotting the generated points

    answers["Two gaussians"] = [mean, std]

    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    all_answers = all_questions()
    with open("all_questions.pkl", "wb") as fd:
        pickle.dump(all_answers, fd, protocol=pickle.HIGHEST_PROTOCOL)
