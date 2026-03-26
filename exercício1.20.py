#Declaração de Variáveis
from math import sqrt
A: int = 0
B: int = 0
C: int = 0
delta: int = 0
r1: float = 0.0
r2: float = 0.0
div: int = 0

#início
A = int(input("Qual o seu valor de X^2?"))
B = int(input("Qual o seu valor de X?"))
C = int(input("Qual o seu valor de C?"))
div = (2 * A) 
delta = ((B ** 2) - (4 * A * C))
if delta > 0:
    r1 = ((-B) + sqrt(delta)) / div
    r2 = ((-B) - sqrt(delta)) / div
    print ("Suas raízes são:", r1, "e", r2)
    
elif delta == 0:
 r1 = (-B) / div
 print ("Sua raiz é única com valor de:", r1)

else:
   print ("Não possui raiz real") 
#fim 
    