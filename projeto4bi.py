from tkinter import *
import customtkinter as ctk

# ! Projeto de PEOO - Anna Clara, Enzo Riquelme, Hellen Vitória e Kauã Angelo

# * config. da aparência
ctk.set_appearance_mode('light')

#* janela principal
app = ctk.CTk()
app.title('Goodreads')
app.geometry('500x500')
app.resizable(False, False)

# * janela do login
def fazer_login():
	app.destroy()
	janelalogin = ctk.CTk()
	janelalogin.title('Log-in')
	janelalogin.geometry('500x500')
	janelalogin.resizable(False, False)

	#? funcionalidade a definir se será utilizada
	# ? label_nome = tk.Label(janela2, text = "Nome")
	# ? label_nome.grid(row = 0, column = 0 )
	# ? botao_voltar = tk.Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
	# ? botao_volta.grid(row = 1, column = 0)

	# * labels e entry´s
	user = ctk.CTkLabel(janelalogin, text='Usuário', font=("Courier", 16, 'bold'))
	user.pack(pady = (200, 5))
	user_entry = ctk.CTkEntry(janelalogin, placeholder_text="Digite seu nome de usuário aqui", width = 202)
	user_entry.pack()
	password = ctk.CTkLabel(janelalogin, text='Senha', font=("Courier", 16, 'bold'))
	password.pack() 
	password_entry = ctk.CTkEntry(janelalogin, placeholder_text="Digite a senha da sua conta aqui", width = 202, show = '*')
	password_entry.pack()

	#! IREI TESTAR A BIBLIOTECA PANDAS
	# resultado_login = ctk.CTkLabel(janelalogin, text = '')
	# resultado_login.pack(pady = (1, 5))

	# * funcionalidades da tela de log-in
	def validar_login():
		usuario = user_entry.get()
		senha = password_entry.get()

		#! IREI TESTAR A BIBLIOTECA PANDAS
		# #verificar:
		# if usuario == 'clraweb' and senha == '08booklover':
		# 	resultado_login.configure(text = 'Deu certo! Aguarde', text_color = 'green', font = ('Courier', 12))
		# elif usuario == '' or senha == '':
		# 	resultado_login.configure(text = 'Preencha os campos', text_color = 'blue', font = ('Courier', 12))
		# else:
		# 	resultado_login.configure(text = 'Eita, algo deu errado!', text_color = 'red', font = ('Courier', 12))

	# * botão para validar o log-in
	validar = ctk.CTkButton(janelalogin, text='Validar', command= validar_login, fg_color='black', hover_color='gray')
	validar.pack(pady=(1, 5))

	janelalogin.mainloop()

# * janela do cadastro
def fazer_cadastro():
	app.destroy()
	janelacadast = ctk.CTk()
	janelacadast.title('Cadastro')
	janelacadast.geometry('500x500')
	janelacadast.resizable(False, False)
	# ? janelacadast.after(1, lambda:janelacadast.state('zoomed')) - pra abrir tela maximizada 

	# * labels e entries
	nome = ctk.CTkLabel(janelacadast, text='Nome:', font=("Courier", 16, 'bold'))
	nome.pack(pady = (140, 2))
	nome_entry = ctk.CTkEntry(janelacadast, placeholder_text= '  Como podemos te chamar?', width = 180)
	nome_entry.pack()
	user_cadastro = ctk.CTkLabel(janelacadast, text='Usuário:', font=("Courier", 16, 'bold'))
	user_cadastro.pack()
	usercad_entry= ctk.CTkEntry(janelacadast, placeholder_text= ' Escolha um nome de usuário', width = 185)
	usercad_entry.pack()
	passw_cadastro = ctk.CTkLabel(janelacadast, text='Senha:', font=("Courier", 16, 'bold'))
	passw_cadastro.pack()
	passwc_entry = ctk.CTkEntry(janelacadast, placeholder_text= ' Escolha sua senha!', width = 130)
	passwc_entry.pack()

	'''
	# todo: INSERÇÃO DA BIBLIOTECA PANDAS PARA CRIAR CONTA


	criação = ctk.CTkButton(janelacadast, text = 'Criar conta', command=criar_conta, fg_color ='black', hover_color = 'gray')
	criação.pack(pady = (15, 5))

	'''

	janelacadast.mainloop()


# * TELA INICIAL - LOGIN/CADASTRO
inicio = ctk.CTkLabel(app, text='Bem vindo ao Goodreads!', font=("Courier", 20, 'bold'))
subt = ctk.CTkLabel(app, text='Já tem uma conta?', font=("Courier", 18, 'bold'))

inicio.pack(pady = (200, 0), anchor = 'center')  
subt.pack(anchor = 'center')

# * botões de login/cadastro
botao_login = ctk.CTkButton(app, text='Fazer login', font= ('Lexend', 12), command= fazer_login, fg_color='black', hover_color='gray')
botao_login.pack(pady=(0, 10), anchor='center')

botao_cadastrar = ctk.CTkButton(app, text='Criar conta', font= ('Lexend', 12), command= fazer_cadastro, fg_color='black', hover_color='gray')
botao_cadastrar.pack(pady=(0, 50), anchor='center')

app.mainloop()
