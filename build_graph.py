import networkx as nx
import json
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

G = nx.Graph()

file ='file.txt'
data = []
# max_lines= 10000
with open(file) as f:
    for line_p in f:
        data.append(line_p.split(" "))
        # max_lines-=1
# print len(data)
arcs_tuples =[]
for doc in data:
    bigrams=ngrams(doc,2)
    arcs_tuples.extend(bigrams)
    counter = Counter(arcs_tuples)

unique_edges = set(arcs_tuples)
weighted_edges = []
for element in unique_edges:
    nodes = list(element)
    weight = counter[element]
    weighted_edge = (element[0], element[1], weight)
    weighted_edges.append(weighted_edge)

DG=nx.DiGraph()
DG.add_weighted_edges_from(weighted_edges)
nx.write_gexf(DG, "test.gexf")
