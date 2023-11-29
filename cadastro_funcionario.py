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

def abrir_cadastro_funcionario():
    # Função para anexar o comprovante de residência
    # ----------------------------------------------
    def anexar_comprovante_residencia():
        comprovante_residencia = filedialog.askopenfilename(initialdir="/", title="Selecione o comprovante de residência", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
        comprovante_residencia_entry.insert(0, comprovante_residencia)
    # ----------------------------------------------

    # Função de cadastro de funcionários
    # ----------------------------------
    def cadastrar():
        rg = rg_entry.get()
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        data_nasc = data_nasc_entry.get()
        setor = setor_entry.get()
        senha = password_entry.get()
        num_carteira_de_trabalho = num_carteira_trabalho_entry.get()
        comprovante_de_residencia = comprovante_residencia_entry.get()

        query = "INSERT INTO funcionarios (rg, nome, cpf, data_nasc, setor, senha, num_carteira_de_trabalho, comprovante_de_residencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (rg, nome, cpf, data_nasc, setor, senha, num_carteira_de_trabalho, comprovante_de_residencia)
        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Cadastro de Funcionário", "Funcionário cadastrado com sucesso!")
        registerWindow.destroy()
        abrir_cadastro_funcionario()
    # ----------------------------------

    # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        registerWindow.destroy()
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
    registerWindow = Toplevel()
    registerWindow.title('Sistema Contábil')
    registerWindow.geometry('600x400+400+150')
    registerWindow.state('zoomed')

    gradient_width = registerWindow.winfo_screenwidth()
    gradient_height = registerWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(registerWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(registerWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(registerWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.55, relwidth=0.5, relheight=0.75, anchor=CENTER)
    # ---------------------------------------------------

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Cadastro de Funcionário", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')
    
    rg_label = Label(box, text="RG:", bg='#ffffff', font=('Arial', 12, 'bold'))
    rg_label.pack()
    rg_label.place(relx=0.1, rely=0.05, anchor='w')

    nome_label = Label(box, text="Nome:", bg='#ffffff', font=('Arial', 12, 'bold'))
    nome_label.pack()
    nome_label.place(relx=0.1, rely=0.15, anchor='w')

    cpf_label = Label(box, text="CPF:", bg='#ffffff', font=('Arial', 12, 'bold'))
    cpf_label.pack()
    cpf_label.place(relx=0.1, rely=0.25, anchor='w')

    data_nasc_label = Label(box, text="Data de Nascimento:", bg='#ffffff', font=('Arial', 12, 'bold'))
    data_nasc_label.pack()
    data_nasc_label.place(relx=0.1, rely=0.35, anchor='w')

    setor_label = Label(box, text="Setor:", bg='#ffffff', font=('Arial', 12, 'bold'))
    setor_label.pack()
    setor_label.place(relx=0.1, rely=0.45, anchor='w')

    password_label = Label(box, text="Senha:", bg='#ffffff', font=('Arial', 12, 'bold'))
    password_label.pack()
    password_label.place(relx=0.1, rely=0.55, anchor='w')

    num_carteira_trabalho_label = Label(box, text="Número da Carteira de Trabalho:", bg='#ffffff', font=('Arial', 12, 'bold'))
    num_carteira_trabalho_label.pack()
    num_carteira_trabalho_label.place(relx=0.1, rely=0.65, anchor='w')

    comprovante_residencia_label = Label(box, text="Comprovante de Residência:", bg='#ffffff', font=('Arial', 12, 'bold'))
    comprovante_residencia_label.pack()
    comprovante_residencia_label.place(relx=0.1, rely=0.75, anchor='w')
    # --------------------------------------------------

    # Entradas
    # --------------------------------------------------
    rg_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    rg_entry.pack()
    rg_entry.place(relx=0.7, rely=0.05, anchor='center')

    nome_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    nome_entry.pack()
    nome_entry.place(relx=0.7, rely=0.15, anchor='center')

    cpf_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    cpf_entry.pack()
    cpf_entry.place(relx=0.7, rely=0.25, anchor='center')

    data_nasc_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    data_nasc_entry.pack()
    data_nasc_entry.place(relx=0.7, rely=0.35, anchor='center')

    setor_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    setor_entry.pack()
    setor_entry.place(relx=0.7, rely=0.45, anchor='center')

    password_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    password_entry.pack()
    password_entry.place(relx=0.7, rely=0.55, anchor='center')

    num_carteira_trabalho_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    num_carteira_trabalho_entry.pack()
    num_carteira_trabalho_entry.place(relx=0.7, rely=0.65, anchor='center')

    comprovante_residencia_entry = Entry(box, bg='#d9d9d9', font=('Arial', 12))
    comprovante_residencia_entry.pack()
    comprovante_residencia_entry.place(relx=0.7, rely=0.75, anchor='center')
    # --------------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão para anexar o comprovante de residência
    comprovante_residencia_button = Button(box, text="Anexar comprovante", font=('Arial', 12), command=anexar_comprovante_residencia)
    comprovante_residencia_button.pack()
    comprovante_residencia_button.place(relx=0.7, rely=0.8, anchor='center')

    # Botão de cadastro de funcionários
    cadastrar_button = Button(box, text="Cadastrar", font=('Arial', 18, 'bold'), command=cadastrar)
    cadastrar_button.pack()
    cadastrar_button.place(relx=0.5, rely=0.95, anchor=CENTER)

    # Botão para voltar para a página inicial
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18, 'bold'), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')
    # --------------------------------------------------

    registerWindow.protocol("WM_DELETE_WINDOW", registerWindow.destroy)

    registerWindow.mainloop()

    cursor.close()
    connection.close()