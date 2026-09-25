#Declaration of a variable of a chain variable
name = "Alice"
#Declaration of an integer variable
age = 30
#Print something
print(name)
print(age)
#Change of the value of the variable "name"
name = "Bob"
print(name)

#Change of the value of the variable "age"
age = 45
print(age)
#The function "type()" is used to read the type of an object
print(type(name))

print(type(0.25))
print(type(10))
#Aqui "type" no va a decir de que tipo es la variable name, sino el tipo que es el valor de esa variable
print(type(age))

#("str" es para cadenas de texto, "int" para enteros, "float" para decimales, "bool" para booleanos)

is_running=True
#Estas dos lineas de abajo
variable_type = type(is_running)
print(variable_type)
is_running=56
#Es lo mismo que poner esta linea de abajo
print(type(is_running))