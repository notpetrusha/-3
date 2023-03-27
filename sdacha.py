N=int(input('Введите сдачу '))
monetki={int(input('Номинал ')):int(input('Количество денег данного номинала ')), int(input('Номинал ')):int(input('Количество денег данного номинала ')),
         int(input('Номинал ')):int(input('Количество денег данного номинала ')), int(input('Номинал ')):int(input('Количество денег данного номинала '))}
monetki_sdacha={}

while N!=0:
    nominal= max(monetki.keys())
    n=N//nominal
    if monetki[nominal]<=n:
        N-=nominal*monetki[nominal]
        monetki_sdacha[nominal]=monetki[nominal]
    else:
        N-=n*monetki[nominal]
        monetki_sdacha[nominal] = n
    monetki.pop(nominal)
print(monetki_sdacha)




