import tkinter as tk

root = tk.Tk()
software_title = "A janela gamer"

def HelloButton():
    print("buceta")

# ----------Botão-----------

button = tk.Button(root,
        text="oiaaaaaaaaaaaa",
        height=1,
        width=1,
        command=HelloButton
)

button.pack(
    ipadx=1,
    ipady=1,
)
# --------------------------

listaboa = ('pica', 'buceta', 'cu', 'boca')

listBoxConvert = tk.Variable(value=listaboa)

# ---------Lista------------
lista = tk.Listbox(
    root,
    listvariable=listBoxConvert,
    height=6
)

lista.pack(ipadx=10, ipady=15, fill=tk.BOTH)
# --------------------------

root.geometry('640x510')
root.resizable(False, False)

root.title(software_title)
root.configure(background="gray")

root.mainloop()