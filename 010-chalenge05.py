x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
print('-----------------------------------------------')
if x > y and x > z:
    print('O maior número digitado foi', x)
if y > x and y > z:
    print('O maior número digitado foi', y)
if z > y and z > y:
    print('O maior número digitado foi', z)

print('-----------------------------------------------')
if x < y and x < z:
    print('O menor número digitado foi', x)
if y < x and y < z:
    print('O menor número digitado foi', y)
if z < x and z < y:
    print('O menor número digitado foi', z)
print('-----------------------------------------------')
