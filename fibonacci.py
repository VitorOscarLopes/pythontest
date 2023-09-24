n = int(input('Digit a number: '))
a = 1
b = 0
c = 0
if n == 1:
    print('0 ', end='')
else:
    print('0, 1', end='')
while c < n - 2:
    f = a + b
    b = a
    a = f
    c += 1
    print(',', f, end='')
