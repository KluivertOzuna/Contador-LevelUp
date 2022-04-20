from ast import Num
import tkinter
from xml.etree.ElementPath import get_parent_map
ventana=tkinter.Tk()
ventana.title("contador")
ventana.geometry("500x300")
#funciones
def changeColor(valor):
    if int(valor) < 0:
        contador.config(fg = "red")
    elif int(valor) == 0:
        contador.config(fg = "black")
    elif int(valor) > 0:
        contador.config(fg = "green")    
def sumar():
    valor = int(contador["text"])
    contador["text"] = f"{valor + 1 }"
    valor = int(contador["text"])
    changeColor(valor)
def restar():
    valor = int(contador ["text"]) 
    contador["text"] = f"{valor - 1}"
    valor = int(contador ["text"]) 
    changeColor(valor)  
def reiniciar():
    valor = int(contador ["text"])    
    contador["text"] = f"{valor * 0}"
    valor = int(contador["text"])
    changeColor(valor)
bsumar=tkinter.Button(ventana, text="sumar",command=sumar,bg="green", width=10,height=2 )
bsumar.place(x=40, y=200)
drestar=tkinter.Button(ventana, text="restar",command=restar, bg="red", width=10,height=2 )
drestar.place(x=210, y=200)
treiniciar=tkinter.Button(ventana, text="reiniciar",command=reiniciar,bg="gray", width=10,height=2 )
treiniciar.place(x=390, y=200)
contador=tkinter.Label(ventana, text="contador",foreground="blue", font="cambria 35")
contador.place(x=165, y=20)
contador=tkinter.Label(ventana, text="0", font="cambria 35")
contador.place(x=235, y=90)

ventana.mainloop()