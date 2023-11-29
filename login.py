from tkinter import *
import mysql.connector
import PIL.Image
from PIL import Image, ImageTk
import indexAdmin
import indexFuncionario

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

# Verificação de credenciais do banco de dados
def login():
    user = user_entry.get()
    password = password_entry.get()

    if len(user) == 4:
        cursor.execute("SELECT idAdmin, senha FROM sisadmin WHERE idAdmin = %s AND senha = %s", (user, password))
        if cursor.fetchone() is not None:
            loginWindow.destroy()
            indexAdmin.abrir_indexAdmin()
        else:
            login_status_label['text'] = "Usuário ou senha incorretos!"
    elif len(user) == 11:
        cursor.execute("SELECT cpf, senha FROM funcionarios WHERE cpf = %s AND senha = %s", (user, password))
        if cursor.fetchone() is not None:
            loginWindow.destroy()
            indexFuncionario.abrir_indexFuncionario()
        else:
            login_status_label['text'] = "Usuário ou senha incorretos!"

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


# Configuração da Pagina de Login
# -------------------------------
loginWindow = Tk()
loginWindow.title('Login Sistema Contábil')
loginWindow.geometry('600x400+400+150')
loginWindow.state('zoomed')

gradient_width = loginWindow.winfo_screenwidth()
gradient_height = loginWindow.winfo_screenheight()
start_color = (0, 0, 0)
end_color = (102, 0, 0)
gradient_image = create_gradient(gradient_width, gradient_height, start_color, end_color)

background_label = Label(loginWindow, image=gradient_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(loginWindow, bg='#D9D9D9', bd=5)
frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor=CENTER)
# -------------------------------

# Labels
# --------------------------------------------------
#logo_label = Label(frame, image=photo, bg='#D9D9D9')
user_label = Label(frame, text="Usuário:", bg='#D9D9D9', font=('Arial', 18, 'bold'))
user_label.pack()
user_label.place(relx=0.4, rely=0.4, anchor=CENTER)

password_label = Label(frame, text="Senha:", bg='#D9D9D9', font=('Arial', 18, 'bold'))
password_label.pack()
password_label.place(relx=0.4, rely=0.5, anchor=CENTER)

login_status_label = Label(frame, text="", bg='#D9D9D9', font=('Arial', 16, 'bold'))
login_status_label.pack()
login_status_label.place(relx=0.5, rely=0.3, anchor=CENTER)
# --------------------------------------------------

# Entradas
# --------------------------------------------
user_entry = Entry(frame, width='20', font=('Arial', 13))
user_entry.pack()
user_entry.place(relx=0.55, rely=0.4, anchor=CENTER)

password_entry = Entry(frame, width='20', font=('Arial', 13), show="*")
password_entry.pack()
password_entry.place(relx=0.55, rely=0.5, anchor=CENTER)
# --------------------------------------------

# Botão de Login
# --------------------------------------------------------------
login_button = Button(frame, text="Login", font=('Arial', 18, 'bold'), command=login)
login_button.pack()
login_button.place(relx=0.5, rely=0.7, anchor=CENTER)
# --------------------------------------------------------------

loginWindow.protocol("WM_DELETE_WINDOW", loginWindow.destroy)

loginWindow.mainloop()

cursor.close()
connection.close()