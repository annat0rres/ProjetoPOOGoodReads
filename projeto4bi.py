#testes - última atualização: 21/01/2025 - Anna Clara

from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk


#config. da aparência
ctk.set_appearance_mode('light')

#janela principal
app = ctk.CTk()
app.title('Goodreads')
app.geometry('500x500')
app.resizable(False, False)

#janela do login
def fazer_login():
	app.destroy()
	janela2 = ctk.CTk()
	janela2.title('Log-in')
	janela2.geometry('500x500')
	janela2.resizable(False, False)
	# label_nome = tk.Label(janela2, text = "Nome")
	# label_nome.grid(row = 0, column = 0 )
	# botao_voltar = tk.Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
	# botao_volta.grid(row = 1, column = 0)
	# labels da janela2:
	user = ctk.CTkLabel(janela2, text='Usuário', font=("Times New Roman", 16, 'bold'))
	user.pack(pady=(200, 5), padx=2)
	user.entry = ctk.CTkEntry(janela2, placeholder_text="Digite seu nome de usuário aqui", width = 202)
	user.entry.pack()
	password = ctk.CTkLabel(janela2, text='Senha', font=("Times New Roman", 16, 'bold'))
	password.pack(pady=(5, 5), padx=2)
	#entry - usuário 
	password.entry = ctk.CTkEntry(janela2, placeholder_text="Digite a senha da sua conta aqui", width = 202)
	password.entry.pack()
	janela2.mainloop()


# botao = tk.Button(janela, text = 'Ir para nova janela', command = abrir_janela)
# botao.grid(row = 0, column = 0)

#label
logo = Image.open("logo.png")  # Usando PIL para abrir a imagem
logo = logo.resize((250, 250))  # Ajuste o tamanho da imagem, se necessário
logo_img = ImageTk.PhotoImage(logo)  # Convertendo para o formato necessário pelo tkinter/CTk
logo_label = ctk.CTkLabel(app, image=logo_img, text='')  # Passando a imagem convertida
inicio = ctk.CTkLabel(app, text='Bem vindo ao Goodreads!', font=("Times New Roman", 20, 'bold'))
subt = ctk.CTkLabel(app, text='Já tem uma conta?', font=("Times New Roman", 16, 'bold'))

#oorganizando os labels
logo_label.pack(pady = 50, padx = 1)
inicio.pack(padx=2)  
subt.pack(padx=2)

#buttons
botao_login = ctk.CTkButton(app, text='Fazer login', command= fazer_login, fg_color='blue', hover_color='black')
botao_login.pack(pady=(0, 10), padx=2)

botao_cadastrar = ctk.CTkButton(app, text='Criar conta', command=lambda: print("Iniciando cadastro"), fg_color='blue', hover_color='black')
botao_cadastrar.pack(pady=(0, 20), padx=2)

app.mainloop()
