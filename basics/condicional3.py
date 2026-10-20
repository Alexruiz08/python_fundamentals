temperatura = int(input("Introduce una temperatura (Entre 0° y 40°): ")) #(entre 0 y 40)
humedad = float(input("Introduce una humedad (Entre 0 y 1): ")) #(entre 0 y 1)

#Medir si la temperatura es demasiado alta o demasiado baja
if temperatura >40 or temperatura <0:
    print("La temperatura es demasiado alta o demasiado baja")
#Medir niveles de humedad y temperatura
if temperatura >=0 and temperatura <5:
    if humedad >=0.5 and humedad <=0.7:
        print("La temperatura es demasiado baja y la humedad es alta")
elif temperatura >=5 and temperatura <10:
    if humedad >=0.5 and humedad <=0.7:
        print("La temperatura es moderada y la humedad es alta")
elif temperatura >=10 and temperatura <15:
    if humedad >=0.45 and humedad <=0.65:
        print("La temperatura es moderada y la humedad es moderada")
elif temperatura >=15 and temperatura <20:
    if humedad >=0.4 and humedad <=0.6:
        print("La temperatura es moderada y la humedad es moderada")
elif temperatura >=20 and temperatura <25:
    if humedad >=0.4 and humedad <=0.6:
        print("La temperatura es moderada y la humedad es moderada")
elif temperatura >=25 and temperatura <30:
    if humedad >=0.5 and humedad <=0.65:
        print("La temperatura es moderada y la humedad es moderada")
elif temperatura >=30 and temperatura <35:
    if humedad >=0.5 and humedad <=0.7:
        print("La temperatura es moderada y la humedad es alta")
elif temperatura >=35 and temperatura <=40:
    if humedad >=0.5 and humedad <=0.7:
        print("La temperatura es alta y la humedad es alta")
#Si la temperatura o la humedad no cumplen con los valores adecuados
else:
    print("La temperatura o humedad no es adecuada para la medición")