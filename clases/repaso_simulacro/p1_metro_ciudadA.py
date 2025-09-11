# Escribe tu código aquí
from metro import primera, proxima

def esta_en(linea, estacion):

    prim = primera(linea)
    if prim == estacion:
        return True

    while True:
        prox = proxima(linea, prim)
        if prox == "" and prox != prim:
            return False
        if prox == estacion:
            return True
        prim = prox