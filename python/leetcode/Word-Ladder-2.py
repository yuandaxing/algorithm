class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    
    # from dict, find every word could transform to other
    # transformDict = {i:j for i in len(dict) for
    # j in range(j, len(dict)) if canTrans(dict[i], dict[j])
    # F[i][j] = min{F[i][k] + 1, F[i][j]} where i < j and 
    # transformDict.has_key(k, j)
    # N^4
    # Floyd algorithm O(N^3) algorithm
    # F[i][j]^K is the shorted path the immediate vertice is
    # [1, 2, 3, 4, 5, 6......K]
    # F[i][j]^(K+1) = min{F[i][j]^K, F[i][k]^K+F[k][j]^K}
    def __init__(self) :
        self.visited = set()
        self.path = []
    def PathSearch(self, prefixMap, i, j, cur) :
        cur.append(j)
        #print i, j, cur
        if i == j :
            self.path.append(list(cur)) 
        elif j in prefixMap :
            for k in range(1, len(prefixMap[j])) :
                self.PathSearch(prefixMap, i, prefixMap[j][k], cur)
        cur.pop() 
        
    def BFS(self, edge, i, j) :
        self.visited.add(i)
        prefixMap, queue={}, []
        queue.append((i, 1))
        prefixMap.setdefault(i, [1])
        while len(queue) :
            cur = queue.pop(0)
            for n in edge[cur[0]] :
                if not n in self.visited :
                    queue.append((n, cur[1]+1))
                    prefixMap.setdefault(n, [cur[1]+1, cur[0]])
                    self.visited.add(n)
                elif cur[1]+1 == prefixMap[n][0]:
                    prefixMap[n].append(cur[0])
#        print prefixMap
        self.PathSearch(prefixMap, i, j, [])
        return self.path
    def findLadders(self, start, end, dict):
        strs = list(dict); strs.append(start); strs.append(end);
        str2Cluster = {}
        for i in range(len(strs)) :
            for j in range(len(strs[i])) :
                key = strs[i][0:j]+strs[i][j+1:], j
                str2Cluster.setdefault(key, [])
                str2Cluster[key].append(i)
        edge = {}
        #print str2Cluster
        for k, v in str2Cluster.items() :
            for i in range(len(v)) :
                for j in range(i+1, len(v)) :
                    edge.setdefault(v[i], [])
                    edge[v[i]].append(v[j])
                    edge.setdefault(v[j], [])
                    edge[v[j]].append(v[i])
        res =  self.BFS(edge, len(dict), len(dict)+1)
        return [[strs[ele[j]] for j in range(len(ele)-1, -1, -1)] for ele in res]
        
sol = Solution()
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
print sol.findLadders("hot", "dog", ["hot","dog"])


