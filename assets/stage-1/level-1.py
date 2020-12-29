from main import *
is_completed = false

a = choice(numbers)
b = choice(numbers)
answer = a + b
myAnsw = int(input())
def checkAnsw():
    if myAnsw != answer:
        print('Wrong')
    elif myAnsw == answer:
    print('Right')


print('Question 1:')
print(f'{a} + {b} = ???')
