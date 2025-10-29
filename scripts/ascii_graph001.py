from ascii_graph import Pyasciigraph
from ascii_graph import colors

data = [('A' , 5, colors.Red) , ('B' , 3, colors.BGre) , ('C' , 9, colors.Blu) , ('D' , 6, colors.BIYel)]

graph = Pyasciigraph()

for line in graph.graph('Sample Graph', data):
    print(line)