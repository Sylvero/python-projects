a = 29
b = 123457
c = str(b)
suma = 0

def waga(liczba,czyParzysta):
    if czyParzysta == 1:
        if liczba < 5:
            return liczba*2
        else:
            temp = list(str(liczba*2))
            return int(temp[0])+int(temp[1])
    else:
        return liczba

for j in range(0,999999):
    listaCyfr = list(str(j))
    for i,c in enumerate(listaCyfr):
        if i % 2 == 0:
            suma += waga(int(listaCyfr[i]),1)
        else:
            suma += waga(int(listaCyfr[i]), 0)

    if int('543210' + ''.join(listaCyfr) +'1234') % b == 0 and (a+suma) % 10 == 0:
        print(a+suma)
        print(f'543210' + ''.join(listaCyfr) +'1234')

    suma = 0

