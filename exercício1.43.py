#Declaração de Variáveis
Ana: float = 1.10
Maria: float = 1.5
cont: int = 0

#Início
while Ana <= Maria:
    Ana = Ana + 0.03
    Maria = Maria + 0.02
    cont = cont + 1
print ("Depois de", cont, "anos, Ana é maior que Maria!")
print ("Ana:", round(Ana, 2), "Maria:", round(Maria, 2))
#fim