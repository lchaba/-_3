a = (input("куда двигается персонаж?\n"))
b = int(input("на сколько клеток? "))

if (a == 'вверх'):
    y = b
    print(0, y)
if  (a== 'вниз'):
    y = -b
    print(0, y)
if  (a== 'вправо'):
    x = b
    print(x, 0) 
if  (a== 'влево'):
    x = -b
    print(x, 0)       