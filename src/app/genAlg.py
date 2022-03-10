from src.app.fun import Fun
from src.different.statistics import Statistic
from src.app.cross import Cross
from src.app.mutation import Mutation
from src.app.select import Select
from src.app.invert import Invert
from src.different.timeRun import Time
from src.app.elite import Elite
import numpy as np
import tkinter.messagebox as tm


PROC_CROSS = 0.7
PROC_MUTATE = 0.9
ROUND_TO = 2
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
X_TEXT = ' Dla x='
GLOBAL = ' globalny '
FIRST = 0
SECOND = 1
TO_ROAD = 2


class GenAlg:
    """ Glowna klasa, zazadza obliczeniami """

    def __init__(
            self, epoch, len_popu, len_var, len_bit, end_points,
            name_fun, name_select, name_cross, name_mutate,
            elit=ELITE_LEN, p_cross=PROC_CROSS, p_mutate=PROC_MUTATE,
            p_invert=PROC_MUTATE
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
        self.__time = None
        self.__elit = None
        self.__invert = None

    """ Glowna funkcja, ona steruje wsztstkim """
    def run(self) -> None:
        self.__init_extr_class()  # inicjacja zewnetrznych klass
        popu = self.__create_population()  # tworzenie populacji

        self.__time.start()

        for i in range(self.__epoch):
            rating = self.__exam_popu.get_eval(popu)  # Ocena populacji
            popu, rating = self.__elit.save_best(popu, rating)
            self.__statistic.check_statistics(rating, popu)  # zapisanie statystyk
            popu = self.__select.select(popu, rating)  # selekcja epoki
            popu = self.__elit.add_best(popu)  # dodanie najlepszych
            popu = self.__crosses.cross(popu)  # krzyzowanie populacji
            popu = self.__mutation.mutate(popu)  # mutacja populacji
            popu = self.__invert.invert(popu)  # inwersja populacji
            print(EPOK, i + ROAD_IND)

        self.__time.stop()
        self.__show_result(popu)

    """ Funkcja generuje polulację """
    def __create_population(self) -> []:
        return np.random.randint(
            BASE, size=(
                self.__len_popu,
                self.__len_var * self.__len_bit
            )
        )

    """ Inicjacja zawnetrznych klass """
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
        self.__time = Time()

    """ Pokazuje zgromadzone dane """
    def __show_result(self, popu) -> None:
        time = self.__time.get_result()
        best, point = self.__get_best_val(popu)
        best_global = self.__statistic.get_min_g()
        best_glo_xy = self.__exam_popu.get_point(
            self.__statistic.get_best_xy()
        ).round(ROUND_TO)

        tm.showinfo(
            TITLE_INFO,
            BEST_RESULT + END + str(best) + X_TEXT +
            str(point[FIRST]) + Y_TEXT + str(point[SECOND]) +
            NEW_LINE + BEST_RESULT + GLOBAL + str(best_global) +
            X_TEXT + str(best_glo_xy[FIRST]) + Y_TEXT +
            str(best_glo_xy[SECOND]) + NEW_LINE + NEW_LINE +
            TIME + time + SECONDS
        )

        # self.__statistic.save_data() todo odkomentowac na kuncu, wypisywanie danych do txt
        self.__statistic.draw_graphs()

    """ Zwracanie najlepszej wartosci min """
    def __get_best_val(self, popu) -> ():
        rating = self.__exam_popu.get_eval(popu)
        ind = np.argmin(rating)

        best = np.round(rating[ind], ROUND_TO)
        points = np.round(
            self.__exam_popu.get_point(popu[ind]), ROUND_TO
        )

        return best, points
