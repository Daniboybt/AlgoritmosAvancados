from sys import setrecursionlimit
setrecursionlimit(20000)
n,t = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
a.sort()
def bb(x,y,v):
	m = (x+y)/2
	if x == y:
		return m
	if a[m] <= v:
		 return bb(m+1,y,v)
	elif a[m] > v:
		return bb(x,m,v)		 

lista = []

for i in b:
	print bb(0,len(a),i),
