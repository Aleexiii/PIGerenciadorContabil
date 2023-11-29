from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
import adddoccliente


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

def abrir_doc_clientes():
     # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        docClientWindow.destroy()
    # ----------------------------------------

    # Função para adicionar um novo documento
    # ---------------------------------------
    def addDoc():
        adddoccliente.abrir_add_doc()

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

    # Configuração da Página de Documentos dos Clientes
    # -------------------------------
    docClientWindow = Toplevel()
    docClientWindow.title('Sistema Contábil')
    docClientWindow.geometry('600x400+400+150')
    docClientWindow.state('zoomed')

    gradient_width = docClientWindow.winfo_screenwidth()
    gradient_height = docClientWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(docClientWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(docClientWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(docClientWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.6, anchor=CENTER)
    # -------------------------------

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Documentos dos Clientes", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')
    # --------------------------------------------------

    # Listbox
    # -----------------------------------------------
    # Listbox para mostrar os documentos dos Clientes
    listbox = Listbox(box, bg='#ffffff', font=('Arial', 18))
    listbox.pack(side=LEFT, fill=BOTH)
    listbox.place(relx=0.02, rely=0.5, relwidth=0.7, relheight=1, anchor='w')
    
    # Scrollbar para o listbox
    scrollbar = Scrollbar(box)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Preenchendo o listbox com os nomes dos Clientes
    cursor.execute('SELECT nome_cliente, tipo FROM documentos')
    nome = cursor.fetchall()
    for documento in nome:
        listbox.insert(END, documento)
    # -----------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão de voltar
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18, 'bold'), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')

    # Botão para adicionar um novo documento
    addDoc_button = Button(box, text="Adicionar", bg='#ffffff', font=('Arial', 18), command=addDoc)
    addDoc_button.pack()
    addDoc_button.place(relx=0.75, rely=0.5, anchor='w')
    # --------------------------------------------------

    docClientWindow.mainloop()

    cursor.close()
    connection.close()
 