from collections import Iterator
class CircularList(Iterator):
    def __init__(self, arr):
        self.arr = arr
        self._index = 0
    
    def __len__(self):
        return len(self.arr)

    @property
    def current(self):
        return self.arr[self._index]

    def __iter__(self):
        return self
    
    def next(self):
        data = self.arr[self._index]
        self._index = (self._index + 1) % len(self.arr)
        return data

class Die:
    def __init__(self, sides):
        import random
        self.random = random
        self.sides = sides

    def roll(self):
        return self.random.randint(1, self.sides)

class Monopoly:
    positions = 'H2 T2 H1 CH3 R4 G3 CC3 G2 G1 G2J F3 U2 F2 F1 R3 E3 E2 CH2 E1 FP D3 D2 CC2 D1 R2 C3 C2 U1 C1 JAIL B3 B2 CH1 B1 R1 T1 A2 CC1 A1 GO'.split()[::~0]
    def __init__(self, sides):
        from random import shuffle
        '''Initializes the board'''
        self.moves = 0
        self.landings = dict(zip(Monopoly.positions, [0 for _ in xrange(len(Monopoly.positions))]))
        self.dice1, self.dice2 = Die(sides), Die(sides)
        self.squares = CircularList(Monopoly.positions)
        self.community_chest = CircularList(['GO', 'JAIL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.chance = CircularList(['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', -3, 0, 0, 0, 0, 0, 0])
        self.doubles = 0
        shuffle(self.community_chest.arr)
        shuffle(self.chance.arr)
    
    def simulate_turn(self):
        '''Simulates a turn'''
        num1, num2 = self.dice1.roll(), self.dice2.roll()
        if num1 == num2:
            self.doubles += 1
        
        if self.doubles == 3:
            self.doubles = 0
            self.goto('JAIL')
        elif num1 == num2:
            self.goto(num1+num2, land=False)
        else:
            self.goto(num1+num2)

    def goto(self, place, land=True):
        if isinstance(place, int):
            # we can only go forward
            place = place if place >= 0 else place + len(self.squares)
            for _ in xrange(place):
                # go forward
                self.squares.next()
        elif isinstance(place, str):
            # print place
            while True:
                # go forward 
                self.squares.next()
                # print self.squares.current
                if self.squares.current.startswith(place):
                    # we need to stop
                    break
        else:
            raise Exception('the parameter \'place\' cannot be of type {}'.format(type(place)))
        
        # get landing
        curr = self.squares.current
        if curr == 'G2J':
            self.goto('JAIL')
        elif curr.startswith('CC'):
            card = self.community_chest.next()
            self.goto(card)
        elif curr.startswith('CH'):
            card = self.chance.next()
            self.goto(card)
        else:
            self.landings[curr] += int(land)
            self.moves += int(land)
    
    @property
    def top_three(self):
        data = sorted([(k,v) for k,v in self.landings.iteritems()], key=lambda x: x[~0])
        return '{}{}{}'.format(
            str(Monopoly.positions.index(data[~0][0])).rjust(2, '0'),
            str(Monopoly.positions.index(data[~1][0])).rjust(2, '0'),
            str(Monopoly.positions.index(data[~2][0])).rjust(2, '0'),
        )

if __name__ == '__main__':
    SIDES = 6
    EPS   = 100000
    game = Monopoly(SIDES)
    for _ in xrange(EPS):
        game.simulate_turn()
    # print game.landings
    print game.top_three