import networkx
import matplotlib.pyplot
from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List


class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int
    def __init__(self, data,index):
        self.data = data
        self.index = index
    def __str__(self) -> str:
        return(str(self.data+ self.index))

class Edge:
        source: Vertex
        destination: Vertex
        weight: Optional[float]
        def __init__(self, source, destination, weight):
            self.source = source
            self.destination = destination
            self.weight=weight
class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
    def __init__(self):
        self.adjacencies ={}
        self.index=0
    def get_Vertex(self, index):
        for key in (self.adjacencies).keys():
            if key.index ==index:
                return key
    def has_edges(self, vertex):
        if (self.adjacencies.get(vertex)!= []):
            return True
        else:
            return False

    def has_edges_id(self, index):
        if (self.adjacencies.get(self.get_Vertex(index)) != []):
            return True
        else:
            return False
    def create_vertex(self, data: Any) -> Vertex:
        self.adjacencies [Vertex(data,self.index)] = []
        self.index = self.index+1
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source,destination,weight))
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        zwracacz = 0
        # print(self.head)
        scope = self.head
        while (scope != None):
            zwracacz+=1
            scope = scope.next
        return zwracacz
    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        zwracacz = 0
        # print(self.head)
        scope = self.head
        while (scope != None):
            zwracacz+=1
            scope = scope.next
        return zwracacz
    def show(self):
        graf = networkx.DiGraph()
        for key, value in self.adjacencies.items():
            for wartosc in self.adjacencies.get(key):
                networkx.add_path(graf, [(wartosc.source).index,(wartosc.destination).index])
        matplotlib.pyplot.figure(figsize=(15, 15))
        networkx.draw_networkx(graf, with_labels=True)
        matplotlib.pyplot.show()
    def __str__ (self):
        zwracacz=""
        for key, value in self.adjacencies.items():
            zwracacz += "ID: "
            zwracacz += str(key.index)
            lista = []
            zwracacz += ", wartosc "
            zwracacz += str(key.data)
            zwracacz += " ----> [  "
            id_robocze = None
            if (self.get_Vertex(id_robocze) in lista):
                pass
            for wartosc in self.adjacencies.get(key):
                zwracacz += str((wartosc.source).index)
                zwracacz += ": "
                zwracacz += str((wartosc.destination).index)
                zwracacz += ", "
            zwracacz = zwracacz[:-2]
            zwracacz += "]\n"
        return zwracacz
def pomocnicza(lista_mala:[Vertex],lista_duza:[Vertex], g: Graph, id, value, blacklist):
    lista_mala.append(value)
    blacklist.append(value)
    if (g.has_edges(g.get_Vertex(lista_mala[-1])) == True):
            for wartosc in g.adjacencies.get(g.get_Vertex(lista_mala[-1])):
                if (wartosc.destination).index not in blacklist:
                    pomocnicza(lista_mala.copy(),lista_duza, g, id,(wartosc.destination).index,blacklist)
                elif (wartosc.destination).index == id:
                    lista_mala.append(id)
                    lista_duza.append(lista_mala)
                    return []
                else:
                    return []
    else:
            return []

def dead_path(g: Graph, cross_id: Any):
    duza=[]
    mala=[]
    blacklist=[]
    pomocnicza(mala,duza,g,cross_id,cross_id,blacklist)
    konwerter_pomoc=[]
    finalny_zwrot=[]
    for sciezka in duza:
        konwerter_pomoc = []
        for id in sciezka:
            konwerter_pomoc.append(g.get_Vertex(id))
        finalny_zwrot.append(konwerter_pomoc)
    print(duza)
    if finalny_zwrot==[]:
        return None
    else:
        return finalny_zwrot

graf =Graph()
graf.create_vertex(3)
graf.create_vertex(2)
graf.create_vertex(2)
graf.create_vertex(4)
graf.add_directed_edge(graf.get_Vertex(2),graf.get_Vertex(0))
graf.add_directed_edge(graf.get_Vertex(0),graf.get_Vertex(1))
graf.add_directed_edge(graf.get_Vertex(1),graf.get_Vertex(2))
graf.add_directed_edge(graf.get_Vertex(3),graf.get_Vertex(1))
graf.add_directed_edge(graf.get_Vertex(3),graf.get_Vertex(0))

