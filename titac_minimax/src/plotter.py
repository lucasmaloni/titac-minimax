from entities.node import Node
import networkx as nx
import matplotlib.pyplot as plt

class Plotter:
    
    def plot_tree(self, root_node: Node):
        '''function to plot the decision tree'''
        graph = nx.DiGraph()
        node_labels = {}
        
        self.conect_nodes(root_node, graph, node_labels)
            
        plt.figure(figsize = (15, 10))
        positions = nx.drawing.nx_pydot.graphviz_layout(graph, prog='dot')
        nx.draw(graph, positions, labels=node_labels, with_labels = True)
        plt.show()
            
    def conect_nodes(self, root_node: Node, graph, labels: dict):
        '''aux function that recursively conects nodes in the graph'''
        labels[id(root_node)] = f"M:{root_node.move}\nS:{root_node.score}"
        graph.add_node(id(root_node))

        for child in root_node.children:
            graph.add_edge(id(root_node), id(child))
            self.conect_nodes(child, graph, labels)

    def print_root_info(self, root_node: Node, depth=0):
        '''recursively traversses the tree printing its information'''
        print(f"{' ' * depth}Nó com score: {root_node.score} e jogada: {root_node.move}")
        for child in root_node.children:
            self.print_root_info(child, depth+1)
