#logical operators: or, and, not
#bool: true or false
b1 = True
b2 = False

print("Práctica 1")
#Con el comando "and", si una de las condiciones es falsa, sobreescribe a la otra

print(f"El tipo de variable que es 'b1' es {type(b1)} y su valor es {int(b1)} respectivamente")
print(f"El tipo de variable que es 'b2' es {type(b2)} y su valor es {int(b2)} respectivamente")

condition1 = True
condition2 = True
condition3 = False

print(f"Condition1 = {condition1}, Condition2 = {condition2}, Condition3 = {condition3}") #Condition1 = True, Condition2 = True, Condition3 = False

print(condition1 and condition2 and condition3)
if condition1 and condition2 and condition3:
    print("Todas las condiciones son cumplidas")

print("Práctica 2")
#Con el comando "or", si una de las condiciones es verdadera, sobreescribe a la otra

print(condition1 or condition2)
print(condition1 or condition3)
if condition1 or condition2 or condition3:
    print("Una de las condiciones se cumple")

print("Práctica 3")
#Con el comando "not", se invierte el valor de la condición

condition1 = not condition1

print(f"Condition1 = {condition1}, Condition2 = {condition2}, Condition3 = {condition3}") #Condition1 = False, Condition2 = True, Condition3 = False

if not condition1 and condition2 or condition3:
    print("Una de las condiciones se cumple")

print("Prioridad de operadores lógicos: ", False or False and True or False) #Prioridad de operadores lógicos:  True