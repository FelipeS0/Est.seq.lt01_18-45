#Declaração de Variáveis
n1: int = 0
n2: int = 0
aux: int = 0 
dif: int = 0

#Início
n1 = int(input("Qual o primeiro número?"))
n2 = int(input("Qual o segundo número?"))
if n2 > n1:
 aux = n2
 n2 = n1
 
dif = (aux - n1)
print ("A diferença de valor entre", n1, "e", aux, "é", dif)
#fim 
