##################################################################################
#                            Author: Anas ESSOUNAINI                             #
#                       File Name: travelling_salesman.py                        #
#                     Creation Date: July 18, 2020 09:41 PM                      #
#                    Last Updated: November 17, 2020 03:06 AM                    #
#                            Source Language: python                             #
#  Repository: https://github.com/AnasEss/travelling-salesman-shortest-path.git  #
#                                                                                #
#                            --- Code Description ---                            #
#                         simulated annealing algorithm                          #
##################################################################################

# packages
import numpy as np
import math
import abc


############################################
# Abstract Class Simulation
############################################

class Simulation(abc.ABC):
    """General class of simulated annealing algorithm
    """

    def __init__(self, seed=0):
        self.seed = seed

    @abc.abstractmethod
    def initial_config(self):
        raise NotImplementedError

    @abc.abstractmethod
    def draw_neighbour(self, x):
        raise NotImplementedError

    @abc.abstractmethod
    def acceptance_probability(self, x, y, T):
        raise NotImplementedError

    def simulated_annealing(self, N, T0):
        """Simulated annealing algorithm - described in markdown

        Args:
            N (int): number of iterations
            T0 (int): algorithm parameter T0

        Returns:
            x (list): trajectory
            f_x_n (float): value of acceptance probability  for last point
        """
        x0 = self.initial_config()
        x, n, T = x0, 1, T0
        f_x_n = []
        print(r'Begin travelling salesman algorithm : ------------------------------------------', end='', sep='')
        while n < N:
            y = self.draw_neighbour(x)
            u = np.random.uniform(0, 1)
            acceptance, f_x = self.acceptance_probability(x, y, T)
            if u < acceptance:
                x = y
            n = n+1
            T = T0/np.log(n)
            f_x_n += [f_x]
        print(f"[COMPLETED]")
        x += [x[0]]

        return x, f_x_n


############################################
# Travelling salesman algorithm
############################################

class TravelingSalesman(Simulation):

    def __init__(self, points, distance):
        """initialize travelling salesman algorithm

        Args:
            points (list): points representation
            distance (function): distance definition

        Returns:
            None
        """
        print(r'Initial configuration for travelling salesman : --------------------------------------------', end='', sep='')
        self.points = points

        def cost(sigma, C):
            d = 0
            K = len(sigma)
            for i in range(K-1):
                d += distance(C[sigma[i]], C[sigma[i+1]])
            return d
        self.distance = distance
        self.function = lambda p: cost(p, self.points)
        print(f"[COMPLETED]")

    def initial_config(self):
        """Initial configuration of the path

        Returns:
            list: configuration of the path => permutation of the points
        """
        points = self.points
        K = len(points)
        x = [np.random.randint(0, K)]
        for i in range(1, K):
            x += [self.Nearest(x[len(x)-1], points, x)]
        return x

    def draw_neighbour(self, x):
        """draws neighbour as described in the markdown

        Args:
            x (Object): point representation

        Returns:
            list: permutation
        """
        K = len(self.points)
        i = np.random.randint(0, K-1)
        k = np.random.randint(i+1, K)
        permutation = x.copy()
        for j in range(i, k+1):
            permutation[j] = x[k+i-j]
            permutation[k+i-j] = x[j]
        return permutation

    def Nearest(self, idx, points, x):
        """draws nearest element

        Args:
            idx (int): index of element
            points ([Object]): points
            x ([Object]): points to not take into consideration

        Returns:
            Object: nearest point
        """
        d_min = math.inf
        nearest = idx
        for i in range(len(points)):
            if i not in x:
                d = self.distance(points[idx], points[i])
                if d < d_min:
                    d_min = d
                    nearest = i
        return nearest

    def acceptance_probability(self, x, y, T):
        """computes acceptance probability

        Args:
            x (Object): point 1
            y (Object): point 2
            T (float): algorithm parameter

        Returns:
            float: acceptance probability
        """
        f = self.function
        return min(1, np.exp((f(x) - f(y))/T)), f(x)

    def print_result(self, n_iter, T0, dict_):
        """print results of the simulation

        Args:
            n_iter (int): number of iterations
            T0 (float): algorithm parameter
            dict_ (dict): dictionnary whose keys are the objects representation used in computing the distance and whose values are the names of objects
        """
        # Creating simulation
        trajectory, function = self.simulated_annealing(n_iter, T0)

        labels, names = list(dict_.keys()),  np.array(list(dict_.values()))

        n = len(dict_)

        # final result
        print("\n \n#############################################################################################################")
        print("Optimal path is : ", names[trajectory])
        print("------------------------------------------------------------------------------------------------------------------")
        print("Total distance to come back to departure point is  : ",
              self.function(trajectory))
        print("------------------------------------------------------------------------------------------------------------------")
        a, b = trajectory[n-1], trajectory[n]
        print(f"Total distance to pass through the {len(names)} points is  : ", self.function(
            trajectory)-self.distance(a, b))
        print("##################################################################################################################")
