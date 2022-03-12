import numpy as np

NULL = 0
FIRST = 0
TO_LIST = -1


class Elite:
    """ Klasa zapisuje dane na czas selekcji """

    def __init__(self, len_save):
        self.__len_save = len_save
        self.__save_data = np.array([])

    """ Zapisanie najlepszych """
    def save_best(self, popu, rating) -> ():
        self.__save_data = np.array([])

        if (self.__len_save == NULL
                or self.__len_save >= len(popu)):
            return popu, rating

        for _ in range(self.__len_save):
            ind = np.argmin(rating)
            self.__save_data = np.append(
                self.__save_data, popu[ind]
            )
            popu = np.delete(popu, ind, NULL)
            rating = np.delete(rating, ind)

        return popu, rating

    """ Zwracanie najlepszych """
    def add_best(self, popu) -> []:
        if self.__len_save:
            len_ver = len(popu[FIRST])
            popu = np.append(popu, self.__save_data)

            return np.reshape(popu, (TO_LIST, len_ver))

        return popu
