L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2 # operator + does not have a side effect. It creates a new list and returns it
print('L3=',L3)

L1.extend(L2) # mutated L1
print('L1=',L1)

L1.append(L2)
print('L1=',L1)

print(L1.count(4))

L1.insert(0,'insert')
print('Insert L1: ',L1)

L1.remove('insert')
print('after remove insert: ',L1)

L1.reverse()
print('After reverse the order: ',L1)

L1.sort()
print('sorted :',L1)
