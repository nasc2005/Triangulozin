def tipo_triangulo(x, y, z):
    # Verificação de valores inválidos (lados <= 0)
    if x <= 0 or y <= 0 or z <= 0:
        return "Erro: Elemento digitado não forma um triangulo"

    # Verificação da desigualdade triangular
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        return "Erro: A soma de dois lados não pode ser menor ou igual ao terceiro lado"

    # Identificação do tipo de triângulo
    if x == y == z:
        return "Triângulo Equilátero"
    elif x == y or x == z or y == z:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


# Programa principal
if __name__ == "__main__":
    try:
        x = float(input("Digite o valor do lado x: "))
        y = float(input("Digite o valor do lado y: "))
        z = float(input("Digite o valor do lado z: "))

        resultado = tipo_triangulo(x, y, z)
        print(resultado)

    except ValueError:
        print("Erro: Elemento digitado não forma um triangulo")
