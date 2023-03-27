N=int(input('Количество эспонатов '))
eksponat=[[int(input('Цена экспоната ')), int(input('Вес экспоната '))] for _ in range(N)]
M=int(input('Количество заходов '))
K=int(input('Количество килограмм '))
eksponat={eksponat[i][0]/eksponat[i][1]:eksponat[i] for i in range(N)}
ek_key=list(eksponat.keys())
for i in ek_key:
    if eksponat[i][1] > K:
        eksponat.pop(i)
result=[]
for i in range(M):
    money_kg=max(eksponat.keys())
    result.append(eksponat[money_kg])
    eksponat.pop(money_kg)
print(result)



