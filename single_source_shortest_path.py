import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt


def generate_random_weighted_graph(num_nodes, max_edges, max_weight):
    # Knoten erstellen
    nodes = range(num_nodes)
    
    # Kanten und Gewichte speichern
    edges = []
    
    # Alle möglichen Kanten generieren
    possible_edges = list(itertools.combinations(nodes, 2))
    
    # Zufällig Kanten auswählen
    num_edges = random.randint(1, max_edges)
    selected_edges = random.sample(possible_edges, num_edges)
    
    for edge in selected_edges:
        weight = random.randint(100, max_weight)  # Gewicht zwischen 1 und max_weight
        edges.append((edge, weight))
        
    return nodes, edges


def draw_graph(nodes, edges):
    G = nx.Graph()
    
    # Knoten hinzufügen
    G.add_nodes_from(nodes)
    
    # Kanten hinzufügen
    for (u, v), weight in edges:
        G.add_edge(u, v, weight=weight)
    
    # Position der Knoten ermitteln
    pos = nx.spring_layout(G)
    
    # Kanten zeichnen und Gewichte als Labels hinzufügen
    labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.show()

# Parameter
num_nodes = 10
max_edges = 25  # Maximal mögliche Kanten
max_weight = 200  # Maximal mögliches Gewicht

# Graph generieren
nodes, edges = generate_random_weighted_graph(num_nodes, max_edges, max_weight)

# Graph zeichnen
draw_graph(nodes, edges)