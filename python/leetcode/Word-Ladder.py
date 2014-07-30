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
    def canTrans(self, str1, str2) :
            diff = 0
            for i in range(len(str1)) :
                if str1[i] != str2[i] :
                    diff += 1
            return diff <= 1
            
    def BFS(self, edge, i, j) :
        self.visited.add(i)
        queue=[]
        queue.append((i, 1))
        while len(queue) :
            cur = queue.pop(0)
            if cur[0] == j : return cur[1] 
            for n in edge[cur[0]] :
                if not n in self.visited :
                    queue.append((n, cur[1]+1))
                    self.visited.add(n)
        return 0
        
    def ladderLength1(self, start, end, dict):
        strs = list(dict); strs.append(start); strs.append(end);
        edge = {}
        for i in range(len(strs)) :
            edge.setdefault(i, [])
            for j in range(i+1, len(strs)) :
                if self.canTrans(strs[i], strs[j]) :
                    edge[i].append(j)
                    edge.setdefault(j, [])
                    edge[j].append(i)
        return self.BFS(edge, len(dict), len(dict)+1)

    def ladderLength(self, start, end, dict):
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
        return self.BFS(edge, len(dict), len(dict)+1)


start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
sol = Solution()
print sol.ladderLength("talk", "tail", ["talk","tons","fall","tail","gale","hall","negs"])        

