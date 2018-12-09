# 3 WATER JUG PROBLEM By Sumer

def pour(jug1,jug2,jug3):
    max1,max2,max3,fill=12,8,3,6

    print("%d\t\t%d\t\t%d\n"%(jug1,jug2,jug3))
    if jug1 is fill and jug2 is  fill:
        return
    elif jug1 is  0:
        pour(max1,0,0)
    elif jug1 is max1:
        pour(jug1-max3,0,max3)
    elif jug3 is max3 and jug2 is 0:
        pour(jug1,jug3,0)
    elif jug3 is 0:
        pour(jug1-max3,jug2,max3)
    elif jug1 is fill and jug2!=fill:
        pour(jug1,jug2+jug3,0)

print("jug1\tjug2 \t jug3\n")
pour(0,0,0)

# --------
# OUTPUT
# --------

# jug1	jug2 	jug3

# 0		0		0

# 12	0		0

# 9		0		3

# 9		3		0

# 6		3		3

# 6		6		0