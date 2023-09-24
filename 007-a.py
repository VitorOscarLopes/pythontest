n1 = float(input('Digit the first number: '))
n2 = float(input('Digit the second number:'))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
rd = n1 // n2
e = n1 ** n2

print('THE RESULT OF THE \n Sum: {} \n Subtraction: {} \n Multiplication: {} \n Division: {:.3f} \n Division int:{} '
      '\n Exponential: {}'.format(s, sub, m, d, rd, e))
