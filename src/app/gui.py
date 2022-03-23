import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tm
from src.different.examStartVal import ExamStartVal
from src.app.genAlg import GenAlg


TITLE = 'Aplikacja szukająca min.glo za pomocą alg.genetycznego'
TITLE_APP = 'Aplikacja'
TITLE_ENTRY = 'Liczba epok'
TITLE_SIZE_POPU = 'Rozmiar populacji'
TITLE_LEN_BIT = 'Rozmiar cechy'
TITLE_FUN_OPT = 'Funkcja do opt'
TITLE_SELECT = 'Funkcja selekcji'
TITLE_CROSS = 'Funkcja krzyzowania'
TITLE_MUTABLE = 'Funkcja mutacji'
TITLE_CROSS_PROP = 'Procent krzyzowania'
TITLE_MUTABLE_PROP = 'Procent mutacji'
TITLE_INVER_PROP = 'Procent inwersji'
TITLE_ELIT = 'Strategia elitarna'
TITLE_SET_X = 'Zakres dla X'
TITLE_SET_Y = 'Zakres dla Y'
TITLE_BUTTON = 'Start'
SIZE_WIN = '540x330+400+100'
COLUMN_1 = 10
COLUMN_2 = 270
ROW_1 = 50
ROW_2 = 80
ROW_3 = 110
ROW_4 = 140
ROW_5 = 170
ROW_6 = 200
ROW_7 = 230
MARGIN_2_ENTRY = 195
MARGIN_FROM = 95
MARGIN_TO = 170
FIRST = 0
WIDTH_ENTRY = 19
WIDTH_SET = 7
WIDTH_COMBOX = 16
WIDTH_BUTTON = 10
MARGIN_ROW = 120
FONT_TITLE = ('Arial', 12)
FONT_BUTTON = ('Arial', 10)
STATIC = 'readonly'
FROM = 'od'
TO = 'do'
NO = False
TWO_BIT = 2
NULL = ''
X_MIN, X_MAX = 0, 1
Y_MIN, Y_MAX = 2, 3
BUT_X, BUT_Y = 220, 290
TITLE_X, TITLE_Y = 70, 10
TITLE_ERROR = 'Bład danych'
VALUES = 'values'
OPT_FUN = (
    'ACKLEY', 'BEALE', 'BUKIN', 'DROP-WAVE',
    'GOLDSTEIN-PRICE', 'MCCORMICK', 'SCHAFFER 2',
    'HOLDER TAB'
)
OPT_SELECT = (
    'Koła ruletki', 'Najlepsi', 'Selekcja turniejowa'
)
OPT_CROSS = (
    'Jedno punktowe', 'Dwu punktowe',
    'Trzy punktowa', 'Jednorodne'
)
OPT_MUTABLE = (
    'Brzegowa', 'Jedno punktowa', 'Dwu punktowa',
    'Jednorodne'
)


