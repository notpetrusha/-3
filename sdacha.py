N=int(input('Введите сдачу '))
monetki={int(input('Номинал ')):int(input('Количество денег номинала ')), int(input('Номинал ')):int(input('Количество денег номинала ')),
         int(input('Номинал ')):int(input('Количество денег номинала ')), int(input('Номинал ')):int(input('Количество денег номинала '))}
monetki_sdacha={}

while N!=0:
    nominal= max(monetki.keys())
    n=N//nominal
    if n>0:
        if monetki[nominal]<=n:
            N-=nominal*monetki[nominal]
            monetki_sdacha[nominal]=monetki[nominal]
        else:
            N-=n*nominal
            monetki_sdacha[nominal] = n
    monetki.pop(nominal)
print(monetki_sdacha)




