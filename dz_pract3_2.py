
c = input("стоп-слово: ")
x=0 
y=0
while 1==1:
    a = (input("куда двигается персонаж?\n"))
    if a == c:
        break 
    b = int(input("на сколько клеток?\n "))
    if (a == 'вверх'):
        y = y + b
        print(x, y)
    if  (a== 'вниз'):
        y = y - b
        print(x, y)
    if  (a== 'вправо'):
        x = x + b
        print(x, y) 
    if  (a== 'влево'):
        x = x - b
        print(x, y)   
       