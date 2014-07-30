
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @ edge, vertex = set(), dict
    # @ DFS queue,edge, handle= queue.append(node),empty
    # @ while not len(queue) :
    # @      cur = queue.pop(0) 
    #        vertext.setDefault(cur, UndirectedGraphNode(cur.val))
    #         newcur = vertext[cur]
    # @      visited.add(cur) 
    # #      for n in cur.neighbors :
    #            if n in visited : continue 
    #            else visited.add(n)
    #            Vertext.setDefault(n, UndirectedGraphNode(n.val) 
    #            newcur.neighbors.add(vertext[n])
    #             
    def cloneGraph(self, node):
        vertexMap, visit, queue, newGraph = {}, set(), [], None
        if not node: return newGraph
        queue.append(node); visit.add(node)
        while len(queue) :
            cur = queue.pop(0)
            vertexMap.setdefault(cur, UndirectedGraphNode(cur.label))
            newCur = vertexMap[cur]
            if not newGraph: newGraph = newCur
            for n in cur.neighbors :
                if not n in visit :
                    queue.append(n); visit.add(n);
                vertexMap.setdefault(n, UndirectedGraphNode(n.label))
                newCur.neighbors.append(vertexMap[n])
        return newGraph
        
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

G = UndirectedGraphNode(-1)
sol = Solution()
print sol.cloneGraph(G)
