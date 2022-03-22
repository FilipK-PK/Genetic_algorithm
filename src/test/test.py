from src.app.fun import Fun
from src.different.statistics import Statistic
from src.app.cross import Cross
from src.app.mutation import Mutation
from src.app.select import Select
from src.app.elite import Elite
from src.app.invert import Invert
import numpy as np


PROC_CROSS = 0.7
PROC_MUTATE = 0.9
ROUND_TO = 7
LEN_SAVE = 5
BASE = 2
ROAD_IND = 1
TITLE_INFO = 'Uzyskane rezultaty'
TIME = 'Czas '
BEST_RESULT = 'Najlepszy wynik'
END = ' koncowy '
NEW_LINE = '\n'
SECONDS = ' s'
ELITE_LEN = 10
EPOK = 'Epoka:'
Y_TEXT = ' y='
X_TEXT = '  dla x='
GLOBAL = ' globalny '
FIRST = 0
SECOND = 1
TO_ROAD = 2
SEP = '\t'


class Test:
    """ Kopia klasy AlgGen okrojona do potrzebnych elementów,
    słurzy do testowania pojedynczych elementów algorytmu genetycznego """


    """ Parametry donyslne dla kazdego parametru, dla poprawy czystosci kodu """
    def __init__(
            self, epoch=20, len_popu=50, len_var=2, len_bit=24,
            end_points=[-10, 10, -10, 10], name_fun='ACKLEY',
            name_select='Najlepsi', name_cross='Jednorodne',
            name_mutate='Jednorodne', elit=3, p_cross=0.8,
            p_mutate=0.1, p_invert=0.1
    ):
        self.__epoch = epoch
        self.__len_popu = len_popu
        self.__len_bit = len_bit
        self.__len_var = len_var
        self.__end_points = end_points
        self.__name_fun = name_fun
        self.__name_select = name_select
        self.__name_cross = name_cross
        self.__p_cross = p_cross
        self.__name_mutate = name_mutate
        self.__p_mutate = p_mutate
        self.__p_invert = p_invert
        self.__elit_len = elit

        self.__exam_popu = None
        self.__statistic = None
        self.__crosses = None
        self.__mutation = None
        self.__select = None
        self.__elit = None
        self.__invert = None

    """ Glowna funkcja, ona steruje wsztstkim """
    def run(self) -> float:
        self.__init_extr_class()  # inicjacja zewnetrznych klass
        popu = self.__create_population()  # tworzenie populacji

        for i in range(self.__epoch):
            rating = self.__exam_popu.get_eval(popu)  # Ocena populacji
            popu, rating = self.__elit.save_best(popu, rating)
            self.__statistic.check_statistics(rating, popu)  # zapisanie statystyk
            popu = self.__select.select(popu, rating)  # selekcja epoki
            popu = self.__elit.add_best(popu)  # dodanie najlepszych
            popu = self.__crosses.cross(popu)  # krzyzowanie populacji
            popu = self.__mutation.mutate(popu)  # mutacja populacji
            popu = self.__invert.invert(popu)  # inwersja populacji

        return self.__show_result()

    """ Funkcja generuje polulację """
    def __create_population(self) -> []:
        return np.random.randint(
            BASE, size=(
                self.__len_popu,
                self.__len_var * self.__len_bit
            )
        )

    """ Inicjacja zawnetrznych klas """
    def __init_extr_class(self) -> None:
        self.__exam_popu = Fun(
            self.__name_fun, self.__len_bit, self.__end_points
        )
        self.__crosses = Cross(
            self.__name_cross, self.__p_cross, self.__len_popu
        )
        self.__mutation = Mutation(
            self.__name_mutate, self.__p_mutate
        )
        self.__select = Select(self.__name_select)
        self.__invert = Invert(self.__p_invert)
        self.__elit = Elite(self.__elit_len)
        self.__statistic = Statistic()

    """ Pokazuje min globalne """
    def __show_result(self) -> None:
        best_min, best_yx = self.__statistic.get_global_best()
        return best_min


def calc_statistic():
    """ Sprawdzanie 40 razy kazdej wartosci danego parametru """

    """ Przykładaowe wywołanie """
    data = []
    var = [4, 8, 12, 16, 20, 24, 28, 32]

    """ Petla oblicza poszczegulne wartosci """
    for el in var:
        row = []
        print('[S]:', el)
        for _ in range(40):
            app = Test(len_bit=el)
            row.append(app.run())
        data.append(row)

    data = np.array(data)

    """ Obliczanie min sredniej odchylenia """
    min_val = np.min(data, axis=1)
    mean_val = np.mean(data, axis=1)
    std_val = np.std(data, axis=1)

    """ Wyswietlanie wyników """
    for i, j, k, l in zip(var, min_val, mean_val, std_val):
        print(i, SEP, j, SEP, k, SEP, l)


if __name__ == '__main__':
    calc_statistic()