print(graf)
print(graf.has_edges(graf.get_Vertex(3)))
graf1 =Graph()
graf1.create_vertex(3)
graf1.create_vertex(2)
graf1.create_vertex(2)
graf1.create_vertex(4)
graf1.create_vertex(3)
graf1.create_vertex(2)
graf1.create_vertex(2)
graf1.create_vertex(4)
graf1.add_directed_edge(graf1.get_Vertex(1),graf1.get_Vertex(0))
graf1.add_directed_edge(graf1.get_Vertex(3),graf1.get_Vertex(1))
graf1.add_directed_edge(graf1.get_Vertex(1),graf1.get_Vertex(2))
graf1.add_directed_edge(graf1.get_Vertex(3),graf1.get_Vertex(2))
graf1.add_directed_edge(graf1.get_Vertex(3),graf1.get_Vertex(4))
graf1.add_directed_edge(graf1.get_Vertex(4),graf1.get_Vertex(2))
graf1.add_directed_edge(graf1.get_Vertex(2),graf1.get_Vertex(5))
graf1.add_directed_edge(graf1.get_Vertex(5),graf1.get_Vertex(6))
graf1.add_directed_edge(graf1.get_Vertex(6),graf1.get_Vertex(0))
graf1.add_directed_edge(graf1.get_Vertex(6),graf1.get_Vertex(4))
graf2 =Graph()
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.create_vertex(3)
graf2.add_directed_edge(graf2.get_Vertex(0),graf2.get_Vertex(3))
graf2.add_directed_edge(graf2.get_Vertex(2),graf2.get_Vertex(3))
graf2.add_directed_edge(graf2.get_Vertex(1),graf2.get_Vertex(11))
graf2.add_directed_edge(graf2.get_Vertex(11),graf2.get_Vertex(10))
graf2.add_directed_edge(graf2.get_Vertex(10),graf2.get_Vertex(8))
graf2.add_directed_edge(graf2.get_Vertex(8),graf2.get_Vertex(2))
graf2.add_directed_edge(graf2.get_Vertex(5),graf2.get_Vertex(11))
graf2.add_directed_edge(graf2.get_Vertex(3),graf2.get_Vertex(5))
graf2.add_directed_edge(graf2.get_Vertex(6),graf2.get_Vertex(10))
graf2.add_directed_edge(graf2.get_Vertex(4),graf2.get_Vertex(7))
graf2.add_directed_edge(graf2.get_Vertex(7),graf2.get_Vertex(0))
graf2.add_directed_edge(graf2.get_Vertex(6),graf2.get_Vertex(3))
graf2.add_directed_edge(graf2.get_Vertex(3),graf2.get_Vertex(8))
graf2.add_directed_edge(graf2.get_Vertex(11),graf2.get_Vertex(0))
graf2.add_directed_edge(graf2.get_Vertex(4),graf2.get_Vertex(9))
graf2.add_directed_edge(graf2.get_Vertex(9),graf2.get_Vertex(11))
graf2.add_directed_edge(graf2.get_Vertex(9),graf2.get_Vertex(2))
graf2.add_directed_edge(graf2.get_Vertex(7),graf2.get_Vertex(4))
graf2.add_directed_edge(graf2.get_Vertex(6),graf2.get_Vertex(2))
graf2.add_directed_edge(graf2.get_Vertex(6),graf2.get_Vertex(1))
graf2.add_directed_edge(graf2.get_Vertex(2),graf2.get_Vertex(1))
graf2.add_directed_edge(graf2.get_Vertex(2),graf2.get_Vertex(3))
graf2.add_directed_edge(graf2.get_Vertex(3),graf2.get_Vertex(7))
graf2.add_directed_edge(graf2.get_Vertex(1),graf2.get_Vertex(2))
graf2.add_directed_edge(graf2.get_Vertex(1),graf2.get_Vertex(10))
graf2.add_directed_edge(graf2.get_Vertex(10),graf2.get_Vertex(0))
graf2.add_directed_edge(graf2.get_Vertex(10),graf2.get_Vertex(7))
print(dead_path(graf,1))
print(dead_path(graf1,1))
print(dead_path(graf2,3))
graf.show()
graf1.show()
graf2.show()








