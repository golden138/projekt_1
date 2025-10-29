import rich
import time
import random
from rich.progress import track
import rich.traceback

#czyszczenie konsoli
rich.get_console().clear()

#Pasek tytułowy
rich.get_console().rule('Przykład tytułu', style='bold green')

#print
rich.get_console().print('Hello :pile_of_poo: [bold magenta]rich[/bold magenta]!', style='italic red')

#paski postępu
for i in track(range(100), description='[bold green]Progress...[/bold green]'):
    time.sleep(random.random())

#robienie wyników błedu w ładny sposób
rich.traceback.install()

1/0