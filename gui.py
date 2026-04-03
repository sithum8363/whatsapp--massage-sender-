from tkinter import *
from tkinter import messagebox
import threading
import whatsapp_web

def mas():
    messagebox.showinfo(" error", "programing is out  enter  number agine ")
def start():
    messagebox.showinfo("start", " start sending massage ")
root =Tk()
root.geometry("600x550")
root.title("whatsapp massage sender")
icon = PhotoImage(file="whatsapp.png")
root.iconphoto(True, icon)
root.configure(bg="green")
massage_value=[]
number_value=[]
time_value=[]
Label(root,text ="number").grid(row=0,column=2)
Label(root,text ="message").grid(row=0,column=3)
Label(root,text ="time").grid(row=0,column=4)
def add():
    row = len(number_value) + 1
    number = Entry(root)
    number.grid(row=row, column=2, pady=3, padx=2)
    number_value.append(number)
    massage =Entry(root)
    massage.grid(row=row, column=3, pady=3, padx=2)
    massage_value.append(massage)
    time=Entry(root)
    time.grid(row=row,column=4,pady=3,padx=2)
    time_value.append(time)
add_button = Button(root, text="Add Text Box", command=add)
add_button.grid(row=4, column=0, columnspan=2, padx=5,pady=1)

add()


def send():
    data = []
    for i in range(len(number_value)):
        num = number_value[i].get().strip()
        if not num:
            mas()
            return
        msg = massage_value[i].get()
        tm = time_value[i].get()
        data.append({'number': num, 'message': msg, 'time': tm})
    def w():
        whatsapp_web.send_e(data)
    threading.Thread(target=w, daemon=True).start()
button = Button(root, text="send massage", command=send)
button.grid(row=0 , column=0,  padx=5,pady=1)

root.mainloop()
