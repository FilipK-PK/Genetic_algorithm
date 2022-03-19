import math

import numpy as np

JUMP_TWO = 2
FIRST, SECOND = 0, 1
MARGIN = 1
NULL = 0
NEXT = 1
BASE = 2
FUN_BUKIN = 'BUKIN'
FUN_DROP_WAVE = 'DROP-WAVE'
FUN_GOLDSTREAM = 'GOLDSTEIN-PRICE'
FUN_MCCORMICK = 'MCCORMICK'
FUN_ACKLEY = 'ACKLEY'
FUN_BEALE = 'BEALE'
FUN_SCHAFFER_2 = 'SCHAFFER 2'
FUN_HOLDER_TABLE = 'HOLDER TAB'


class Fun:
    """ Klasa na podstawie macierzy populacji
    oblicza wartosci funkcji """

    def __init__(self, name_fun, len_bit, end_points):
        self.__len_bit = len_bit
        self.__min_val = []
        self.__df = []  # najmniejszy przedział dokładnosci
        self.__fun = None
        self.__len_set = BASE**len_bit + MARGIN

        self.__set_use_fun(name_fun)
        self.__init_variable(end_points)

    """ Glowna funkcja, zrwaca liste z ocena populacji """
    def get_eval(self, population) -> []:
        eval_list = []

        for el in population:
            eval_list.append(
                self.__fun(self.__bin_to_double(el))
            )

        return np.array(eval_list)

    """ Funkcja zwraca wartosci dla danego vektora bit """
    def get_point(self, vec) -> []:
        return self.__bin_to_double(vec)

    """ Zapisanie funkcji do zmiennej, czystrzy kod """
    def __set_use_fun(self, name_fun) -> None:
        set_fun = {
            FUN_ACKLEY: self.__fun_ackley,
            FUN_BEALE: self.__fun_beale,
            FUN_BUKIN: self.__fun_bukin,
            FUN_DROP_WAVE: self.__fun_drop_wawe,
            FUN_GOLDSTREAM: self.__fun_goldstein_price,
            FUN_MCCORMICK: self.__fun_miccormick,
            FUN_SCHAFFER_2: self.__fun_schaffer2,
            FUN_HOLDER_TABLE: self.__fun_holder_table
        }

        self.__fun = set_fun[name_fun]

    """ Przekształcanie argomentów poczatkowych """
    def __init_variable(self, end_points) -> None:
        len_set = len(end_points)

        for i in range(FIRST, len_set, JUMP_TWO):
            self.__min_val.append(end_points[i])
            self.__df.append(
                (end_points[i+NEXT] - end_points[i])
                / self.__len_set
            )

    """ Zamiana pojedynczego wiersza na liste punktów """
    def __bin_to_double(self, vec) -> []:
        len_set = len(vec)
        points = []

        for i in range(FIRST, len_set, self.__len_bit):
            sum_dec = NULL
            for j in vec[i: i+self.__len_bit]:
                sum_dec = BASE*sum_dec + j

            points.append(sum_dec)

        return self.__rescale_val(points)

    """ Przeskalowanie wartosci liczby do przedziału podanego """
    def __rescale_val(self, val) -> []:
        res_list = np.array([])

        for i, el in enumerate(val):
            res_list = np.append(
                res_list, self.__min_val[i] + self.__df[i] * el
            )

        return res_list

    """ ACKLEY FUNCTION """
    @staticmethod
    def __fun_ackley(p) -> float:
        return (
                -20 * math.exp(-0.2 * math.sqrt(0.5 * (p[0] ** 2 + p[1] ** 2)))
                - math.exp(0.5 * (math.cos(2 * math.pi * p[0]) + math.cos(math.pi * p[1])))
                + 20 + math.exp(1)
        )

    """ BEALE FUNCTION """
    @staticmethod
    def __fun_beale(p) -> float:
        return (
                (1.5 - p[0] + p[0] * p[1]) ** 2 +
                (2.25 - p[0] + p[0] * p[1] ** 2) ** 2 +
                (2.625 - p[0] + p[0] * p[1] ** 3) ** 2
        )

    """ BUKIN """
    @staticmethod
    def __fun_bukin(p) -> float:
        return (
                100.0 * math.sqrt(math.fabs(p[1] - 0.01 * p[0] ** 2))
                + 0.01 * math.fabs(p[0] + 10.0)
        )

    """ DROP-WAVE """
    @staticmethod
    def __fun_drop_wawe(p) -> float:
        return (
            -(1.0 + math.cos(12.0 * math.sqrt(p[0] ** 2 + p[1] ** 2)))
            / (0.5 * (p[0] ** 2 + p[1] ** 2) + 2.0)
        )

    """ GOLDSTEIN-PRICE """
    @staticmethod
    def __fun_goldstein_price(p) -> float:
        return (
            (1.0+(p[0]+p[1]+1.0)**2 * (19.0-14*p[0]+3*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2)) *
            (30.0+(2*p[0]-3*p[1])**2 * (18.0-32*p[0]+12*p[0]**2+48*p[1]-36*p[0]*p[1]+27*p[1]**2))
        )

    """ MCCORMICK """
    @staticmethod
    def __fun_miccormick(p) -> float:
        return (
            math.sin(p[0] + p[1]) + (p[0] - p[1])**2 - 1.5 * p[0] + 2.5 * p[1] + 1
        )

    """ SCHAFFER 2 """
    @staticmethod
    def __fun_schaffer2(p) -> float:
        return (
            0.5 + (math.sin(p[0]**2-p[1]**2)**2-0.5) / (1.0 + 0.001*(p[0]**2+p[1]**2))**2
        )

    """ HOLDER TABLE """
    @staticmethod
    def __fun_holder_table(p) -> float:
        return (
            - math.fabs(math.sin(p[0]) * math.cos(p[1]) *
                        math.exp(math.fabs(1-(math.sqrt(p[0]**2+p[1]**2)) / math.pi))
                        )
        )
