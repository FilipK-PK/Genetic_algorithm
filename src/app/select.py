import numpy as np
import random


PROC_SELECT = 3
TO_LIST = -1
FIRST = 0
SECOND = 1
NULL = 0.0
TWO_ARG = 2
BEST = 'Najlepsi'
ROULET = 'Koła ruletki'
LEADER = 'Selekcja turniejowa'
START_POINT = 1.0


class Select:
    """ Klasa odpowiedzialna za selekcje epoki """

    def __init__(self, name_fun):
        self.__use_fun = None
        self.__init_use_fun(name_fun)

    """ Głowna funkcja selekcjonujaca epoke """
    def select(self, population, rating) -> []:
        len_bit = len(population[FIRST])
        new_population = self.__use_fun(population, rating)

        return np.reshape(new_population, (TO_LIST, len_bit))

    """ Zapisanie funkcji do zmiennej, czyszczy kod """
    def __init_use_fun(self, name_fun) -> None:
        list_fun = {
            ROULET: self.__roulette_select,
            LEADER: self.__leader_select,
            BEST: self.__best_select,
        }

        self.__use_fun = list_fun[name_fun]

    """ Wybieranie elementów najlepszych """
    @staticmethod
    def __best_select(popu, rati) -> []:
        len_sel = len(rati) // PROC_SELECT
        len_bit = len(popu[FIRST])
        select_set = np.array([])

        for _ in range(len_sel):
            ind = np.argmin(rati)
            select_set = np.append(select_set, popu[ind])
            popu = np.delete(popu, ind, FIRST)
            rati = np.delete(rati, ind)

        return np.reshape(select_set, (TO_LIST, len_bit))

    """ Wybieranie elementów na podstawie koła ruletki """
    def __roulette_select(self, popu, rati) -> []:
        len_select = len(rati) // PROC_SELECT
        len_bit = len(popu[FIRST])

        rati = rati + START_POINT - np.min(rati)
        dx = np.min(rati) + np.max(rati)
        tab = dx - rati
        tab = tab/np.sum(tab)

        tab_roul = self.__create_tab_roulet(tab)

        new_tab = self.__random_rulet(
            len_select, tab_roul, popu
        )

        return np.reshape(new_tab, (TO_LIST, len_bit))

    """ Petla losujaca do ruletki """
    @staticmethod
    def __random_rulet(len_select, tab_roul, popu) -> []:
        new_tab = np.array([])

        for _ in range(len_select):
            r = random.random()
            for i, p in enumerate(tab_roul):
                if p[FIRST] <= r <= p[SECOND]:
                    new_tab = np.append(new_tab, popu[i])
                    break

        return new_tab

    """ Tworzenia tablicy - tarcza losujaca """
    @staticmethod
    def __create_tab_roulet(tab) -> []:
        tab_roul = np.array([])
        s = NULL

        for i, el in enumerate(tab):
            tab_roul = np.append(tab_roul, [s, s + el])
            s += el

        return np.reshape(tab_roul, (TO_LIST, TWO_ARG))

    """ Wybieranie elementów na podstawie drabinki """
    @staticmethod
    def __leader_select(popu, rati) -> []:
        tab_new = np.array([])
        len_popu = len(popu)
        len_bit = len(popu[FIRST])

        for i in range(FIRST, len_popu, PROC_SELECT):
            ind = np.argmin(rati[i: i+PROC_SELECT]) + i
            tab_new = np.append(tab_new, popu[ind])

        return np.reshape(tab_new, (TO_LIST, len_bit))
