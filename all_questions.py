"""
Work with DENCLUE clustering.
Do not use global variables!
"""

import matplotlib.pyplot as plt
from numpy.typing import NDArray
import utils
import pickle

######################################################################
#####     CHECK THE PARAMETERS     ########
######################################################################


def all_questions() -> None:

    answers = {}

    # Return the sum of 3 and 7
    answers["q1"] = None

    # Return the first 8 Fibonacci numbers, starting with 0
    answers["q2"] = None

    # Return a plot of y versus x, where
    # x = [0, 1, 2, 3, 4, 5]
    # y = [0, 1, 4, 9, 16, 25]
    answers["plot_original_cluster"] = None

    # Create a scattergram with 300 points. 
    # 1) N(1, 2)  (standard deviation= 2) with 100 points
    # 2) N(2, 3) with 200 points
    # Compute the mean and standard deviation of all the points. 
    answers["Two gaussians"] = None

    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    all_answers = all_questions()
    with open("all_questions.pkl", "wb") as fd:
        pickle.dump(all_answers, fd, protocol=pickle.HIGHEST_PROTOCOL)
