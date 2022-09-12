from Interfejs import Daty
import urllib.request
import sys

class Tworzenie_podwojnej_krotki:

    def Tworzenie_podwojnej_krotki():
        results = Daty.Daty()
        if results[1] == '1':
            wynik = Tworzenie_podwojnej_krotki.PL_WYK_KSE(results)
        else:
            wynik = Tworzenie_podwojnej_krotki.PL_GEN_WIATR(results)

        return(wynik)

    def PL_WYK_KSE(results1):
        data = results1[0]
        Nazwy=[]
        try:
            if data[0][:6] == data[1][:6]:

                if data[-1][:6] == data[-2][:6]:

                    lista=list(zip(data, data[1:]))[::2]

                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))


                else:

                    lista=list(zip((data[:-1]), (data[:-1])[1:]))[::2]
                    samotna_data2=data[-1]

                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url1='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data2)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url2='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data/{z}'.format(z = samotna_data2)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

            else:

                if data[-1][:6] == data[-2][:6]:

                    lista=list(zip(data[1:], (data[1:])[1:]))[::2]
                    samotna_data1=data[0]

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data1)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url1='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data/{z}'.format(z = samotna_data1)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))


                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url2='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url2, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                else:

                    lista=list(zip((data[1:-1]), (data[1:-1])[1:]))[::2]
                    samotna_data1=data[0]
                    samotna_data2=data[-1]

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data1)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url1='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data/{z}'.format(z = samotna_data1)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                    for daty1 in lista:

                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url2='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url2, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))


                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data2)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url3='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data/{z}'.format(z = samotna_data2)
                    urllib.request.urlretrieve(url3, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

            return Nazwy

        except:

            print('Najprawdopdobniej błąd strony\nPrawdopodobnie zostaly wpisane daty ktorych strona nie obsluguje')
            sys.exit()
        
    def PL_GEN_WIATR(results1):
        results = results1
        data = results[0]
        Nazwy=[]
        try:
            if data[0][:6] == data[1][:6]:

                if data[-1][:6] == data[-2][:6]:

                    lista=list(zip(data, data[1:]))[::2]

                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                else:

                    lista=list(zip((data[:-1]), (data[:-1])[1:]))[::2]
                    samotna_data2=data[-1]

                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url1='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data2)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url2='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data/{z}'.format(z = samotna_data2)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

            else:

                if data[-1][:6] == data[-2][:6]:

                    lista=list(zip(data[1:], (data[1:])[1:]))[::2]
                    samotna_data1=data[0]

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data1)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url1='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data/{z}'.format(z = samotna_data1)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))


                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url2='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url2, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    
                else:
                    
                    lista=list(zip((data[1:-1]), (data[1:-1])[1:]))[::2]
                    samotna_data1=data[0]
                    samotna_data2=data[-1]

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data1)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url1='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data/{z}'.format(z = samotna_data1)
                    urllib.request.urlretrieve(url1, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                    for daty1 in lista:
                        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                        Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                        url2='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                        urllib.request.urlretrieve(url2, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

                    nazwa_pliku = '{poczatek}'.format(poczatek = samotna_data2)
                    Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                    url3='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data/{z}'.format(z = samotna_data2)
                    urllib.request.urlretrieve(url3, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))

            return Nazwy

        except:

            print('Najprawdopdobniej błąd strony\nPrawdopodobnie zostaly wpisane daty ktorych strona nie obsluguje')
            sys.exit()

