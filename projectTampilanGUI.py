import tkinter 

Python_GUI = tkinter.Tk()

def btnCLick():
    btnClick = tkinter.Label(Python_GUI, text="Hehe kami keren")
    btnClick.pack()
    
def btn_remove():
    btnCancel.place_forget()

nama = tkinter.Label(Python_GUI, text="Halo nama saya Sandi, Nabil, Mifta, dan Fajar" )
kelas = tkinter.Label(Python_GUI, text="Kami kelas XI TKJ 2" )
desciption = tkinter.Label(Python_GUI, text="Kami sedang belajar python berbasis GUI" )

btnOke = tkinter.Button(Python_GUI, text="Oke", width=10, command=btnCLick)
btnCancel = tkinter.Button(Python_GUI, text="Cancel", width=10, background="green", command=btn_remove)

nama.pack()
kelas.pack()
desciption.pack()
btnOke.pack()
btnCancel.pack()


Python_GUI.mainloop()