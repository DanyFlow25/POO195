import tkinter.messagebox as messagebox

class Overflow:
    def __init__(self):
        self.valor = 0

    def operacion(self):
        try:
            resultado = self.valor ** 99999
            return resultado
        except OverflowError:
            messagebox.showerror("Error Overflow", "Error Overflow (Cantidad demasiado grande)")

    def establecer_valor(self, valor):
        self.valor = valor
