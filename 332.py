n = int(input())
res, tmp_res = 0, 0
x, y, z, t = 0, 0, 0, 0
while res < n :
    res = x ** 2
    x += 1
if x == 0 : x = 0
elif x == 2 : x = 1
else : x -= 2
res = x ** 2
print('x = ' + str(x))
tmp_res += res
# print(tmp_res)
# print()

if tmp_res != n :
    while res < n :
        res = tmp_res + y ** 2
        y += 1
if y == 0 : y = 0
elif y == 2 : y = 1
else : y -= 2
res = y ** 2
print('y = ' + str(y))
tmp_res += res
# print(tmp_res)
# print()

if tmp_res != n:
    while res < n :
        res = tmp_res + z ** 2
        z += 1

if z == 0 : z = 0
elif z == 2 : z = 1
else : z -= 2
res = z ** 2
print('z = ' + str(z))
tmp_res += res
# print(tmp_res)
# print()

if tmp_res != n :
    while res < n :
        res = tmp_res + t ** 2
        t += 1

if t == 0 : t = 0
elif t == 2 : t = 1
else : t -= 2
res = t ** 2
tmp_res += res
print('t = ' + str(t))
#print(tmp_res)


