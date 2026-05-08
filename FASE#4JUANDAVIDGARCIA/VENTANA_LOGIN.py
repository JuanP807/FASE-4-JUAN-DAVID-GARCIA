import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from VENTANA_PRINCIPAL import principal


def login(root):
    login_win = tk.Toplevel(root)
    login_win.title("Acceso a la Aplicación")
    login_win.geometry("450x300")
    login_win.configure(bg="#f0f0f0")

    tk.Label(
        login_win,
        text="APLICACION :ARBOLES BINARIOS",
        font=("Arial", 16, "bold"),
        bg="#f0f0f0"
    ).pack(pady=10)

    tk.Label(
        login_win,
        text="Estudiante: Juan David Garcia Paez",
        font=("Arial", 12),
        bg="#f0f0f0"
    ).pack(pady=5)

    tk.Label(
        login_win,
        text=f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",
        font=("Arial", 12),
        bg="#f0f0f0"
    ).pack(pady=5)

    tk.Label(
        login_win,
        text="Contraseña:",
        font=("Arial", 12),
        bg="#f0f0f0"
    ).pack(pady=5)

    pass_entry = tk.Entry(login_win, show="*", width=25, font=("Arial", 12))
    pass_entry.pack(pady=10)

    def verificar():
        if pass_entry.get() == "ARBOL":
            login_win.destroy()
            root.destroy()
            principal()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    tk.Button(
        login_win,
        text="Ingresar",
        command=verificar,
        width=15,
        bg="#00eeff",
        font=("Arial", 11, "bold")
    ).pack(pady=20)


root = tk.Tk()
root.withdraw()
login(root)
root.mainloop()