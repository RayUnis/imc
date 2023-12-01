import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função calcular IMC
def calcular_imc():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get()) / 100  # Converter altura de cm para m
        imc = peso / (altura ** 2)
        resultado_label.config(text=f"IMC: {imc:.2f}")

        # Conectar ao banco de dados SQLite e inserir dados
        conn = sqlite3.connect('dados_pacientes.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (nome, endereco, peso, altura, imc) VALUES (?, ?, ?, ?, ?)",
                       (nome_entry.get(), endereco_entry.get(), peso, altura, imc))
        conn.commit()
        conn.close()

        # Atualizar a lista de pacientes
        atualizar_lista_pacientes()
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de que os valores de peso e altura sejam numéricos.")

# Função para limpar campos
def limpar_campos():
    nome_entry.delete(0, 'end')
    endereco_entry.delete(0, 'end')
    altura_entry.delete(0, 'end')
    peso_entry.delete(0, 'end')
    resultado_label.config(text="IMC:")

# Função para atualizar a lista de pacientes
def atualizar_lista_pacientes():
    # Limpar a lista de pacientes
    lista_pacientes.delete(0, 'end')

    # Conectar ao banco de dados SQLite e obter dados da tabela
    conn = sqlite3.connect('dados_pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM pacientes")
    pacientes = cursor.fetchall()
    conn.close()

    # Adicionar pacientes à lista
    for paciente in pacientes:
        lista_pacientes.insert('end', paciente[0])

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Campos de entrada
# ... (código existente)

# Resultado do IMC
# ... (código existente)

# Lista de Pacientes
lista_pacientes_label = tk.Label(janela, text="Lista de Pacientes:")
lista_pacientes_label.pack()

lista_pacientes = tk.Listbox(janela)
lista_pacientes.pack()

# Botões
# ... (código existente)

# Iniciar interface gráfica
janela.mainloop()
