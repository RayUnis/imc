import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Função calcular IMC
def calcular_imc():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get()) / 100  # Converter altura de cm para m
        imc = peso / (altura ** 2)
        resultado_label.config(text=f"IMC: {imc:.2f}")

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('dados_pacientes.db')
        cursor = conn.cursor()

        # Verificar se a tabela existe, se não, criar
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                endereco TEXT,
                peso REAL,
                altura REAL,
                imc REAL
            )
        ''')

        # Inserir dados na tabela
        cursor.execute("INSERT INTO pacientes (nome, endereco, peso, altura, imc) VALUES (?, ?, ?, ?, ?)",
                       (nome_entry.get(), endereco_entry.get(), peso, altura, imc))

        conn.commit()
        conn.close()

        # Atualizar a lista de pacientes
        atualizar_lista_pacientes()
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de que os valores de peso e altura sejam numéricos.")

# Função limpar campos
def limpar_campos():
    nome_entry.delete(0, 'end')
    endereco_entry.delete(0, 'end')
    altura_entry.delete(0, 'end')
    peso_entry.delete(0, 'end')
    resultado_label.config(text="IMC:")

# Função para aplicativo
def sair():
    janela.quit()

# Função para atualizar a lista de pacientes
def atualizar_lista_pacientes():
    # Limpar a lista de pacientes
    lista_pacientes.delete(0, 'end')

    # Conectar ao banco de dados SQLite e obter dados da tabela
    conn = sqlite3.connect('dados_pacientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM pacientes")
    pacientes = cursor.fetchall()
    conn.close()

    # Adicionar pacientes à lista
    for paciente in pacientes:
        lista_pacientes.insert('end', paciente[1])

# Função para exibir os dados do paciente selecionado
def exibir_dados_paciente(event):
    # Obter o índice do paciente selecionado na lista
    selected_index = lista_pacientes.curselection()

    if selected_index:
        # Conectar ao banco de dados SQLite e obter detalhes do paciente
        conn = sqlite3.connect('dados_pacientes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome, endereco, peso, altura, imc FROM pacientes WHERE id=?", (selected_index[0] + 1,))
        paciente = cursor.fetchone()
        conn.close()

        # Exibir os detalhes do paciente no rótulo
        dados_paciente_label.config(text=f"Detalhes do Paciente:\nNome: {paciente[0]}\nEndereço: {paciente[1]}\nPeso: {paciente[2]} kg\nAltura: {paciente[3]} cm\nIMC: {paciente[4]:.2f}")

# Verificar se o banco de dados existe, se não, criar
db_file_path = 'dados_pacientes.db'
if not os.path.exists(db_file_path):
    conn = sqlite3.connect(db_file_path)
    conn.close()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Campos de entrada
nome_label = tk.Label(janela, text="Nome do Paciente:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

endereco_label = tk.Label(janela, text="Endereço Completo:")
endereco_label.pack()
endereco_entry = tk.Entry(janela)
endereco_entry.pack()

altura_label = tk.Label(janela, text="Altura (cm):")
altura_label.pack()
altura_entry = tk.Entry(janela)
altura_entry.pack()

peso_label = tk.Label(janela, text="Peso (kg):")
peso_label.pack()
peso_entry = tk.Entry(janela)
peso_entry.pack()

resultado_label = tk.Label(janela, text="IMC é:")
resultado_label.pack()

# Botões
calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
calcular_button.pack()

limpar_button = tk.Button(janela, text="Reiniciar", command=limpar_campos)
limpar_button.pack()

sair_button = tk.Button(janela, text="Sair", command=sair)
sair_button.pack()

# Lista de Pacientes
lista_pacientes_label = tk.Label(janela, text="Lista de Pacientes:")
lista_pacientes_label.pack()

lista_pacientes = tk.Listbox(janela)
lista_pacientes.pack()

# Rótulo para exibir detalhes do paciente selecionado
dados_paciente_label = tk.Label(janela, text="Detalhes do Paciente:")
dados_paciente_label.pack()

# Atualizar a lista de pacientes
atualizar_lista_pacientes()

# Associar a função de exibir dados do paciente ao evento de seleção na lista
lista_pacientes.bind('<<ListboxSelect>>', exibir_dados_paciente)

# Iniciar interface gráfica
janela.mainloop()
