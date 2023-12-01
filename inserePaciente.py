import tkinter as tk
from tkinter import messagebox
import sqlite3

# ... (código existente)

# Função para inserir paciente
def inserir_paciente():
    try:
        # Obter dados do usuário
        nome = nome_entry.get()
        endereco = endereco_entry.get()
        peso = float(peso_entry.get())
        altura = float(altura_entry.get()) / 100  # Converter altura de cm para m
        imc = peso / (altura ** 2)

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('dados_pacientes.db')
        cursor = conn.cursor()

        # Inserir paciente na tabela
        cursor.execute("INSERT INTO pacientes (nome, endereco, peso, altura, imc) VALUES (?, ?, ?, ?, ?)",
                       (nome, endereco, peso, altura, imc))

        conn.commit()
        conn.close()

        # Limpar campos após inserção
        limpar_campos()

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Paciente inserido com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de que os valores de peso e altura sejam numéricos.")

# ... (restante do código)

# Botão para inserir paciente
inserir_button = tk.Button(janela, text="Inserir Paciente", command=inserir_paciente)
inserir_button.pack()

# ... (restante do código)
