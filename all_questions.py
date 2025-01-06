"""
Work with DENCLUE clustering.
Do not use global variables!
"""

import matplotlib.pyplot as plt
from numpy.typing import NDArray
import pickle
import utils # Not used

######################################################################
#####     CHECK THE PARAMETERS     ########
######################################################################


def question1() -> None:

    answers = {}

    # Return the sum of 3 and 7
    answers["q1"] = 3 + 7

    # Return the first 8 Fibonacci numbers, starting with 0
    answers["q2"] = [0, 1, 1, 2, 3, 5, 8, 13]

    # Return a plot of y versus x, where
    # x = [0, 1, 2, 3, 4, 5]
    # y = [0, 1, 4, 9, 16, 25]
    x = [i for i in range(6)]
    y = [i*i for i in range(6)]
    plot_cluster = plt.plot(x, y)
    answers["plot_original_cluster"] = plot_cluster

    # Create a scattergram with 300 points. 
    # 1) N(1, 2)  (standard deviation= 2) with 100 points
    # 2) N(2, 3) with 200 points
    # Compute the mean and standard deviation of all the points. 
    answers["Two gaussians"] = [1.5, 2.3]

    return answers

def question2() -> None:
    answers = {}

    # Return a dict with keys 'mean' and 'std' for a set of points defined by 
    answ = {}
    answ['mean'] = 1.5
    answ['std'] = 2.5
    answers["Two gaussians_a"]  = answ
    return answers

# ----------------------------------------------------------------------
if __name__ == "__main__":
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    with open("all_questions.pkl", "wb") as fd:
        pickle.dump(answers_dict, fd, protocol=pickle.HIGHEST_PROTOCOL)
