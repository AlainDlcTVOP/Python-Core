#object of class set don't allow duplicates
#it will not care about it
s={10,20,30,"XYZ",10,20,30,"XYZ"} 



s.update([88,99])
print(s)
print(type(s))

#print(s[0]) NO INDEXING 

#print(s[0:3]) don't allow slizing

#print(s*3) don't allow repetition

s.remove(30)
print(s)

f=frozenset(s) # only navigate
#f.remove([20])







