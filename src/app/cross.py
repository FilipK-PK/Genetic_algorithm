import random
import numpy as np


FIRST_EL = 0
TO_LIST = -1
JUMP_TWO = 2
NEXT = 1
BORDER = 1
END = -1
HALF = 2
N_EQUAL = 1
FIRST = 0
SECOND = 1
THIRED = 2
START = 0
MARGIN = -1
NULL = 0
ONE_POINT = 'Jedno punktowe'
TWO_POINT = 'Dwu punktowe'
THIRD_POINT = 'Trzy punktowa'
RAND_POINT = 'Jednorodne'
GET_2_POINT = 2
GET_3_POINT = 3


class Cross:
    """ Klasa przeprowadzająca krzyżowanie osobników """

    def __init__(self, name_fun, pro_cross, len_popu):
        self.__pro_cross = pro_cross
        self.__all_popu = len_popu
        self.__use_fun = None

        self.__init_fun(name_fun)

    """ Funkcja krzyzujaca populacje """
    def cross(self, popu) -> []:
        new_popu = np.array([])
        old_len_popu = len(popu)
        len_bit = len(popu[FIRST_EL])

        # // len_bit, bo np robi jeden wielki wektor, a nie macierz
        while len(new_popu) // len_bit < self.__all_popu:
            if random.random() < self.__pro_cross:
                p = self.__rand_2_point(
                    START, old_len_popu + MARGIN
                )

                new_a, new_b = self.__use_fun(
                    popu[p[FIRST]], popu[p[SECOND]]
                )
                new_popu = np.append(new_popu, new_a)
                new_popu = np.append(new_popu, new_b)

        if not len(new_popu) == self.__all_popu * len_bit:
            new_popu = self.__reduc_no_div(new_popu, len_bit)

        return np.reshape(new_popu, (TO_LIST, len_bit))

    """ Redukcja populacji parzystej do nieparzystej """
    def __reduc_no_div(self, popu, len_bit) -> []:
        p = np.random.randint(
            START, (self.__all_popu + MARGIN) * len_bit
        )
        return np.delete(popu, np.s_[p: p + len_bit], NULL)

    """ Przypisanie do zmiennej funkcji, czystrzy kod """
    def __init_fun(self, name_fun) -> None:
        list_fun = {
            ONE_POINT: self.__fun_one_point,
            TWO_POINT: self.__fun_two_point,
            THIRD_POINT: self.__fun_three_point,
            RAND_POINT: self.__fun_rand_all
        }

        self.__use_fun = list_fun[name_fun]

    """ Funkcja krzyzujaca dwa wektory w jednym punkcie """
    @staticmethod
    def __fun_one_point(vec_a, vec_b) -> ():
        size_list = len(vec_a)

        point_cross = random.randint(
            BORDER, size_list + MARGIN
        )

        new_vec_a = np.append(
            vec_a[:point_cross], vec_b[point_cross:]
        )
        new_vec_b = np.append(
            vec_b[:point_cross], vec_a[point_cross:]
        )

        return new_vec_a, new_vec_b

    """ Funkcja krzyzujaca dwia wektory w dwoch punktach """
    def __fun_two_point(self, vec_a, vec_b) -> ():
        size_list = len(vec_a)
        point = self.__rand_2_point(
            SECOND, size_list + MARGIN
        )
        point = np.sort(point)

        return self.__cut_2_point(vec_a, vec_b, point)

    """ Losowanie 2 liczb z przedziału """
    @staticmethod
    def __rand_2_point(start, stop) -> []:
        p = np.random.randint(start, stop, GET_2_POINT)
        while p[FIRST] == p[SECOND]:
            p = np.random.randint(start, stop, GET_2_POINT)

        return p

    """ Funkcja krzyzujaca dwa wektory w trzech punktach """
    def __fun_three_point(self, vec_a, vec_b) -> ():
        size_list = len(vec_a)

        point = np.random.randint(
            SECOND, size_list + MARGIN, GET_3_POINT
        )
        point = np.sort(point)

        while point[FIRST] >= point[SECOND] >= point[THIRED]:
            point = np.random.randint(
                SECOND, size_list + MARGIN, GET_3_POINT
            )
            point = np.sort(point)

        return self.__cut_3_point(vec_a, vec_b, point)

    """ Funkcja krzyzujaca kazdy chromosom """
    def __fun_rand_all(self, vec_a, vec_b) -> ():
        len_vec = len(vec_a)
        new_a = np.array([])
        new_b = np.array([])

        muta_point = np.random.rand(len_vec)

        for r, a_n, b_n in zip(muta_point, vec_a, vec_b):
            if r < self.__pro_cross:
                new_a = np.append(new_a, b_n)
                new_b = np.append(new_b, a_n)
            else:
                new_a = np.append(new_a, a_n)
                new_b = np.append(new_b, b_n)

        return new_a, new_b

    """ Mieszanie 2 kawałków wektorów """
    @staticmethod
    def __cut_2_point(vec_a, vec_b, point) -> ():
        new_vec_a = np.append(
            vec_a[:point[FIRST]],
            vec_b[point[FIRST]:point[SECOND]]
        )
        new_vec_a = np.append(new_vec_a, vec_a[point[SECOND]:])

        new_vec_b = np.append(
            vec_b[:point[FIRST]],
            vec_a[point[FIRST]:point[SECOND]]
        )
        new_vec_b = np.append(new_vec_b, vec_b[point[SECOND]:])

        return new_vec_a, new_vec_b

    """ Mieszanie 3 kawałków wektorów """
    @staticmethod
    def __cut_3_point(vec_a, vec_b, point) -> ():
        new_vec_a = np.append(
            vec_a[:point[FIRST]],
            vec_b[point[FIRST]:point[SECOND]]
        )
        new_vec_a = np.append(
            new_vec_a, vec_a[point[SECOND]:point[THIRED]]
        )
        new_vec_a = np.append(new_vec_a, vec_b[point[THIRED]:])

        new_vec_b = np.append(
            vec_b[:point[FIRST]],
            vec_a[point[FIRST]:point[SECOND]]
        )
        new_vec_b = np.append(
            new_vec_b, vec_b[point[SECOND]:point[THIRED]])
        new_vec_b = np.append(new_vec_b, vec_a[point[THIRED]:])

        return new_vec_a, new_vec_b
