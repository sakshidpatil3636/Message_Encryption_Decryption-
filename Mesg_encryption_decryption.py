from tkinter import *
import base64
import time


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def show_message():
    clear = Msg.get()
    k = key.get()
    m = mode.get()

    try:
        if not clear or not k:
            raise ValueError("Error:Please enter key and message input.")
        # elif not is_valid_key(k):
        # raise ValueError("Error: Invalid key")
        else:
            if m == 'e':
                Result.set(encode(k, clear))
            else:
                Result.set(decode(k, clear))
    except ValueError as e:
        Result.set(str(e))


def is_valid_key(key):
    if len(key) > 8:
        return False
    return True


def reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


root = Tk()
root.configure(bg="lightgray")  # Set background color

root.geometry("1000x600")

root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN, bg="lightgray")  # Set background color
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN, bg="lightgray")  # Set background color
f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('times', 50, 'bold'), text="MESSAGE\nEncryption & Decryption",
                fg="black", bd=10, anchor='w', bg="lightgray")  # Set background color
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="red", bd=10, anchor='w',
                bg="lightgray")  # Set background color
lblInfo.grid(row=1, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# Set label and entry widget colors and border relief style
label_bg_color = "lightblue"
entry_bg_color = "lightcyan"
relief_style = "groove"

lblReference = Label(f1, font=('arial', 16, 'bold'), text="NAME ::", bd=5, anchor="w", bg=label_bg_color,
                     relief=relief_style)
lblReference.grid(row=0, column=0, padx=2, pady=2)

txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=5, insertwidth=4, bg=entry_bg_color,
                     justify='right', relief=relief_style)
txtReference.grid(row=0, column=1, padx=2, pady=2)

lblMsg = Label(f1, font=('arial', 16, 'bold'), text="MESSAGE ::", bd=5, anchor="w", bg=label_bg_color,
               relief=relief_style)
lblMsg.grid(row=1, column=0, padx=2, pady=2)

txtMsg = Entry(f1, font=('arial', 16, 'bold'), textvariable=Msg, bd=5, insertwidth=4, bg=entry_bg_color,
               justify='right', relief=relief_style)
txtMsg.grid(row=1, column=1, padx=2, pady=2)

lblkey = Label(f1, font=('arial', 16, 'bold'), text="KEY ::", bd=5, anchor="w", bg=label_bg_color, relief=relief_style)
lblkey.grid(row=2, column=0, padx=2, pady=2)

txtkey = Entry(f1, font=('arial', 16, 'bold'), textvariable=key, bd=5, insertwidth=4, bg=entry_bg_color,
               justify='right', relief=relief_style)
txtkey.grid(row=2, column=1, padx=2, pady=2)

lblmode = Label(f1, font=('arial', 16, 'bold'), text="MODE (e-encrypt, d-decrypt) ::", bd=5, anchor="w",
                bg=label_bg_color, relief=relief_style)
lblmode.grid(row=3, column=0, padx=2, pady=2)

txtmode = Entry(f1, font=('arial', 16, 'bold'), textvariable=mode, bd=5, insertwidth=4, bg=entry_bg_color,
                justify='right', relief=relief_style)
txtmode.grid(row=3, column=1, padx=2, pady=2)

lblService = Label(f1, font=('arial', 16, 'bold'), text="The RESULT ::", bd=5, anchor="w", bg=label_bg_color,
                   relief=relief_style)
lblService.grid(row=4, column=0, padx=2, pady=2)

txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Result, bd=5, insertwidth=4, bg=entry_bg_color,
                   justify='right', relief=relief_style, width=40)
txtService.grid(row=4, column=1, padx=2, pady=2)

btnTotal = Button(f1, padx=16, pady=8, bd=5, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="lightgreen", command=show_message)
btnTotal.grid(row=1, column=3, padx=20, pady=20)

btnReset = Button(f1, padx=16, pady=8, bd=5, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="lightpink", command=reset)
btnReset.grid(row=2, column=3, padx=20, pady=20)

btnExit = Button(f1, padx=16, pady=8, bd=5, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="lightcoral", command=root.destroy)
btnExit.grid(row=3, column=3, padx=20, pady=20)

root.mainloop()

