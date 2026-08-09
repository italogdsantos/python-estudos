x = int(input('Digite quantos números da sequência de Fibonacci: '))
t1 = 0
t2 = 1
x -= 2
print('0 -> 1 -> ', end='')
while x != 0:
    x -= 1
    t3 = t1 + t2
    print(f'{t3} ', end='')
    t1 = t2
    t2 = t3
    if x != 0:
        print('-> ', end='')
print('FIM')




