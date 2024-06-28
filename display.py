
import os
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, LEFT
from PIL import Image, ImageTk


PATH_IMG = f'{os.getcwd()}/images/'
EXT_FILE = ['jpg', 'jpeg', 'png', 'raw']


def verificateur_file(file):
    return os.path.exists(file)


def recup_code_produit(recup):
    return recup.get()


def resize_pic(image):
    return image.resize((500, 500))


def display_func():
    code = recup_code_produit(code_produit)
    for i in EXT_FILE:
        path_img = f"{PATH_IMG}{code}.{i}"

        if verificateur_file(path_img):
            image = Image.open(path_img)
            resize_img = resize_pic(image)
            img = ImageTk.PhotoImage(resize_img)
            disp_img.config(image=img)
            disp_img.image = img

    else:
        msg = f"L'image de l'article N° {code} est non disponible ou code produit erroné"
        messagebox.showerror(message=msg)


ws = Tk()
ws.title("AFFICHEUR D'IMAGE")
ws.geometry('700x700')
ws.config(bg='#4a7a8c')

frame = Frame(ws)
frame.pack()

Label(
    frame,
    text='CODE PRODUIT'
    ).pack(side=LEFT)

code_produit = Entry(frame, width=10)
code_produit.pack(side=LEFT)

resize_btn = Button(
    frame,
    text='Validé',
    command=display_func
)
resize_btn.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)


ws.mainloop()
