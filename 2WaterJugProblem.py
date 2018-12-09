# 2 Water Jug Problem by Sumer

def pour(jug1, jug2):
    
	max1, max2, fill = 3, 4, 2  #Change maximum capacity and final capacity
    print("%d\t%d" % (jug1, jug2))
    
	if jug1 is fill:
        return
    
    elif jug1 != 0 and jug2 is 0:
        pour(0, jug1)
    
    elif jug1 < max1:
        pour(max1, jug2)

    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)
 
print("JUG1\tJUG2")
pour(0, 0)

# --------
# OUTPUT
# --------

# JUG1	JUG2
# 0		0
# 3		0
# 0		3
# 3		3
# 2		4