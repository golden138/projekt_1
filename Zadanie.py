import sys
import argparse
from collections import defaultdict # do tworzenia słownika
from ascii_graph import Pyasciigraph # potrzebne do tworzenia histogramu
import string # proste przekszałcenia stringów
import locale # potrzebne do porównania słów z polskimi znakami
import rich # ładne kolorowanie
import platform # do wykrycia systemu po to aby sortować słowa polskie
from rich.progress import track # pasek postępu

parser = argparse.ArgumentParser(description='Skrypt do rysowania histogramu wyrazów występujących w pliku')
parser.add_argument('filename', help='Filename to process')
parser.add_argument('-L' , '--lang', help='Select language (PL or EN)', default='EN')
parser.add_argument('-l', '--length', help='number of words in the histogram', type=int, default=10)
parser.add_argument('-a', '--all', help='use all the words (boolean flag)', action='store_false')
parser.add_argument('-s', '--sort', help='sort alphabetically or by frequency (a or f)', default='f')

args = parser.parse_args()

sciezka = args.filename
jezyk = args.lang
systemW = platform.system()
sortowanie = 'alfabetycznie'
if args.sort == 'f':
    sortowanie = 'po częstoliwości'

#czyszczenie konsoli
rich.get_console().clear()

#Pasek tytułowy
rich.get_console().rule('Skrypt do zlicznia występowania słów w pliku tekstowym')
rich.get_console().print(f'[bold green]Ścieżka do pliku:[/bold green] {sciezka}')
rich.get_console().print(f'[bold green]Wybrany język:[/bold green] {jezyk}')
rich.get_console().print(f'[bold green]Wykryty system:[/bold green] {systemW}')
rich.get_console().print(f'[bold green]Typ sortowania:[/bold green] {sortowanie}')

# ********************************************************************* Pobranie tekstu
tekst = ''
# otwieramy plik w trybcdie odczytu ('r')
with open(sciezka, "r", encoding="utf-8") as f:
    tekst = f.read()  # wczytuje cały plik jako jeden string

# **********************************************************************  Operacje na tekście sortowanie
# ustawienie języka do sortowania
if jezyk == 'EN':
    locale.setlocale(locale.LC_COLLATE, 'C')
else:
    if systemW == 'Windows':
        locale.setlocale(locale.LC_COLLATE, 'Polish_Poland.1250') # to dla windows
    else:
        locale.setlocale(locale.LC_COLLATE, 'pl_PL.UTF-8')  # Linux/Mac

def porownaj_A(a , b):
    return locale.strcoll(a, b) > 0

def porownaj_F(a , b):
    return a[1] < b[1]

def bubble_sort_A(lista):
    n = len(lista)
    for i in track(range(n), description='[bold red]Sortowanie słów alfabetycznie...[/bold red]'):
        for j in range(0, n-i-1):
            if porownaj_A(lista[j] , lista[j+1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# bubble sort
def bubble_sort_F(lista):
    n = len(lista)
    for i in track(range(n), description='[bold red]Sortowanie słów po częstotliwości...[/bold red]'):
        for j in range(0, n - i - 1):
            if porownaj_F(lista[j], lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# **********************************************************************  Operacje na tekście
# usunę wszystkie znaki interpunkcyjne z tekstu
tekst = tekst.translate(str.maketrans("", "", string.punctuation))
tekst = tekst.replace('«', '').replace('»', '')

# dziele tekst na słowa chyba tak najprościej
slowa = tekst.split()

# sortuje słowa alfabetycznie
if args.sort == 'a':
    slowa = bubble_sort_A(slowa)

# tworze słownik
slownik = defaultdict(int)

# lecę po słowach
for slowo in slowa:
    slownik[slowo] += 1

# sortowanie po częstotliwości
if args.sort == 'f':
    lista_slownik = list(slownik.items())
    posortowane = bubble_sort_F(lista_slownik)
    slownik = dict(posortowane)


# tworze histogram ze zliczeń
nn = len(slownik)
if args.all:
    nn =  args.length

slownik_items = list(slownik.items())[:nn]

graph = Pyasciigraph()
for line in graph.graph('Histogram', slownik_items):
    print(line)