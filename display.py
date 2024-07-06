import os
import sys
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, LEFT
from PIL import Image, ImageTk


PATH_IMG = f'{os.getcwd()}/images/'
LIST_IMG = os.listdir(PATH_IMG)
EXT_FILE = ['jpg', 'jpeg', 'png', 'raw']


# Configuration de Pyinstaller
def resource_path(relative_path):
    # get absolute path to resource
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Configurtion du Splash 
if getattr(sys, 'frozen', False):
    import pyi_splash


# Verifier si le ficher existe ou pas
def verificateur_file(file):
    return os.path.exists(file)


def recup_code_produit(recup):
    return recup.get()


def resize_pic(image):
    return image.resize((500, 500))


def display_func(event):
    code = recup_code_produit(code_produit)
    list_nom_sans_ext = [os.path.splitext(i)[0] for i in LIST_IMG]
    if code in list_nom_sans_ext:
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
ws.title("ONLY SOFT")
ws.geometry('700x700')
# Coloré le font d'ecran
ws.config(bg='#4a7a8c')


frame = Frame(ws)
frame.pack()

Label(
    frame,
    text='CODE PRODUIT:'
    ).pack(side=LEFT)

code_produit = Entry(frame, width=10)
code_produit.pack(side=LEFT)

boutton_validé = Button(
    frame,
    text='Validé',
    command=display_func
)

# Lier "Entrer" avec la boutton "Valider"
ws.bind("<Return>", display_func)

boutton_validé.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)

# Fermeture du spalsh avent le lancement de l'application
if getattr(sys, 'frozen', False):
    pyi_splash.close()

ws.mainloop()
