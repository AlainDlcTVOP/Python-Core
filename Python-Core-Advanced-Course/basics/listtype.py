lst= [10,20,'KUNGEN',-10,30]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40)
lst.remove('KUNGEN')
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 66)
print(lst)