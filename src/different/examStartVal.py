PRE_TEXT = 'Błąd w polu do wpisywania '
ERR_EPOCH = 'liczby epok'
ERR_POPU = 'rozmiary populacji'
ERR_BIT = 'liczby bitów'
ERR_END_POINT = 'przedziałów'
ERR_ELIT = 'liczby zapisanych elit'
ERR_CROSS = 'procentu krzyzowania'
ERR_MUTABLE = 'procentu mutacji'
ERR_INVERT = 'procentu inwersji'
ERR_SEL_LIDER = 'rozmiaru grupy turniejowej'
ERR_SEL_BEST = 'procentu najlepszych wartosci'
ERR_SEL_RULLET = 'procentu losowan w kole ruletki'
DOT = '.'
NULL = ''
ZERO = 0.0
ONE = 1.0
NEXT = 1
JUMP_TO = 2
START = 0
ZERO_STR = '0'
OPT_LIDER = 'Selekcja turniejowa'
OPT_BEST = 'Najlepsi'
OPT_RULLET = 'Koła ruletki'


class ExamStartVal:
    """ Klasa sprawdza wpisane wartosci w gui """

    """ Funkcja sprawdzajaca poprawnosc danych """
    def exam(self, epoch, len_popu, len_bit, end_points,
             use_elit, p_cross, p_mutate, p_invert, p_select,
             select_opt) -> str:

        if self.__is_int(epoch):
            return PRE_TEXT + ERR_EPOCH

        if self.__is_int(len_popu):
            return PRE_TEXT + ERR_POPU

        if self.__is_int(len_bit):
            return PRE_TEXT + ERR_BIT

        if self.__is_int(use_elit) and use_elit != ZERO_STR:
            return PRE_TEXT + ERR_ELIT

        if self.__is_ufloat(p_cross):
            return PRE_TEXT + ERR_CROSS

        if self.__is_ufloat(p_mutate):
            return PRE_TEXT + ERR_MUTABLE

        if self.__is_ufloat(p_invert):
            return PRE_TEXT + ERR_INVERT

        if self.__good_set(end_points):
            return PRE_TEXT + ERR_END_POINT

        if select_opt == OPT_RULLET:
            if self.__is_ufloat(p_select) or float(p_select) == ZERO:
                return PRE_TEXT + ERR_SEL_RULLET

        if select_opt == OPT_BEST:
            if self.__is_ufloat(p_select) or float(p_select) == ZERO:
                return PRE_TEXT + ERR_SEL_BEST

        if select_opt == OPT_LIDER:
            if self.__is_int(p_select) or p_select == ZERO_STR:
                return PRE_TEXT + ERR_SEL_LIDER

        return NULL

    """ Czy liczba jest flout >= 0 """
    @staticmethod
    def __is_ufloat(val) -> bool:
        try:
            float(val)
        except ValueError:
            return True

        if ZERO > float(val) or float(val) > ONE:
            return True

        return False

    """ Czy liczba jest flout """
    @staticmethod
    def __is_float(val) -> bool:
        try:
            float(val)
        except ValueError:
            return True

        return False

    """ Czy liczba jest int > 0 """
    @staticmethod
    def __is_int(val) -> bool:
        try:
            int(val)
        except ValueError:
            return True

        if int(val) <= ZERO:
            return True

        if DOT in val:
            return True

        return False

    """ Sprawdzanie poprawnosci zbioru """
    def __good_set(self, tab) -> bool:
        for el in tab:
            if self.__is_float(el):
                return True

        len_set = len(tab)
        for i in range(START, len_set, JUMP_TO):
            if float(tab[i]) >= float(tab[i+NEXT]):
                return True

        return False
