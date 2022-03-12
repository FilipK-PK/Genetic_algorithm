import datetime


TIME_ERR = 'inf'
DOT = '.'
SEP = ':'
FIRST = 0
SECOND = 1
THIRD = 2
MIN = 60
HOUR = 3600
PROC_MICRO = 10000


class Time:
    """ Klasa odmierzajaca czas """

    def __init__(self):
        self.__start = None
        self.__stop = None

    """ Funkcja zaczyna odmiezac czas """
    def start(self) -> None:
        self.__start = datetime.datetime.now()

    """ Funkcja zatrzymuje mierzenie czasu """
    def stop(self) -> None:
        self.__stop = datetime.datetime.now()

    """ Funkcja zwraca czas """
    def get_result(self) -> str:
        if self.__start and self.__stop:
            time = str(self.__stop - self.__start)
            time = time.split(DOT)

            sec = int(
                time[FIRST].split(SEP)[FIRST]
            ) * HOUR

            sec += int(
                time[FIRST].split(SEP)[SECOND]
            ) * MIN

            sec += int(time[FIRST].split(SEP)[THIRD])

            micro = round(float(time[SECOND]) / PROC_MICRO)

            return str(sec) + DOT + str(micro)

        return TIME_ERR
