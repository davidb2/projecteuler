class DisjointSet(object):
    def __init__(self):
        self._map = {}
    
    def connected(self, obj1, obj2):
        return (
            obj1 in self._map and 
            obj2 in self._map and
            self._find_root(self._map[obj1])[0] == self._find_root(self._map[obj2])[0]
        )
    
    def union(self, obj1, obj2):
        if obj1 not in self._map:
            self._map[obj1] = obj1
        if obj2 not in self._map:
            self._map[obj2] = obj2
        
        obj1_root, obj1_height = self._find_root(obj1)
        obj2_root, obj2_height = self._find_root(obj2)

        if obj1_height < obj2_height:
            self._map[obj1_root] = obj2_root
        else:
            self._map[obj2_root] = obj1_root
    
    def connected_components(self):
        some_map = {}
        for key, value in self._map.items():
            root = self._find_root(key)[0]
            if root not in some_map:
                some_map[root] = 0
            some_map[root] += 1
        return some_map
    
    def _find_root(self, obj):
        acc = 0
        while obj != self._map[obj]:
            # path compression
            self._map[obj] = self._map[self._map[obj]]
            obj = self._map[obj]
            acc += 1
        return obj, acc