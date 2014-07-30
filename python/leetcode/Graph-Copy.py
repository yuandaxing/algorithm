# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    
    # dictA contains all the node 
    # setB contains all the edges which the first is more than
    # the next.
    def cloneGraph(self, node):
        

class GraphNode :
    def __init__(self, v, *brothers) :
        self.v = v
        self.neighbors = brothers

root = GraphNode(10, GraphNode(2, GraphNode(1, GraphNode(3),
                                                      GraphNode(4))
                               ,GraphNode(7))
                 ,GraphNode(4))

def SearchGraph(root):
    hasVisit = set([root])
    queue = [root]
    while len(queue) > 0 :
        first = queue[0]
        for child in first.neighbors :
            if child not in hasVisit:
                queue.append(child)
                print child.v
                hasVisit.add(child)
        queue = queue[1:]
SearchGraph(root)
