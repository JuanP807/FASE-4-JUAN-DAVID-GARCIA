class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None
        self.profundidad = 0

    def insertar(self, valor):
        if self._insertar_rec(self.raiz, valor, 0)[1] > 4:
            raise ValueError("Máximo 4 niveles excedido")
        return True

    def _insertar_rec(self, nodo, valor, nivel):
        if nodo is None:
            self.raiz = Nodo(valor) if nivel == 0 else nodo
            return True, nivel + 1
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                return self._insertar_rec(nodo.izquierda, valor, nivel + 1)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                return self._insertar_rec(nodo.derecha, valor, nivel + 1)
        self.profundidad = max(self.profundidad, nivel + 1)
        return True, nivel + 1

    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_rec(nodo.izquierda, valor)
        return self._buscar_rec(nodo.derecha, valor)

    def preorden(self):
        return self._preorden_rec(self.raiz)

    def _preorden_rec(self, nodo):
        if not nodo:
            return []
        return [nodo.valor] + self._preorden_rec(nodo.izquierda) + self._preorden_rec(nodo.derecha)

    def inorden(self):
        return self._inorden_rec(self.raiz)

    def _inorden_rec(self, nodo):
        if not nodo:
            return []
        return self._inorden_rec(nodo.izquierda) + [nodo.valor] + self._inorden_rec(nodo.derecha)

    def posorden(self):
        return self._posorden_rec(self.raiz)

    def _posorden_rec(self, nodo):
        if not nodo:
            return []
        return self._posorden_rec(nodo.izquierda) + self._posorden_rec(nodo.derecha) + [nodo.valor]

    def limpiar(self):
        self.raiz = None
        self.profundidad = 0
        