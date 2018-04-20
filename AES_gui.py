import tkinter as tk
from tkinter import *
from tkinter import ttk
from Encriptador import *
import sys
from tkinter import messagebox

root = tk.Tk()

root.title("AES")

width = 600
height = 460
x_offset = 50
y_offset = 100

root.geometry("%dx%d+%d+%d" % (width, height,x_offset,y_offset))


def confirm(tam_bits,clave):
    if(tam_bits == "16 bytes" and len(clave) == 16):
        return True
    elif(tam_bits == "24 bytes" and len(clave) == 24):
        return True
    elif(tam_bits == "32 bytes" and len(clave) == 32):
        return True
    return False


def encrypt():
    inputValue = textBox1.get("1.0","end-1c")
    key = textBox3.get("1.0","end-1c")
    Encrypter = Encriptador(key)
    if(confirm(combo.get(),key)):
        text_encrypted = Encrypter.Run(inputValue, CheckVar2.get())
        print(text_encrypted)
        textBox2.config(state=NORMAL)
        textBox2.delete("1.0",END)
        textBox2.insert(END,text_encrypted)
        textBox2.config(state=DISABLED)
        print(CheckVar1.get())
        if(CheckVar1.get()):
            file = open('encrypted_text.txt','w',encoding="utf-8")
            file.write(text_encrypted)
            file.close()
    else:
        result = messagebox.showerror("Confirm", "Clave erronea", icon='warning')




frame = tk.Frame(root)
frame.pack(fill='both',expand='yes')

#CheckButton
CheckVar1 = IntVar()
save_text = tk.Checkbutton(frame,text="Save text",variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
save_text.place(x=10,y=380)
'CheckVar1.get()'

#CheckButton
CheckVar2= IntVar()
save_text2 = tk.Checkbutton(frame,text="Decrypt",variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
save_text2.place(x=200,y=380)


#Encryptcion Button
encryptionButton = tk.Button(frame,height=1, width=10,text="Do job",command = encrypt)
encryptionButton.place(x=400,y=410)

#TextBox1
textBox1 = tk.Text(frame,height = 18, width=32)
textBox1.place(x=30,y=100)

#TextBox2
textBox2 = tk.Text(frame,height = 18, width=32)
#textBox2.insert(END,"Texto ya encriptado")
textBox2.place(x=320,y=100)


#TextBox3
textBox3 = tk.Text(frame,height = 1, width=55)
textBox3.place(x=140,y=30)

#ComboBox
combo = ttk.Combobox(frame,width=10)
combo.place(x=30,y=30)
combo["values"] = ["16 bytes","24 bytes","32 bytes"]
'combo.get()'

root.mainloop()
