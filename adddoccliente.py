from tkinter import *
from tkinter import ttk
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

def abrir_add_doc():
    # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        addDocWindow.destroy()
    # ----------------------------------------

    # Função para anexar um documento
    # ---------------------------------
    def anexar_documento():
        documento = filedialog.askopenfilename(initialdir="/", title="Selecione o documento", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
        documento_entry.insert(0, documento)
    # ---------------------------------

    # Função para adicionar um novo documento
    # ---------------------------------
    def adicionar_documento():
        nome_cliente = select.get()
        tipo_documento = tipo_doc_entry.get()
        documento = documento_entry.get()

        if documento:
            with open(documento, 'rb') as file:
                info_documento = file.read()
        nome_documento = documento.split('/')[-1]

        query = "INSERT INTO documentos (nome_cliente, tipo, docname, docdata) VALUES (%s, %s, %s, %s)"
        values = (nome_cliente, tipo_documento, nome_documento, info_documento)
        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Adicionar Documento", "Documento adicionado com sucesso!")
        addDocWindow.destroy()
        abrir_add_doc()
    # ---------------------------------

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

    # Configuração da Página de Adicionar Documentos
    # ----------------------------------------------
    addDocWindow = Toplevel()
    addDocWindow.title('Sistema Contábil')
    addDocWindow.geometry('600x400+400+150')
    addDocWindow.state('zoomed')

    gradient_width = addDocWindow.winfo_screenwidth()
    gradient_height = addDocWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(addDocWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(addDocWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(addDocWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.6, anchor=CENTER)

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Adicionar Documento", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')

    cliente_label = Label(box, text="Cliente:", bg='#ffffff', font=('Arial', 14, 'bold'))
    cliente_label.pack()
    cliente_label.place(relx=0.1, rely=0.1, anchor='w')

    tipo_documento_label = Label(box, text="Tipo de Documento:", bg='#ffffff', font=('Arial', 14, 'bold'))
    tipo_documento_label.pack()
    tipo_documento_label.place(relx=0.1, rely=0.3, anchor='w')

    documento_label = Label(box, text="Documento:", bg='#ffffff', font=('Arial', 14, 'bold'))
    documento_label.pack()
    documento_label.place(relx=0.1, rely=0.5, anchor='w')
    # --------------------------------------------------

    # Entradas
    # --------------------------------------------------
    # Entrada para o nome do cliente
    select = ttk.Combobox(box, width=20, font=('Arial', 13))
    cursor.execute("SELECT nome FROM clientes")
    nome_do_cliente = cursor.fetchall()
    for nomes in nome_do_cliente:
        select.insert(END, nomes)
    select.pack()
    select.place(relx=0.6, rely=0.1, anchor=CENTER)

    # Entrada para o tipo de documento
    tipo_doc_entry = Entry(box, width=20, font=('Arial', 13))
    tipo_doc_entry.pack()
    tipo_doc_entry.place(relx=0.6, rely=0.3, anchor=CENTER)

    # Entrada para o documento
    documento_entry = Entry(box, width=20, font=('Arial', 13))
    documento_entry.pack()
    documento_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
    # --------------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão de voltar
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')

    # Botão para anexar o documento
    anexar_button = Button(box, text="Anexar Documento", bg='#ffffff', font=('Arial', 12,), command=anexar_documento)
    anexar_button.pack()
    anexar_button.place(relx=0.6, rely=0.6, anchor=CENTER)

    # Botão para adicionar um novo documento
    adicionar_button = Button(box, text="Adicionar Documento", bg='#ffffff', font=('Arial', 16, 'bold'), command=adicionar_documento)
    adicionar_button.pack()
    adicionar_button.place(relx=0.5, rely=0.8, anchor=CENTER)
    # --------------------------------------------------

    addDocWindow.mainloop()

    cursor.close()
    connection.close()