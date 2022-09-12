from Dni_miesiaca import Date

class Daty:

    def Daty():

        Liczba = input('1-Wielkosci podstawowe \n2-generacja zrodel wiatrowych i fotowoltaicznych\n-->')

        if Liczba == '1':
            Rokpoczatkowy=input('Podaj poczatkowy rok\n-->')
            Miesiacpoczatkowy=input('Podaj poczatkowy miesiac\n-->')
            Dzienpoczatkowy=input('Podaj poczatkowy dzien\n-->')
            Rokkoncowy=input('Podaj koncowy rok\n-->')
            Miesiackoncowy=input('Podaj koncowy miesiac\n-->')
            Dzienkoncowy=input('Podaj koncowy dzien\n-->')
            Slownik = Date(Rokpoczatkowy, Rokkoncowy, Miesiacpoczatkowy, Miesiackoncowy, Dzienpoczatkowy, Dzienkoncowy)
            Lista=Slownik.Przygotowanie_danych()
        else:
            Rokpoczatkowy=input('Podaj poczatkowy rok\n-->')
            Miesiacpoczatkowy=input('Podaj poczatkowy miesiac\n-->')
            Dzienpoczatkowy=input('Podaj poczatkowy dzien\n-->')
            Rokkoncowy=input('Podaj koncowy rok\n-->')
            Miesiackoncowy=input('Podaj koncowy miesiac\n-->')
            Dzienkoncowy=input('Podaj koncowy dzien\n-->')
            Slownik = Date(Rokpoczatkowy, Rokkoncowy, Miesiacpoczatkowy, Miesiackoncowy, Dzienpoczatkowy, Dzienkoncowy)
            Lista=Slownik.Przygotowanie_danych()

        return Lista, Liczba


