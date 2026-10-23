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
print(condition1 and condition2 and condition3)
if condition1 and condition2 and condition3:
    print("Todas las condiciones son cumplidas")

print("Práctica 2")
#Con el comando "or", si una de las condiciones es verdadera, sobreescribe a la otra

print(condition1 or condition2)
print(condition1 or condition3)
if condition1 or condition2 or condition3:
    print("Una de las condiciones se cumple")