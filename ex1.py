def fanc(t):
    print('**** **** ****', t[::-4])


def func(c):
    a = c[::-1]
    f = c
    if a == f:
        print('Слово палиндром')

t=input()
c=input()
func(c)
fanc(t)