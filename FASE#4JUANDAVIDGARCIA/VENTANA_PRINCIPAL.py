import tkinter as tk
from tkinter import messagebox


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        return self._insertar(self.raiz, valor, 1)

    def _insertar(self, nodo, valor, nivel):
        if valor == nodo.valor:
            return True

        if valor < nodo.valor:
            if nodo.izquierda is None:
                if nivel + 1 > 4:
                    raise ValueError("Máximo 4 niveles")
                nodo.izquierda = Nodo(valor)
                return True
            return self._insertar(nodo.izquierda, valor, nivel + 1)
        else:
            if nodo.derecha is None:
                if nivel + 1 > 4:
                    raise ValueError("Máximo 4 niveles")
                nodo.derecha = Nodo(valor)
                return True
            return self._insertar(nodo.derecha, valor, nivel + 1)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.valor)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

    def posorden(self):
        resultado = []
        self._posorden(self.raiz, resultado)
        return resultado

    def _posorden(self, nodo, resultado):
        if nodo is not None:
            self._posorden(nodo.izquierda, resultado)
            self._posorden(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    def limpiar(self):
        self.raiz = None


def dibujar_arbol(canvas, nodo, x, y, dx):
    if nodo is not None:
        if nodo.izquierda is not None:
            canvas.create_line(x, y, x - dx, y + 60, width=2)
            dibujar_arbol(canvas, nodo.izquierda, x - dx, y + 60, dx // 2)

        if nodo.derecha is not None:
            canvas.create_line(x, y, x + dx, y + 60, width=2)
            dibujar_arbol(canvas, nodo.derecha, x + dx, y + 60, dx // 2)

        canvas.create_oval(
            x - 20, y - 20, x + 20, y + 20,
            fill="lightblue", outline="black", width=2
        )

        canvas.create_text(
            x, y,
            text=str(nodo.valor),
            font=("Arial", 12, "bold")
        )


def actualizar_graficos(bst, canvas_arbol, txt_pre, txt_in, txt_pos):
    canvas_arbol.delete("all")

    if bst.raiz is not None:
        dibujar_arbol(canvas_arbol, bst.raiz, 400, 40, 120)

    txt_pre.config(state="normal")
    txt_in.config(state="normal")
    txt_pos.config(state="normal")

    txt_pre.delete("1.0", tk.END)
    txt_in.delete("1.0", tk.END)
    txt_pos.delete("1.0", tk.END)

    txt_pre.insert(tk.END, " -> ".join(map(str, bst.preorden())))
    txt_in.insert(tk.END, " -> ".join(map(str, bst.inorden())))
    txt_pos.insert(tk.END, " -> ".join(map(str, bst.posorden())))

    txt_pre.config(state="disabled")
    txt_in.config(state="disabled")
    txt_pos.config(state="disabled")


def principal():
    ventana = tk.Tk()
    ventana.title("Árbol Binario de Búsqueda")
    ventana.geometry("1000x700")
    ventana.configure(bg="#f0f0f0")

    bst = BST()

    titulo = tk.Label(
        ventana,
        text="Árbol Binario de Búsqueda",
        font=("Arial", 18, "bold"),
        bg="#f0f0f0"
    )
    titulo.pack(pady=10)

    frame_superior = tk.Frame(ventana, bg="#f0f0f0")
    frame_superior.pack(pady=10)

    tk.Label(
        frame_superior,
        text="Ingrese valor entero:",
        font=("Arial", 12),
        bg="#f0f0f0"
    ).grid(row=0, column=0, padx=5)

    entry_valor = tk.Entry(frame_superior, font=("Arial", 12), width=15)
    entry_valor.grid(row=0, column=1, padx=5)

    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=10)

    frame_arbol = tk.LabelFrame(
        ventana,
        text="Panel Árbol",
        font=("Arial", 12, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=10
    )
    frame_arbol.pack(padx=10, pady=10, fill="both")

    canvas_arbol = tk.Canvas(frame_arbol, width=850, height=300, bg="white")
    canvas_arbol.pack()

    frame_recorridos = tk.Frame(ventana, bg="#f0f0f0")
    frame_recorridos.pack(pady=10)

    frame_pre = tk.LabelFrame(
        frame_recorridos,
        text="Preorden",
        font=("Arial", 12, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=10
    )
    frame_pre.grid(row=0, column=0, padx=10)

    txt_pre = tk.Text(frame_pre, width=25, height=5, font=("Arial", 11))
    txt_pre.pack()
    txt_pre.config(state="disabled")

    frame_in = tk.LabelFrame(
        frame_recorridos,
        text="Inorden",
        font=("Arial", 12, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=10
    )
    frame_in.grid(row=0, column=1, padx=10)

    txt_in = tk.Text(frame_in, width=25, height=5, font=("Arial", 11))
    txt_in.pack()
    txt_in.config(state="disabled")

    frame_pos = tk.LabelFrame(
        frame_recorridos,
        text="Posorden",
        font=("Arial", 12, "bold"),
        bg="#f0f0f0",
        padx=10,
        pady=10
    )
    frame_pos.grid(row=0, column=2, padx=10)

    txt_pos = tk.Text(frame_pos, width=25, height=5, font=("Arial", 11))
    txt_pos.pack()
    txt_pos.config(state="disabled")

    def agregar():
        try:
            valor = int(entry_valor.get())
            bst.insertar(valor)
            actualizar_graficos(bst, canvas_arbol, txt_pre, txt_in, txt_pos)
            entry_valor.delete(0, tk.END)
        except ValueError as e:
            if str(e) == "Máximo 4 niveles":
                messagebox.showerror("Error", "No se permiten nodos en un nivel mayor a 4")
            else:
                messagebox.showerror("Error", "Debe ingresar un número entero")

    def buscar():
        try:
            valor = int(entry_valor.get())
            encontrado = bst.buscar(valor)
            if encontrado:
                messagebox.showinfo("Búsqueda", f"El nodo {valor} sí existe en el árbol")
            else:
                messagebox.showerror("Error", f"El nodo {valor} no existe en el árbol")
            entry_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero")

    def limpiar():
        bst.limpiar()
        actualizar_graficos(bst, canvas_arbol, txt_pre, txt_in, txt_pos)
        entry_valor.delete(0, tk.END)

    def salir():
        ventana.destroy()

    btn_agregar = tk.Button(frame_botones, text="Agregar Nodo", width=15, command=agregar, bg="#90ee90")
    btn_agregar.grid(row=0, column=0, padx=5)

    btn_buscar = tk.Button(frame_botones, text="Buscar Nodo", width=15, command=buscar, bg="#87cefa")
    btn_buscar.grid(row=0, column=1, padx=5)

    btn_limpiar = tk.Button(frame_botones, text="Limpiar", width=15, command=limpiar, bg="#f4a460")
    btn_limpiar.grid(row=0, column=2, padx=5)

    btn_salir = tk.Button(frame_botones, text="Salir", width=15, command=salir, bg="#f08080")
    btn_salir.grid(row=0, column=3, padx=5)

    ventana.mainloop()