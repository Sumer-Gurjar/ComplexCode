# ----------------------------
# TOWER OF HANOI
# ----------------------------

def moveTower(h,frompole,topole,withpole):
    if h>=1:
        moveTower(h-1,frompole,withpole,topole)
        moveDisk(frompole,topole)
        moveTower(h-1,withpole,topole,frompole)

def moveDisk(fp,tp):
    print("Disk :",fp,"to",tp)

disk=int(input("Enter the Disks : "))
moveTower(disk,"A","B","C")



# --------
# OUTPUT
# --------

# Enter the Disks : 3
# Disk : A to B
# Disk : A to C
# Disk : B to C
# Disk : A to B
# Disk : C to A
# Disk : C to B
# Disk : A to B
