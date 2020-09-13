#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


class pzl:

    q = []
    map = {}
    i = 0
    inputMatrix = '123045786'

    def pop(self):
        return self.q.popleft()

    def add(self, string, n):
        if not string in self.map.keys():
            self.map[string] = n
            self.q.append(string)
            print 'Queue: ' + str(self.q)

    def up(self, string):
        a = string.find('0')

        if a > 2:
            print 'up'
            s = string[0:a - 3] + '0' + string[a - 2:a] + string[a - 3] \
                + string[a + 1:]
            self.add(s, self.map.get(string) + 1)
            if s == '123456780':
                print 'Solution Exists at Level' + str(self.map.get(s))
                sys.exit(0)

    def down(self, string):
        a = string.find('0')
        if a < 6:
            print 'down'
            s = string[0:a] + string[a + 3:a + 4] + string[a + 1:a + 3] \
                + '0' + string[a + 4:]
            self.add(s, self.map.get(string) + 1)
            if s == '123456780':
                print 'Solution Exists at Level' + str(self.map.get(s))
                sys.exit(0)

    def left(self, string):

        a = string.find('0')
        if a != 0 and a != 3 and a != 6:
            print 'left'
            s = string[0:a - 1] + '0' + string[a - 1] + string[a + 1:]
            self.add(s, self.map.get(string) + 1)
            if s == '123456780':
                print 'Solution Exists at Level' + str(self.map.get(s))
                sys.exit(0)

    def right(self, string):
        a = string.find('0')
        print string
        if a != 2 and a != 5 and a != 8:
            print 'right'
            s = string[0:a] + string[a + 1] + '0' + string[a + 2:]
            self.add(s, self.map.get(string) + 1)
            if s == '123456780':
                print 'Solution Exists at Level' + str(self.map.get(s))
                sys.exit(0)


p = pzl()
p.add(p.inputMatrix, 0)
i = 0
while p.q[0] != None:

    p.up(p.q[0])
    print '***p.q' + str(p.q[len(p.q) - 1])
    p.down(p.q[0])
    print '***p.q' + str(p.q[len(p.q) - 1])
    p.left(p.q[0])
    print '***p.q' + str(p.q[len(p.q) - 1])
    p.right(p.q[0])
    print '***p.q' + str(p.q[len(p.q) - 1])
    p.q.pop(0)
    i = i + 1
    if i == 30:
        break
print "Solution doesn't exist"
