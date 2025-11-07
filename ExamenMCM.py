semilla = 1234      
n = 5             

for i in range(n):
    cuadrado = semilla ** 2
    s = str(cuadrado).zfill(8)
    medio = int(s[2:6])
    r = medio / 1000   # opcional: genera número con decimales
    print(f"{i+1}. {semilla}² = {s}")
    semilla = medio
