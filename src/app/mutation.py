import random
import numpy as np


FIRST = 0
TO_LIST = -1
IS, IS_N = 1, 0
BOUND = 'Brzegowa'
ONE_POINT = 'Jedno punktowa'
TWO_POINT = 'Dwu punktowa'
RAND_POPINT = 'Jednorodne'
END, START = -1, 0
MARGIN = -1


class Mutation:
    """ Klasa przeprowadza proczes mutacji pokolenia """

    def __init__(self, name_fun, pro_mutate):
        self.__pro_mutate = pro_mutate
        self.__use_fun = None

        self.__init_use_fun(name_fun)

    """ Przeprowadzanie mutacji na populacji """
    def mutate(self, population) -> []:
        new_popul = np.array([])
        len_bit = len(population[FIRST])

        for vec in population:
            if random.random() < self.__pro_mutate:
                new_vec = self.__use_fun(vec)
                new_popul = np.append(new_popul, new_vec)
            else:
                new_popul = np.append(new_popul, vec)

        return np.reshape(new_popul, (TO_LIST, len_bit))

    """ Zapisane zmiennej do funkcji czyszczy kod """
    def __init_use_fun(self, name_fun) -> None:
        list_fun = {
            BOUND: self.__end_mutate,
            ONE_POINT: self.__one_mutate,
            TWO_POINT: self.__two_mutate,
            RAND_POPINT: self.__rand_mutate
        }

        self.__use_fun = list_fun[name_fun]

    """ Funkcja mutuje brzeg """
    @staticmethod
    def __end_mutate(vec) -> []:
        p = random.randint(END, START)
        vec[p] = (IS if vec[p] == IS_N else IS_N)

        return vec

    """ Funkcja mutuje losowo jeden gen """
    @staticmethod
    def __one_mutate(vec) -> []:
        r = random.randint(START, len(vec)+MARGIN)
        vec[r] = (IS if vec[r] == IS_N else IS_N)

        return vec

    """ Funkcja mutuje losowo dwa geny """
    @staticmethod
    def __two_mutate(vec) -> []:
        p1 = random.randint(START, len(vec) + MARGIN)
        p2 = random.randint(START, len(vec) + MARGIN)

        while p1 == p2:
            p2 = random.randint(START, len(vec) + MARGIN)

        vec[p1] = (IS if vec[p1] == IS_N else IS_N)
        vec[p2] = (IS if vec[p2] == IS_N else IS_N)

        return vec

    """ Funkcja mutuje losowo gen """
    def __rand_mutate(self, vec) -> []:
        vec_len = len(vec)

        for i in range(vec_len):
            if random.random() <= self.__pro_mutate:
                vec[i] = (IS if vec[i] == IS_N else IS_N)

        return vec
