import string
import random
import tkinter
import pandas as pd
import csv

# BACKEND
def Close():
    window.destroy()

def Copy():
    global password
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    
def Generate():
    global password
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plene = plen.get()
    apps = app.get()
    #print(plene)
    #print(type(plene))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    #print("".join(s[0:plene]))
    password = "".join(s[0:plene])
    er['text'] = "Your " + apps + " Password is: " + password

    # Saving to Spreadsheet
    #df = pd.read_csv("data.csv")
    data = [[apps, password]]
    df = pd.DataFrame(data)
    df.to_csv('data.csv', mode='a', header=False, index=False)

# FRONTEND
window = tkinter.Tk()
window.geometry("500x450")
window.title("Password Generator")
heading = tkinter.Label(window, text = "Password Generator",font=('arial',20,"bold"))
heading.pack()

l1 = tkinter.Label(window,text="How longer the password you need",font="san-serif",fg="red")
l1.pack()
plen = tkinter.IntVar()
e1 = tkinter.Entry(window, textvariable=plen)
e1.pack()

l2 = tkinter.Label(window,text="In which app you use this password",font="san-serif",fg="red")
l2.pack()
app = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable=app)
e2.pack()

txt = tkinter.Label(window, text = "",font=('arial',14,"bold"))
txt.pack()
er = tkinter.Label(window, text = "",font=('arial',14,"bold"))
er.pack()

b1 = tkinter.Button(window,text="Generate",command=Generate)
b1.pack()

b2 = tkinter.Button(window,text="Copy",command=Copy)
b2.pack()

b3 = tkinter.Button(window,text="Close Application",command=Close)
b3.pack() 

window.mainloop()
