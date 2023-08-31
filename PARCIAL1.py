# Función para calcular la distancia entre dos puntos en el plano cartesiano
def distancia(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

# Decorador que aplica el algoritmo "Divide y Vencerás" a la función pares_cercanos
def pares_cercanos_decorator(func):
    def wrapper(*args, **kwargs):
        # Llamada a la función original para obtener la lista de puntos
        points = func(*args, **kwargs)
        # Ordena los puntos por coordenada x antes de aplicar el algoritmo
        points.sort()
        # Llama a la función con Divide y Vencerás y devuelve el resultado
        return pares_cercanos_divide_conquer(points)
    return wrapper

# Aplica el decorador pares_cercanos_decorator a la función pares_cercanos
@pares_cercanos_decorator
def pares_cercanos(points):
    return points


# Función que busca pares cercanos 
def encontrar_pares_cercanos(puntos): #se utiliza para encontrar los pares de puntos más cercanos en una lista de puntos cuando el tamaño de la lista es pequeño 
    min_dist = float('inf')
    p1 = None
    p2 = None
    # Compara todas las combinaciones posibles de pares de puntos
    for i in range(len(puntos)):
        for j in range(i+1, len(puntos)):
            dist = distancia(puntos[i], puntos[j])
            # Actualiza el par más cercano si se encuentra una distancia menor
            if dist < min_dist:
                min_dist = dist
                p1 = puntos[i]
                p2 = puntos[j]
    return p1, p2, min_dist

# Función principal que implementa el algoritmo "Divide y Vencerás" para buscar pares cercanos
def pares_cercanos_divide_conquer(puntos):
    n = len(puntos)
    # Si hay pocos puntos, utiliza la funcion encontrar pares cercanos para encontrar los pares más cercanos
    if n <= 3:
        return encontrar_pares_cercanos(puntos)

    # Divide la lista de puntos en dos mitades
    mitad = n // 2
    punto_medio = puntos[mitad]

    izquierda = puntos[:mitad]
    derecha = puntos[mitad:]

    # Recursivamente busca pares cercanos en ambas mitades
    izquierda_pares = pares_cercanos_divide_conquer(izquierda)
    derecha_pares = pares_cercanos_divide_conquer(derecha)

    # Encuentra la distancia mínima entre los pares de las mitades y considera una "banda" en el medio
    min_dist = min(izquierda_pares[2], derecha_pares[2])
    cercanos_en_banda = cercanos_en_banda_divide_conquer(puntos, min_dist, punto_medio)

    # Compara las distancias mínimas y decide cuál tomar
    if cercanos_en_banda:
        return cercanos_en_banda
    elif min_dist == izquierda_pares[2]:
        return izquierda_pares
    else:
        return derecha_pares

# Función que busca pares cercanos en una "banda" definida por la distancia mínima
def cercanos_en_banda_divide_conquer(puntos, min_dist, punto_medio):
    banda = []
    # Filtra los puntos que están cerca de la línea vertical del punto medio
    for punto in puntos:
        if abs(punto[0] - punto_medio[0]) < min_dist:
            banda.append(punto)
    # Ordena los puntos en la "banda" por coordenada y
    banda.sort(key=lambda x: x[1])
    cercanos = None
    # Busca pares cercanos dentro de la "banda"
    for i in range(len(banda)):
        for j in range(i+1, min(i+8, len(banda))):  # Considera un subconjunto cercano en y
            dist = distancia(banda[i], banda[j])
            if dist < min_dist:
                min_dist = dist
                cercanos = (banda[i], banda[j], min_dist)
    return cercanos



# Puntos de ejemplo
puntos = [(1, 2), (5, 9), (3, 4), (8, 6), (2, 7)]
p1, p2, min_dist = pares_cercanos(puntos)
print("Punto 1:", p1)
print("Punto 2:", p2)
print("Distancia mínima:", min_dist)
