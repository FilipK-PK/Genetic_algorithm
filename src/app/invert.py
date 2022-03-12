import numpy as np


FIRST = 0
SECOND = 1
TWO_POINT = 2
IS = 1
IS_N = 0
START = 0
MARGIN = -1


class Invert:
    """ Klasa wykonywuje inwersje """

    def __init__(self, prop):
        self.__prop_inv = prop

    """ Losowanie inwersji """
    def invert(self, popu) -> []:
        len_popu = len(popu)
        len_bit = len(popu[FIRST])
        vec_rand = np.random.rand(len_popu)

        for i in range(len_popu):
            if vec_rand[i] <= self.__prop_inv:

                p = np.random.randint(
                    START, len_bit + MARGIN, TWO_POINT
                )
                p = np.sort(p)

                while p[FIRST] >= p[SECOND]:
                    p = np.random.randint(
                        START, len_bit + MARGIN, TWO_POINT
                    )
                    p = np.sort(p)

                for j in range(p[FIRST], p[SECOND]):
                    popu[i][j] = (IS if popu[i][j] == IS_N else IS_N)

        return popu
