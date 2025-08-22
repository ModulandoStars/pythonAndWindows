import tkinter as tk
import os



root = tk.Tk()
software_title = "A janela gamer"

root.geometry('640x510')
root.resizable(False, False)

IntroductionText = tk.StringVar()
IntroductionText.set("olá, bem vindo ao seletor de pastas aleatórias!")

#selectedPath = input("sexo")


#folderDirList = []

#   def checkFolders(directory):
#        print(directory + " foi o diretório")
#       folderCheck = os.scandir(directory)
#       for entry in folderCheck:
#          if entry.is_dir():
#                folderDirList.append(entry.name)


textList = []
variableList = tk.Variable(value=textList)



text = tk.Label(
    root,
    anchor=tk.CENTER,
    height=2,
    textvariable=IntroductionText
)
text.pack(pady=15)

dirAskBox = tk.Text(
    root,
    height=5,
    width=10,
    font=("Segoe UI", 12)
)
dirAskBox.insert(tk.END, "C:\\Windows")
dirAskBox.pack()
textBox = dirAskBox.get("1.0", tk.END)

def inmendText(text):
    textBox = dirAskBox.get("0.0", tk.END)
    variableList = tk.Variable(value=textList)
    textList.append(text)
    print(textList)
    root.update()

doFunction = tk.Button(
    root,
    text="hello",
    command= lambda: inmendText(textBox)
)
doFunction.pack(pady=5)




folderList = tk.Listbox(
    root,
    bg="white",
    width=50,
    listvariable=variableList,
    font=("Segoe UI", 12)
)
folderList.pack()




root.title(software_title)
root.configure(background="dark grey")

root.mainloop()