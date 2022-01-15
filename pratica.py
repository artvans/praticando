'''

while True:
 x = int(input("digite sua idade:"))

 if x>=18 and x<120:
    print(f'voce é maior, voce tem {x} anos')
 elif x>=120:
    print(f'vocé um vampiro, voce tem {x} anos')
 else:
    print(f'voce é menor, voce tem {x} anos')




while True:
    a = int(input('digite um numero:'))

    b = int(input('digite um numero:'))

    def soma(x,y):
        return x+y

    som =soma(a,b)

    print(f'a soma é:{som}')
'''

senha = "arthur"
leitura = " "
while (leitura != senha):
    leitura = input ("Digite a senha:")
    if leitura == senha :
       print ('Acesso liberado')
    else:
       print ('Senha incorreta. Tente novamente')