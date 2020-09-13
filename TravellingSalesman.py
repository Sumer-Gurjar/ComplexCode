n = int(input("Enter the number of village:"))
arr = [[0 for j in range(n)] for i in range(n)]
completed = [0 for j in range(10)]
cost=0

def takeInput():
    for i in range(0, n):
        for j in range(0, n):
            arr[i][j] = int(input('Enter the cost of Matrix:'))
        completed[i] = 0

    print ("Cost list")

    for i in range(0, n):
        for j in range(0, n):
            print arr[i][j]

def mincost(city):
    global cost
    completed[city] = 1
    print (' ---> %d' % int(city + 1))
    ncity = least(city)

    if ncity == 999:
        ncity = 0
        print (' %d' % int(ncity + 1))
        cost += arr[city][ncity]
        return
    mincost(ncity)

def least(c):
    global cost
    nc = 999
    minc = 999

    for i in range(0, n):
        if arr[c][i] != 0 and completed[i] == 0:
            if arr[c][i] + arr[i][c] < minc:
                minc = arr[i][0] + arr[c][i]
                kmin = arr[c][i]
                nc = i

    if minc != 999:
        cost += kmin
    return nc

takeInput()
print "\n\nThe Path is:\n"
mincost(0)
print "\n\nMinimum cost is :", int(cost)
