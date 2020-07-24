# packages
import numpy as np
import math
import abc


############################################
# Abstract Class Simulation
############################################

class Simulation(abc.ABC):

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
        x0 += [x0[0]]

        return x, f_x_n, x0


############################################
# Travelling salesman algorithm
############################################

class TravelingSalesman(Simulation):

    def __init__(self, points, distance):
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
        points = self.points
        K = len(points)
        x = [np.random.randint(0, K)]
        for i in range(1, K):
            x += [self.Nearest(x[len(x)-1], points, x)]
        return x

    def draw_neighbour(self, x):
        K = len(self.points)
        i = np.random.randint(0, K-1)
        k = np.random.randint(i+1, K)
        permutation = x.copy()
        for j in range(i, k+1):
            permutation[j] = x[k+i-j]
            permutation[k+i-j] = x[j]
        return permutation

    def Nearest(self, idx, points, x):
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
        f = self.function
        return min(1, np.exp((f(x) - f(y))/T)), f(x)

    def print_result(self, n_iter, T0, dict_):
        # Creating simulation
        trajectory, function, x0 = self.simulated_annealing(n_iter, T0)

        labels, names = list(dict_.keys()),  np.array(list(dict_.values()))

        # final result
        print("\n \n#############################################################################################################")
        print("Optimal path is : ", names[trajectory])
        print("------------------------------------------------------------------------------------------------------------------")
        print("Total distance to come back to departure point is  : ",
              self.function(trajectory))
        print("------------------------------------------------------------------------------------------------------------------")
        a, b = trajectory[15], trajectory[16]
        print(f"Total distance to pass through the {len(names)} points is  : ", self.function(
            trajectory)-self.distance(a, b))
        print("##################################################################################################################")
