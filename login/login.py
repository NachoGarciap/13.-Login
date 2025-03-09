import tkinter as tk
from tkinter import ttk, messagebox


class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0, 0)  # para que no se pueda hacer mas grande ni pequeña

        # configurar el grid
        self.columnconfigure(0, weight=1)  # 1º columna ancho=1
        self.columnconfigure(1, weight=3)  # 2º columna ancho=3

        # creamos los componentes
        self._crear_componentes()

    # definir el metodo crear componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login',
                            f'Usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')


