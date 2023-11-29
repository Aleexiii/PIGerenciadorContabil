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

def abrir_visualizar_funcionarios():
    # Função para deletar funcionários
    # --------------------------------
    def deletar_funcionario():
        nome_funcionario = listbox.get(ANCHOR)

        # Confirmação de exclusão
        confirmacao = messagebox.askquestion("Confirmação", "Tem certeza que deseja deletar o funcionário selecionado?")
        if confirmacao == 'no':
            return

        # Deletando o funcionário selecionado
        cursor.execute("DELETE FROM funcionarios WHERE nome = %s", (nome_funcionario,))
        connection.commit()

        # Atualizando a listbox
        listbox.delete(ANCHOR)
        messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
    # --------------------------------

    # Função para voltar para a página inicial
    # ----------------------------------------
    def voltar():
        viewWindow.destroy()
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

    # Configuração da Página de Visualização de Funcionários
    # -------------------------------
    viewWindow = Toplevel()
    viewWindow.title('Sistema Contábil')
    viewWindow.geometry('600x400+400+150')
    viewWindow.state('zoomed')
    # viewWindow.iconbitmap('imagens/logo_juriscon.ico')

    gradient_width = viewWindow.winfo_screenwidth()
    gradient_height = viewWindow.winfo_screenheight()
    start_color = (106, 106, 106)
    end_color = (237, 237, 237)
    gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

    background_label = Label(viewWindow, image=gradient_image)
    background_label.place(relwidth=1, relheight=1)

    cabecalho = Frame(viewWindow, bg='#ffffff', bd=5)
    cabecalho.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor=CENTER)

    box = Frame(viewWindow, bg='#ffffff', bd=5)
    box.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.6, anchor=CENTER)
    # -------------------------------

    # Labels
    # --------------------------------------------------
    cabecalho_label = Label(cabecalho, text="Visualizar Funcionários", bg='#ffffff', font=('Arial', 30, 'bold'))
    cabecalho_label.pack()
    cabecalho_label.place(relx=0.01, rely=0.5, anchor='w')
    # --------------------------------------------------

    # Listbox
    # -----------------------------------------------
    # Listbox para mostrar os nomes dos funcionários
    listbox = Listbox(box, bg='#ffffff', font=('Arial', 18))
    listbox.pack(fill=BOTH, expand=YES)
    listbox.place(relx=0.02, rely=0.5, relwidth=0.7, relheight=1, anchor='w')

    # Scrollbar para a listbox
    scrollbar = Scrollbar(box)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)


    # Preenchendo a listbox com os nomes dos funcionários
    cursor.execute("SELECT nome FROM funcionarios")
    nomes = cursor.fetchall()
    for nome in nomes:
        listbox.insert(END, nome[0])
    # -----------------------------------------------

    # Botões
    # --------------------------------------------------
    # Botão para deletar o funcionário selecionado
    deletar_button = Button(box, text="Deletar", bg='#ffffff', font=('Arial', 18), command=deletar_funcionario)
    deletar_button.pack()
    deletar_button.place(relx=0.8, rely=0.5, anchor='w')

    # Botão para voltar para a página inicial
    voltar_button = Button(cabecalho, text="Voltar", bg='#ffffff', font=('Arial', 18, 'bold'), command=voltar)
    voltar_button.pack()
    voltar_button.place(relx=0.9, rely=0.5, anchor='e')
    # --------------------------------------------------

    viewWindow.protocol("WM_DELETE_WINDOW", viewWindow.destroy)

    viewWindow.mainloop()

    cursor.close()
    connection.close()