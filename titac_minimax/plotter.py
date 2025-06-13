from node import Node
import networkx as nx

class Plotter:
    
    def plot_tree(self, root_node):
        '''function to plot the decision tree'''
        graph = nx.DiGraph()
        return

    def print_root_info(self, root_node: Node, depth=0):
        '''recursively traversses the tree printing its information'''
        print(f"{' ' * depth}Nó com score: {root_node.score} e jogada: {root_node.move}")
        for child in root_node.children:
            self.print_root_info(child, depth+1)
        
        return
