from tkinter import *
import mysql.connector
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

def abrir_visualizar_clientes():
    # Função para deletar Clientes
    # --------------------------------
    def deletar_cliente():
        nome_cliente = listbox.get(ANCHOR)

        # Confirmação de exclusão
        confirmacao = messagebox.askquestion("Confirmação", "Tem certeza que deseja deletar o cliente selecionado?")
        if confirmacao == 'no':
            return

        # Deletando o cliente selecionado
        cursor.execute("DELETE FROM clientes WHERE nome = %s", (nome_cliente,))
        connection.commit()

        # Atualizando a listbox
        listbox.delete(ANCHOR)
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
    # --------------------------------

    # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        viewClientWindow.destroy()
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

    # Configuração da Página de Visualização de Clientes
    # -------------------------------
    viewClientWindow = Toplevel()
    viewClientWindow.title('Sistema Contábil')
    viewClientWindow.geometry('600x400+400+150')
    viewClientWindow.state('zoomed')
    # viewClientWindow.iconbitmap('imagens/logo_juriscon.ico')

    gradient_width = viewClientWindow.winfo_screenwidth()
    gradient_height = viewClientWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(viewClientWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(viewClientWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(viewClientWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.6, anchor=CENTER)
    # -------------------------------

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Visualizar Clientes", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')
    # --------------------------------------------------

    # Listbox
    # -----------------------------------------------
    # Listbox para mostrar os nomes dos Clientes
    listbox = Listbox(box, bg='#ffffff', font=('Arial', 18))
    listbox.pack(fill=BOTH, expand=YES)
    listbox.place(relx=0.02, rely=0.5, relwidth=0.7, relheight=1, anchor='w')

    # Scrollbar para a listbox
    scrollbar = Scrollbar(box)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)


    # Preenchendo a listbox com os nomes dos clientes
    cursor.execute("SELECT nome FROM clientes")
    nomes = cursor.fetchall()
    for nome in nomes:
        listbox.insert(END, nome[0])
    # -----------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão para deletar o cliente selecionado
    deletar_button = Button(box, text="Deletar", bg='#ffffff', font=('Arial', 18), command=deletar_cliente)
    deletar_button.pack()
    deletar_button.place(relx=0.8, rely=0.5, anchor='w')

    # Botão para voltar para a página inicial
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18, 'bold'), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')
    # --------------------------------------------------

    viewClientWindow.protocol("WM_DELETE_WINDOW", viewClientWindow.destroy)

    viewClientWindow.mainloop()

    cursor.close()
    connection.close()