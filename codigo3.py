from flask import Flask, render_template
from Arbol1 import Nodo

app = Flask(__name__)

def buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
       return nodo_inicial
    else:
        dato_nodo = nodo_inicial.get_datos()
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
    
        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados)
                if sol is not None:
                    return sol

        return None

@app.route('/')
def index():
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo = buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados)

    resultado = []
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    return render_template('index3.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
