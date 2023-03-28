resultado_anterior = 1

for i in range(1, 11):
    resultado = i * 60 / resultado_anterior
    print(resultado)
    resultado_anterior = resultado
