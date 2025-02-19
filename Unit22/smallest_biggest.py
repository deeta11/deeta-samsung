import itertools
def per(lst):
    return sorted(list(itertools.permutations(lst))) #gives the return value in list of tuples of combinations(ex:[('2','3'),('3','2')])
n=input("Enter n:")
l=list(n)

p=per(l)
#To find the index of the next biggest number which is smallest
index_n=p.index(tuple(l))+1
if index_n>=(len(p)):
    print("Not possible")
else:
    print("".join(p[index_n]))