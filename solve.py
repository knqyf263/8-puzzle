#! /usr/bin/python

from pqueue import *
import time

adjacent = (
    (1, 3),       # 0
    (0, 2, 4),    # 1
    (1, 5),       # 2
    (0, 4, 6),    # 3
    (1, 3, 5, 7), # 4
    (2, 4, 8),    # 5
    (3, 7),       # 6
    (4, 6, 8),    # 7
    (5, 7)        # 8
)

OPEN = 0
CLOSE = 1
FORE = 0
BACK = 1

def make_distance_table(board, wide):
    size = len(board)
    table = [[0] * size for _ in xrange(size)]
    for i in xrange(size):
        p = board[i]
        if p == 0: continue
        x1 = i / wide
        y1 = i % wide
        for j in xrange(size):
            x2 = j / wide
            y2 = j % wide
            table[p][j] += max(x1 - x2, x2 - x1)
            table[p][j] += max(y1 - y2, y2 - y1)
    return table

def get_distance(board, distance):
    v = 0
    for x in xrange(9):
        p = board[x]
        if p == 0: continue
        v += distance[p][x]
    return v

class State:
    def __init__(self, board, space, prev, move, dir, kind = OPEN):
        self.board = board
        self.space = space
        self.prev = prev
        self.move = move
        self.dir = dir
        self.kind = kind
        if dir == FORE:
            dt = start_distance
        else:
            dt = goal_distance
        if prev is None:
            self.cost = move + get_distance(board, dt)
        else:
            p = board[prev.space]
            self.cost = prev.cost + 1 - dt[p][space] + dt[p][prev.space]

    def __cmp__(x, y):
        return x.cost - y.cost

def a_star_search(start, goal):
    global start_distance, goal_distance
    q = PQueue()
    table ={}
    start_distance = make_distance_table(goal, 3)
    a = State(start, start.index(0), None, 0, FORE)
    q.push(a)
    table[tuple(start)] = a
    goal_distance = make_distance_table(start, 3)
    a = State(goal, goal.index(0), None, 0, BACK)
    q.push(a)
    table[tuple(goal)] = a
    while not q.isEmpty():
        a = q.pop()
        if a.kind == CLOSE: continue
        for x in adjacent[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table:
                c = table[key]
                if a.dir != c.dir:
                    if a.dir == FORE:
                        print_answer(a)
                        print_answer_goal(c)
                    else:
                        print_answer(c)
                        print_answer_goal(a)
                    return
                if c.move > a.move + 1:
                    if c.kind == OPEN:
                        c.kind = CLOSE
                        c = State(b, x, a, a.move + 1, a.dir)
                        table[key] = c
                    else:
                        c.prev = a
                        c.cost = c.cost - c.move + a.move + 1
                        c.move = a.move + 1
                        c.kind = OPEN
                    q.push(c)
            else:
                c = State(b, x, a, a.move + 1, a.dir)
                q.push(c)
                table[key] = c
        a.kind = CLOSE

def print_answer(x):
    if x is not None:
        print_answer(x.prev)
        print x.board

def print_answer_goal(x):
    while x is not None:
        print x.board
        x = x.prev

a = [1,2,5,4,8,6,7,3,0]
goal = [1,2,3,4,5,6,7,8,0]

s = time.clock()
a_star_search(a, goal)
e = time.clock()
print "%.3f" % (e - s)
