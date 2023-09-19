import random
empanadas = ["choclo", "carne", "JyQ", "pollo"]
caja=[]

cant = int(input("¿Cuantas empanadas queres? \n"))
for i in range(cant):
    intem = random.choice(empanadas)
    caja.append(intem)

print(caja)