from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
import cadastro_funcionario
import visualizar_funcionarios
import docfuncionarios
import cadastro_cliente
import visualizar_clientes
import doccliente

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

def abrir_indexFuncionario():
    # Função para abrir a página de cadastro de clientes
    # ---------------------------------------------------
    def abrir_cadastro_cliente():
        cadastro_cliente.abrir_cadastro_cliente()
    # ---------------------------------------------------

    # Função para abrir a página de visualização de clientes
    # -------------------------------------------------------
    def abrir_visualizar_clientes():
        visualizar_clientes.abrir_visualizar_clientes()
    # -------------------------------------------------------

    # Função para abrir a página de documentos de clientes
    # -----------------------------------------------------
    def abrir_doc_clientes():
        doccliente.abrir_doc_clientes()
    # -----------------------------------------------------

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

    # Configuração da Pagina Inicial
    # -------------------------------
    indexAdminWindow = Tk()
    indexAdminWindow.title('Sistema Contábil')
    indexAdminWindow.geometry('600x400+400+150')
    indexAdminWindow.state('zoomed')

    gradient_width = indexAdminWindow.winfo_screenwidth()
    gradient_height = indexAdminWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(indexAdminWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(indexAdminWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box2 = Frame(indexAdminWindow, bg='#ffffff', bd=5)
    box2.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.4, anchor=CENTER)
    # -------------------------------

    # Labels
    # --------------------------------------------------
    welcome_label = Label(cabecalho, text="Bem vindo!", bg='#ffffff', font=('Arial', 40, 'bold'))
    welcome_label.pack()
    welcome_label.place(relx=0.01, rely=0.5, anchor='w')

    box2_label = Label(box2, text="Clientes", bg='#ffffff', font=('Arial', 20, 'bold'))
    box2_label.pack()
    box2_label.place(relx=0.5, rely=0.02, anchor='n')
    # --------------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão de cadastro de clientes
    cadastro_cliente_button = Button(box2, text="Cadastrar", bg='#ffffff', font=('Arial', 12, 'bold'), command=abrir_cadastro_cliente)
    cadastro_cliente_button.pack()
    cadastro_cliente_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Botão de visualização de clientes
    visualizar_clientes_button = Button(box2, text="Visualizar", bg='#ffffff', font=('Arial', 12, 'bold'), command=abrir_visualizar_clientes)
    visualizar_clientes_button.pack()
    visualizar_clientes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    # Botão de documentos de clientes
    documentos_clientes_button = Button(box2, text="Documentos", bg='#ffffff', font=('Arial', 12, 'bold'), command=abrir_doc_clientes)
    documentos_clientes_button.pack()
    documentos_clientes_button.place(relx=0.5, rely=0.8, anchor=CENTER)
    # --------------------------------------------------

    indexAdminWindow.protocol("WM_DELETE_WINDOW", indexAdminWindow.destroy)

    indexAdminWindow.mainloop()

    cursor.close()
    connection.close()