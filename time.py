import time

summa = input('Сколько копеек нужно выдать сдачи: ')

start = time.clock()
monetki = [0, 0, 0, 0]
nominal = [50, 10, 5, 1]
s = int(summa)
print('Первый способ: time.clock:')
print('Ваша сдача:')
length = len(nominal)
for i in range(length):
    while s >= nominal[i]:
        s -= nominal[i]
        monetki[i] += 1
    print(monetki[i], 'монетки по', nominal[i], 'копеек')
print('Спасибо за покупку! Приходите еще!')
elapsed = (time.clock() - start)

print(elapsed)

print(' ')
print('**************************')
print(' ')

end = time.time()
monetki = [0, 0, 0, 0]
nominal = [50, 10, 5, 1]
s = int(summa)
print('Второй способ: time.time:')
print('Ваша сдача:')
length = len(nominal)
for i in range(length):
    while s >= nominal[i]:
        s -= nominal[i]
        monetki[i] += 1
    print(monetki[i], 'монетки по', nominal[i], 'копеек')
print('Спасибо за покупку! Приходите еще!')
elapsed = (time.time() - end)

print(elapsed)
