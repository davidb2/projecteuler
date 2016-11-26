class Trit:
    mapping = ['R', 'G', 'B']

    def __init__(self, int_value):
        self.int_value = int_value
        self.str_value = _to_trinary(int_value)
        self.is_valid  = _is_valid_trit(self.str_value)
        self.size      = len(str_value)
    
    def _to_trinary(n):
        assert 0 <= n
        if n == 0:
            return 'R'
        tri = ''
        while n:
            tri.append(mapping[n%3])
            n //= 3
        return tri[::-1]

    def _is_valid_trit(trit):
        for i in range(1, len(trit)):
            if trit[0] == trit[1]:
                return False
        return True
    
    def is_valid_seq(self, other):
        assert type(self) == type(other)
        if self.size != other.size - 2:
            return False
        for e in range(0, self.size, 2):
            if self.str_value[e] == other.str_value[e+1]:
                return False
        return True

    def num_of_n_length_trits(n):
        return 3 ** n


LIMIT = 15
cache = {}

def ways(level, state):
    if level > LIMIT:
        return 1
    elif (level, state) not in cache