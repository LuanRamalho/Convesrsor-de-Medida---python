import tkinter as tk
from tkinter import ttk

# Função para converter metros
def converter():
    try:
        metros = float(entry_metros.get())
        km.set(f"{metros / 1000:.3f} km")
        cm.set(f"{metros * 100:.0f} cm")
        mm.set(f"{metros * 1000:.0f} mm")
    except ValueError:
        km.set("Entrada inválida")
        cm.set("Entrada inválida")
        mm.set("Entrada inválida")

# Janela principal
root = tk.Tk()
root.title("Conversor de Medidas")
root.geometry("400x300")
root.config(bg="#e3f2fd")

# Título
titulo = tk.Label(root, text="Conversor de Medidas", font=("Arial", 20, "bold"), bg="#64b5f6", fg="white", pady=10)
titulo.pack(fill=tk.X)

# Frame para entrada
frame_input = tk.Frame(root, bg="#e3f2fd")
frame_input.pack(pady=20)

label_metros = tk.Label(frame_input, text="Digite o valor em metros:", font=("Arial", 12), bg="#e3f2fd", fg="#0d47a1")
label_metros.grid(row=0, column=0, padx=5, pady=5)

entry_metros = ttk.Entry(frame_input, font=("Arial", 12), width=15)
entry_metros.grid(row=0, column=1, padx=5, pady=5)

# Botão para converter
btn_converter = tk.Button(root, text="Converter", command=converter, font=("Arial", 12, "bold"), bg="#8B0000", fg="#7CFC00")
btn_converter.pack(pady=10)

# Resultados
frame_resultados = tk.Frame(root, bg="#e3f2fd")
frame_resultados.pack(pady=10)

km = tk.StringVar()
cm = tk.StringVar()
mm = tk.StringVar()

label_km = tk.Label(frame_resultados, textvariable=km, font=("Arial", 12), bg="#e3f2fd", fg="#1b5e20")
label_km.grid(row=0, column=0, pady=5)

label_cm = tk.Label(frame_resultados, textvariable=cm, font=("Arial", 12), bg="#e3f2fd", fg="#1b5e20")
label_cm.grid(row=1, column=0, pady=5)

label_mm = tk.Label(frame_resultados, textvariable=mm, font=("Arial", 12), bg="#e3f2fd", fg="#1b5e20")
label_mm.grid(row=2, column=0, pady=5)

root.mainloop()
