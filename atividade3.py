def impoupar(x):
    val = int(x) % 2 == 0
    if val: return 'este numero é par'
    else: return 'este numero é impar'

sn=(input('você deseja verificar se algum numero é par ou impar? '))
while sn == 'sim': 
   n=input('qual seria este numero? ')
   digito = n.isnumeric()
   if digito: print(impoupar(n))
   else: print('isso nao é um numero')
   sn=(input('deseja continuar? '))
   if sn == 'nao': 
       break
   else:
       sn = input('digite sim ou nao. Aqui ')
print('obrigado por usar')