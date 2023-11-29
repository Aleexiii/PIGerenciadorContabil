from tkinter import *
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

# Conexão com o banco de dados
# ----------------------------
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_juriscon'
)
cursor = connection.cursor()
# ----------------------------

def abrir_cadastro_cliente():
    # Função de cadastro de funcionários
    # ----------------------------------
    def cadastrar():
        cnpj = cnpj_entry.get()
        func_atendente = func_atendente_entry.get()
        nome = nome_entry.get()
        nome_fantasia = nome_fantasia_entry.get()
        cpf_responsavel= cpf_responsavel_entry.get()
        endereco = endereco_entry.get()
        atividade = atividade_entry.get()

        query = "INSERT INTO clientes (cnpj, funcionário_atendente, nome, nome_fantasia, cpf_responsavel, endereço, atividade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (cnpj, func_atendente, nome, nome_fantasia, cpf_responsavel, endereco, atividade)
        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Cadastro de Funcionário", "Funcionário cadastrado com sucesso!")
        registerClientWindow.destroy()
        abrir_cadastro_cliente()
    # ----------------------------------

    # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        registerClientWindow.destroy()
    # ----------------------------------------

    # Criação do gradiente do background
    # ----------------------------------
    def create_gradient(width, height, start_color, end_color):
        image = Image.new('RGB', (width, height))
        for y in range(height):
            r = start_color[0] + (end_color[0] - start_color[0]) * y / height
            g = start_color[1] + (end_color[1] - start_color[1]) * y / height
            b = start_color[2] + (end_color[2] - start_color[2]) * y / height
            for x in range(width):
                image.putpixel((x, y), (int(r), int(g), int(b)))
        return ImageTk.PhotoImage(image)
    # ----------------------------------

    # Configuração da Pagina de Cadastro de Funcionários
    # ---------------------------------------------------
    registerClientWindow = Toplevel()
    registerClientWindow.title('Sistema Contábil')
    registerClientWindow.geometry('600x400+400+150')
    registerClientWindow.state('zoomed')
    # registerClientWindow.iconbitmap('imagens/logo_juriscon.ico')

    gradient_width = registerClientWindow.winfo_screenwidth()
    gradient_height = registerClientWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(registerClientWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(registerClientWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(registerClientWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.55, relwidth=0.5, relheight=0.75, anchor=CENTER)
    # ---------------------------------------------------

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Cadastro de Clientes", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')
    
    cnpj_label = Label(box, text="CNPJ:", bg='#ffffff', font=('Arial', 12, 'bold'))
    cnpj_label.pack()
    cnpj_label.place(relx=0.1, rely=0.05, anchor='w')

    func_atendente_label = Label(box, text="Funcionário Atendente:", bg='#ffffff', font=('Arial', 12, 'bold'))
    func_atendente_label.pack()
    func_atendente_label.place(relx=0.1, rely=0.15, anchor='w')

    nome_label = Label(box, text="Nome:", bg='#ffffff', font=('Arial', 12, 'bold'))
    nome_label.pack()
    nome_label.place(relx=0.1, rely=0.25, anchor='w')

    nome_fantasia_label = Label(box, text="Nome Fantasia:", bg='#ffffff', font=('Arial', 12, 'bold'))
    nome_fantasia_label.pack()
    nome_fantasia_label.place(relx=0.1, rely=0.35, anchor='w')

    cpf_responsavel_label = Label(box, text="CPF do Responsável:", bg='#ffffff', font=('Arial', 12, 'bold'))
    cpf_responsavel_label.pack()
    cpf_responsavel_label.place(relx=0.1, rely=0.45, anchor='w')

    endereco_label = Label(box, text="Endereço:", bg='#ffffff', font=('Arial', 12, 'bold'))
    endereco_label.pack()
    endereco_label.place(relx=0.1, rely=0.55, anchor='w')

    atividade_label = Label(box, text="Atividade:", bg='#ffffff', font=('Arial', 12, 'bold'))
    atividade_label.pack()
    atividade_label.place(relx=0.1, rely=0.65, anchor='w')
    # --------------------------------------------------

    # Entradas
    # --------------------------------------------------
    cnpj_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    cnpj_entry.pack()
    cnpj_entry.place(relx=0.7, rely=0.05, anchor='center')

    func_atendente_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    func_atendente_entry.pack()
    func_atendente_entry.place(relx=0.7, rely=0.15, anchor='center')

    nome_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    nome_entry.pack()
    nome_entry.place(relx=0.7, rely=0.25, anchor='center')

    nome_fantasia_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    nome_fantasia_entry.pack()
    nome_fantasia_entry.place(relx=0.7, rely=0.35, anchor='center')

    cpf_responsavel_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    cpf_responsavel_entry.pack()
    cpf_responsavel_entry.place(relx=0.7, rely=0.45, anchor='center')

    endereco_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    endereco_entry.pack()
    endereco_entry.place(relx=0.7, rely=0.55, anchor='center')

    atividade_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    atividade_entry.pack()
    atividade_entry.place(relx=0.7, rely=0.65, anchor='center')
    # --------------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão de cadastro de clientes
    cadastrar_button = Button(box, text="Cadastrar", font=('Arial', 18, 'bold'), command=cadastrar)
    cadastrar_button.pack()
    cadastrar_button.place(relx=0.5, rely=0.95, anchor=CENTER)

    # Botão para voltar para a página inicial
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18, 'bold'), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')
    # --------------------------------------------------

    registerClientWindow.protocol("WM_DELETE_WINDOW", registerClientWindow.destroy)

    registerClientWindow.mainloop()

    cursor.close()
    connection.close()