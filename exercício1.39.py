#Declaração de Variáveis
n: int = 0
cont: int = 0
qtde: int = 1

#Início
n = int(input("Qual a casa desejada do xadrez?"))
for cont in range (1, n + 1, 1):
    if cont ==1:
        qtde = 1 
        print ("Casa:", cont, "quantidade:", qtde)
        cont = cont + 1
    qtde*= 2
    print ("Casa:", cont, "quantidade:", qtde)
    cont = cont + 1
#Fim