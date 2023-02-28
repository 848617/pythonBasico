'''L=[1,2,3,4,5,6,7,8,9,10]
x=5
while x < len(L):
    print(L[x])
    x+=1'''

'''a = []
a.append('valor')
a.append('20,00  reais')
print(a)'''

L=[]
while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
x=0
while x < len(L):
    print(L[x])
    x=x+1