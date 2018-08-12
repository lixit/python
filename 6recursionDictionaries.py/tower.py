# This program assumes yor have three towers named fr, to and space. There is n disks on one of these towers. The biggest disk is at bottom, and the less big disk is on the top of the previces one. The sequence can not be changed at any given time. Then you move the disks from tower fr to tower to. The program print the step of this movements using recursion methord
def printMove(fr,to):
    print('move from',str(fr),'to',str(to))

def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)

Towers(5,2,1,3)
