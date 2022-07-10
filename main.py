
import pymongo
from tkinter import *
from tkinter import ttk



MONGO_URI ='mongodb://localhost'

cliente= pymongo.MongoClient(MONGO_URI)

baseDatos= cliente['PersonasDB']
collection=baseDatos['Personas']

#Ventana y Widgets de Tkinter
root=Tk()
frm=Frame(root)
frm.grid(row=0,column=0)

tabla= ttk. Treeview(root,columns=2)
tabla.grid(row=1,column=0)
tabla.heading("#0",text='Rut')
tabla.heading('#1',text='Nombre')


def InsertarDatos():
    lista= [
        {'_id':209188830,'Nombre':'Nicolas'},
        {'_id':190184835,'Nombre':'Juan'},
        {'_id':219082331,'Nombre':'Pedro'},
        {'_id':227185586,'Nombre':'Diego'},
    ]
    collection.insert_many(lista)


def MostrarDatos():
    
    for r in collection.find():
        tabla.insert('',0,text=r['_id'],values=r['Nombre'])
        
        

btn=Button(frm,text='Mostar Datos',command=MostrarDatos)
btn1=Button(frm,text='Insertar Datos',command=InsertarDatos)
btn.grid(row=0,column=0,padx=10,pady=10)
btn1.grid(row=0,column=1)

root.mainloop()