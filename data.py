from time import localtime

dt = localtime()[0:6]
d = dt[0] * 10000 + dt[1] * 100 + dt[2]
t = dt[3] * 10000 + dt[4] * 100 + dt[5]

print(d,t)

d = d.to_bytes(4, 'big')
t = t.to_bytes(4, 'big')

print(d,t)



dt = []

dt.append(d+t)

print(dt)
print(type(dt))