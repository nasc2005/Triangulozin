import matplotlib.pyplot as plt
import math

def tipo_triangulo(x, y, z):
    # Verificação de valores inválidos (lados <= 0)
    if x <= 0 or y <= 0 or z <= 0:
        return "Erro: Elemento digitado não forma um triangulo"

    # Verificação da desigualdade triangular
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        return "Erro: A soma de dois lados não pode ser menor ou igual ao terceiro lado"


    # Converter para radianos
    A = math.radians(x)
    B = math.radians(y)
    C = math.radians(z)
    
    # Supondo lado oposto a A como base = 1
    lado_a = 1  
    
    # Usando lei dos senos -> a/sin(A) = b/sin(B) = c/sin(C)
    k = lado_a / math.sin(A)
    lado_b = k * math.sin(B)
    lado_c = k * math.sin(C)
    
    # Colocando os pontos no plano:
    A_point = (0, 0)
    B_point = (lado_a, 0)
    
    # Ponto C com lei dos cossenos
    Cx = (lado_c**2 - lado_b**2 + lado_a**2) / (2 * lado_a)
    Cy = math.sqrt(lado_c**2 - Cx**2)
    C_point = (Cx, Cy)
    
    # Desenho
    plt.figure(figsize=(5,5))
    plt.plot([A_point[0], B_point[0], C_point[0], A_point[0]],
             [A_point[1], B_point[1], C_point[1], A_point[1]], 'b-')
    plt.fill([A_point[0], B_point[0], C_point[0]], 
             [A_point[1], B_point[1], C_point[1]], alpha=0.3, color='cyan')
    
    # Nomes dos pontos
    plt.text(A_point[0]-0.05, A_point[1]-0.05, "A", fontsize=12)
    plt.text(B_point[0]+0.05, B_point[1]-0.05, "B", fontsize=12)
    plt.text(C_point[0], C_point[1]+0.05, "C", fontsize=12)
    
    plt.axis("equal")
    plt.show()

    
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
