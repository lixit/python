#avoid mutating a list as you are iterating over it
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

def remove_dups_copy(L1,L2):
    #L1_copy = L1[:]
    L1_copy = list(L1)
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4]
remove_dups(L1, L2)
print(L1)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4]
remove_dups_copy(L1,L2)
print(L1)
