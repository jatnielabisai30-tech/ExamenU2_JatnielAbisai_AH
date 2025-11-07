semilla = int(input("Ingrese una semilla: "))
n = int(input("Cuantos numeros quiere generar: "))

for i in range(n):
    cuadrado = semilla ** 2
    s = str(cuadrado).zfill(8)
    medio = int(s[2:6])
    r = medio/1000
    print(f"{i+1}. {semilla}²={s}")
    semilla = medio