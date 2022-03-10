import numpy as np
import matplotlib.pyplot as plt
import os


TXT_TYPE = '.txt'
OPEN_FILE = 'w'
PADDING = 0.5
TITLE_BEST_MENS = 'Wykres najlepszej i sredniej wartosci dla epoki'
TITLE_STD = 'Wykres odchylenia standardowego dla epoki'
FIRST = 0
SECOND = 1
ADD = 1
ROUND_TO = 3
NULL = ''
ZERO = 0
END = -1
LEGEND_BEST = 'Najlepszy'
LEGEND_STR = 'Średnia'
COORD_LEGEND = 'upper right'
STD = 'Std'
MEAN = 'Mean'
BEST = 'Best'


class Statistic:
    """ Klasa gromadzi dane co epoke i tworzy wykres """

    def __init__(self):
        self.__best = []
        self.__mean = []
        self.__std = []
        self.__best_xy = []

    """ Zbieranie statystyk """
    def check_statistics(self, vec, popu) -> None:
        self.__best.append(np.min(vec))
        self.__mean.append(np.mean(vec))
        self.__std.append(np.std(vec))
        self.__best_xy.append(popu[np.argmin(vec)])

    """ Rysywanie wykresu """
    def draw_graphs(self) -> None:
        epoch = np.arange(len(self.__best))

        plt.subplot(2, 1, 1)
        plt.title(TITLE_BEST_MENS)
        plt.plot(epoch, self.__best, label=LEGEND_BEST)
        plt.plot(epoch, self.__mean, label=LEGEND_STR)
        plt.legend(loc=COORD_LEGEND)

        plt.subplot(2, 1, 2)
        plt.title(TITLE_STD)
        plt.plot(epoch, self.__std)

        plt.subplots_adjust(hspace=PADDING)
        plt.show()

    """ Zapisywanie statystyka do pliku txt """
    def save_data(self) -> None:
        self.__save_el(self.__best, BEST)
        self.__save_el(self.__mean, MEAN)
        self.__save_el(self.__std, STD)

    """ Zwraca min globalne """
    def get_global_best(self) -> ():
        return (
            round(np.min(self.__best), ROUND_TO),
            self.__best_xy[np.argmin(self.__best)]
        )

    """ Zwraca min ostatniej epoki """
    def get_end_best(self) -> []:
        return (
            round(self.__best[END], ROUND_TO),
            self.__best_xy[END]
        )

    """ Zapis do pliku """
    @staticmethod
    def __save_el(tab, name) -> None:

        add, ind = NULL, ZERO,
        while os.path.exists(name + add + TXT_TYPE):
            ind += ADD
            add = str(ind)

        file = open(name + add + TXT_TYPE, OPEN_FILE)
        np.savetxt(file, tab)

        file.close()