class Gui:
    """ Klasa odpowiedzialma za wyswietlanie
    okna graficznego """

    def __init__(self):
        self.__main = tk.Tk()
        self.__epok = None
        self.__popu = None
        self.__len_bit = None
        self.__len_var = None
        self.__board = None
        self.__fun_opt = None
        self.__select = None
        self.__cross = None
        self.__mutate = None
        self.__button = None
        self.__cross_prop = None
        self.__mutable_prop = None
        self.__inver_prop = None
        self.__elit = None
        self.__opt_fun = tk.StringVar()
        self.__opt_select = tk.StringVar()
        self.__opt_cross = tk.StringVar()
        self.__opt_mutable = tk.StringVar()

        self.__set_gui()

    """ Funkcja uruchamia okno graficzne """
    def create(self) -> None:
        self.__main.mainloop()

    """ Ustawianie elementów gui """
    def __set_gui(self) -> None:
        self.__set_main()
        self.__set_title_win()
        self.__set_option_epok()
        self.__set_choise_win()
        self.__set_proc_entry()
        self.__set_entry_get_set()
        self.__set_button()

    """ Naniesienie tytułu strony na ekran """
    def __set_title_win(self) -> None:
        tk.Label(
            self.__main, text=TITLE, font=FONT_TITLE
        ).place(x=TITLE_X, y=TITLE_Y)

    """ Wyswietlanie opcji zwiazanych z epoka """
    def __set_option_epok(self) -> None:
        self.__epok = self.__put_entry(
            COLUMN_1, ROW_1, TITLE_ENTRY
        )

        self.__popu = self.__put_entry(
            COLUMN_1, ROW_2, TITLE_SIZE_POPU
        )

        self.__len_bit = self.__put_entry(
            COLUMN_1, ROW_3, TITLE_LEN_BIT
        )

        self.__elit = self.__put_entry(
            COLUMN_2, ROW_1, TITLE_ELIT
        )

    """ Wyswietlanie okien funkcji, selekcji, krzyzowania, mutacji """
    def __set_choise_win(self) -> None:
        self.__fun_opt = self.__put_combobox(
            COLUMN_1, ROW_4, TITLE_FUN_OPT,
            OPT_FUN, self.__opt_fun
        )

        self.__fun_select = self.__put_combobox(
            COLUMN_1, ROW_5, TITLE_SELECT,
            OPT_SELECT, self.__opt_select
        )

        self.__fun_cross = self.__put_combobox(
            COLUMN_1, ROW_6, TITLE_CROSS,
            OPT_CROSS, self.__opt_cross
        )

        self.__fun_mutable = self.__put_combobox(
            COLUMN_1, ROW_7, TITLE_MUTABLE,
            OPT_MUTABLE, self.__opt_mutable
        )

    """ Wyswietlanie okien do pobierania przedziałów """
    def __set_entry_get_set(self) -> None:
        x_min, x_max = self.__put_set_xy(
            COLUMN_2, ROW_5, TITLE_SET_X
        )

        y_min, y_max = self.__put_set_xy(
            COLUMN_2, ROW_6, TITLE_SET_Y
        )

        self.__board = [x_min, x_max, y_min, y_max]

    """ Wywoływanie okien do pobrania procentow """
    def __set_proc_entry(self) -> None:
        self.__cross_prop = self.__put_entry(
            COLUMN_2, ROW_2, TITLE_CROSS_PROP
        )

        self.__mutable_prop = self.__put_entry(
            COLUMN_2, ROW_3, TITLE_MUTABLE_PROP
        )

        self.__inver_prop = self.__put_entry(
            COLUMN_2, ROW_4, TITLE_INVER_PROP
        )

    """ Ustawianie okna głownego """
    def __set_main(self) -> None:
        self.__main.title(TITLE_APP)
        self.__main.geometry(SIZE_WIN)
        self.__main.resizable(width=NO, height=NO)

    """ Funkcja tworzy okno ENTRY """
    def __put_entry(self, row, col, text) -> tk:
        tk.Label(
            self.__main, text=text
        ).place(x=row, y=col)

        obj = tk.Entry(self.__main, width=WIDTH_ENTRY)
        obj.place(x=row + MARGIN_ROW, y=col)

        return obj

    """ Funkcja tworzy okno COMBOBOX """
    def __put_combobox(
            self, row, col, text, opt_fun, str_list
    ) -> tk:
        tk.Label(
            self.__main, text=text
        ).place(x=row, y=col)

        obj = ttk.Combobox(
            self.__main, textvariable=str_list,
            width=WIDTH_COMBOX, state=STATIC
        )

        obj.place(x=row + MARGIN_ROW, y=col)
        obj[VALUES] = opt_fun
        obj.current(FIRST)

        return obj

    """ Funkcja tworzy okna do pobrania przedziału """
    def __put_set_xy(self, row, col, text) -> ():
        tk.Label(
            self.__main, text=text
        ).place(x=row, y=col)

        tk.Label(
            self.__main, text=FROM
        ).place(x=row + MARGIN_FROM, y=col)

        obj_1 = tk.Entry(self.__main, width=WIDTH_SET)
        obj_1.place(x=row + MARGIN_ROW, y=col)

        tk.Label(
            self.__main, text=TO
        ).place(x=row + MARGIN_TO, y=col)

        obj_2 = tk.Entry(self.__main, width=WIDTH_SET)
        obj_2.place(x=row + MARGIN_2_ENTRY, y=col)

        return obj_1, obj_2

    """ Ustawianie przycisku uruchamiającego """
    def __set_button(self) -> None:
        self.__button = tk.Button(
            self.__main, text=TITLE_BUTTON,
            width=WIDTH_BUTTON, font=FONT_BUTTON,
            command=self.__click
        )

        self.__button.place(x=BUT_X, y=BUT_Y)

    """ Wykonuje sie w chwili nacisniecia przucisku """
    def __click(self) -> None:
        error = self.__test_var()

        if error == NULL:
            self.__run_calc()
        else:
            tm.showerror(TITLE_ERROR, error)

    """ Wywołani funkcji sprawdzajacej dane """
    def __test_var(self) -> str:
        test = ExamStartVal()

        return test.exam(
            self.__epok.get(), self.__popu.get(),
            self.__len_bit.get(),
            [
                self.__board[X_MIN].get(),
                self.__board[X_MAX].get(),
                self.__board[Y_MIN].get(),
                self.__board[Y_MAX].get()
            ],
            self.__elit.get(), self.__cross_prop.get(),
            self.__mutable_prop.get(), self.__inver_prop.get()
        )

    """ Uruchamianie algorytmu genetycznego """
    def __run_calc(self) -> None:
        app = GenAlg(
            int(self.__epok.get()), int(self.__popu.get()),
            TWO_BIT, int(self.__len_bit.get()),
            [
                float(self.__board[X_MIN].get()),
                float(self.__board[X_MAX].get()),
                float(self.__board[Y_MIN].get()),
                float(self.__board[Y_MAX].get()),
            ],
            self.__opt_fun.get(), self.__opt_select.get(),
            self.__opt_cross.get(), self.__opt_mutable.get(),
            int(self.__elit.get()), float(self.__cross_prop.get()),
            float(self.__mutable_prop.get()),
            float(self.__inver_prop.get())
        )

        app.run()
