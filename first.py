import random
value=random.randint(0,10)
print("ADIVINA EN QUE NUMERO ESTOY PENSANDO DEL 0 AL 10 TIENES 3 OPORTUNIDADES")
numero=int(input())
for x in [1,2,3]:
    if(numero==value):
        print('ADIVINASTE')
        break
    if(numero>value):
        print('Menos digita otro numero')
        numero=int(input())
        break
    if(numero<value):
        print('Mas digita otro numero')
        numero=int(input())
        break

