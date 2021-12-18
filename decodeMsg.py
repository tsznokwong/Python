import gmpy2

msg = int("Firebird".encode("hex"), 16)

p = int(1e9 + 7)
q = int(1e9 + 9)
n = p * q
e = 17
phiN = (p - 1) * (q + 1)
d = gmpy2.powmod(e, -1, phiN)
print("d = " & d)
c = pow(msg, e, n)

m = pow(c, d, n)
print(format(m, "X").decode("hex"))


