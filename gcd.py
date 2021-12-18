def gcd(u,v):
	if v != 0:
		return gcd(v,u%v)
	else:
		return u
u=input('gcd:\nu:\n')
v=input('v:\n')
print(gcd(u,v))
