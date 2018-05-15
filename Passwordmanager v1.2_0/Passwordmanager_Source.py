#Passwordmanager
from tkinter import *
from tkinter import messagebox
import random
import string
import os

root = Tk()

class GUI:

    version = "v1.2_0"

    logo = PhotoImage(file="logo.png")

    keys = PhotoImage(file="keys.png")

    scope = PhotoImage(file="scope.png")

    def OpenMMenu(self, master):

        self.master = master

        master.iconbitmap("_ico2.ico")
        master.title("Passwordmanagement Utility, PSMU")
        master.minsize(width=900, height=600)
        master.maxsize(width=900, height=600)

    # Frames

        master.frame_top = Frame(master, width=900, height=200)
        master.frame_middle = Frame(master, width=900, height=100)
        master.frame_bottom = Frame(master, width=900, height=100)

        master.frame_top.pack(side="top")
        master.frame_middle.pack()
        master.frame_bottom.pack(side="bottom")

    # Buttons

        master.quit_button = Button(master.frame_middle, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                    width=10, height=1, text="Exit", command=master.destroy)
        master.info_button = Button(master.frame_middle, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                    width=10, height=1, text="Info", command=self.inform)
        master.new_button = Button(master.frame_middle, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                   width=15, height=1, text="Create & Store", command=self.OpenCMenu)
        master.opnstorage_button = Button(master.frame_middle, bg="dodger blue", fg="white", relief="flat",
                                          font="Arial", width=15, height=1, text="Open Storage",
                                          command=self.OpenStorage)
        master.smenu_button = Button(master.frame_middle, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                     width=15, height=1, text="Password Finder", command=self.OpenSMenu)

        master.quit_button.grid(row=1, column=5, padx=20, pady=20)
        master.info_button.grid(row=1, column=1, padx=20, pady=20)
        master.info_button.grid(row=1, column=1, padx=20, pady=20)
        master.new_button.grid(row=1, column=4, padx=20, pady=20)
        master.opnstorage_button.grid(row=1, column=2, padx=20, pady=20)
        master.smenu_button.grid(row=1, column=3, padx=20, pady=20)

    # Labels

        master.label_top = Label(master.frame_top, image=self.logo)
        master.label_bottom = Label(master.frame_bottom, text=self.version, font=("Arial", 7), fg="grey")

        master.label_top.pack()
        master.label_bottom.pack(side="bottom")

    # Debugger

    def test(self):
        print("works")

    ###################

    def OpenCMenu(self):

        cmenu = Toplevel(self.master)
        self.cmenu = cmenu

        cmenu.iconbitmap("_ico2.ico")
        cmenu.title("Creation Menu")
        cmenu.wm_attributes("-topmost", 1)
        cmenu.minsize(width=512, height=310)
        cmenu.maxsize(width=512, height=310)

    # Frames

        cmenu.frame_top = Frame(cmenu)
        cmenu.frame_middle = Frame(cmenu)
        cmenu.frame_bottom = Frame(cmenu)

        cmenu.frame_top.pack(side="top")
        cmenu.frame_middle.pack()
        cmenu.frame_bottom.pack(side="bottom")

    # Standard Menu

        # Entrys

        cmenu_entry_app_out = StringVar()
        cmenu_entry_pw_out = StringVar()

        cmenu.entry_app = Entry(cmenu.frame_middle, textvariable=cmenu_entry_app_out)
        cmenu.entry_pw = Entry(cmenu.frame_middle, textvariable=cmenu_entry_pw_out)

        cmenu.entry_pw.grid(row=1, column=2, pady=10)
        cmenu.entry_app.grid(row=0, column=2)

        # Buttons

        cmenu.entry_submit = Button(cmenu.frame_bottom, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                    width=10, height=1, text="Submit",
                                    command=lambda: self.CheckInput(cmenu_entry_app_out,
                                                                    cmenu_entry_pw_out))

        cmenu.quit_button = Button(cmenu.frame_bottom, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                   width=10, height=1, text="Exit", command=cmenu.destroy)

        cmenu.shuffle_button = Button(cmenu.frame_bottom,bg="light gray", fg="white", relief="flat", font="Arial",
                                      width=10, height=1, text="Shuffle", state="disabled", command=self.Generator(0, cmenu.entry_pw))

        cmenu.entry_submit.grid(row=0, pady=10, padx=15)
        cmenu.shuffle_button.grid(row=0, column=1, pady=10,padx=15)
        cmenu.quit_button.grid(row=0, column=2, pady=10, padx=15)

        # Labels

        cmenu.label_top = Label(cmenu.frame_top, image=self.keys)
        cmenu.label_app = Label(cmenu.frame_middle, font="Arial, 10", text="Enter Applic.-name")
        cmenu.label_pw = Label(cmenu.frame_middle, font="Arial, 10", text="Insert Password")

        cmenu.label_top.grid(row=0, pady=20)
        cmenu.label_app.grid(row=0, column=1, padx=10)
        cmenu.label_pw.grid(row=1, column=1, sticky=W, padx=10, pady=10)

        def OpenCMenu_Standard():

            # Entrys

            cmenu.entry_app.configure(justify="left")
            cmenu.entry_pw.configure(state="normal", width=20, relief="sunken", justify="left")
            cmenu.entry_app.grid(row=0, column=2)
            cmenu.entry_pw.grid(row=1, column=2, pady=10)

            # Buttons

            cmenu.shuffle_button.configure(state="disabled", bg="light gray")

            # Labels

            cmenu.label_app.grid(row=0, column=1, padx=10)
            cmenu.label_pw.grid(row=1, column=1, padx=10, pady=10)

        def OpenCMenu_Autol(x):

            # Entrys

            cmenu.entry_app.configure(justify="center")

            cmenu.entry_pw.configure(state="readonly", width=50, relief="flat", justify="center")
            cmenu.entry_app.grid(row=1, columnspan=2)
            cmenu.entry_pw.grid(row=2, columnspan=2, pady=10)

            # Buttons

            cmenu.shuffle_button.configure(state="normal", bg="dodger blue", command=lambda : self.Generator(15, x))

            # Labels

            cmenu.label_app.grid(row=0, column=2, sticky=E)
            cmenu.label_pw.grid_remove()

        def OpenCMenu_Auto2(x):

            # Entrys

            cmenu.entry_app.configure(justify="center")

            cmenu.entry_pw.configure(state="readonly", width=50, relief="flat", justify="center")
            cmenu.entry_app.grid(row=1, columnspan=2)
            cmenu.entry_pw.grid(row=2, columnspan=2, pady=10)

            # Buttons

            cmenu.shuffle_button.configure(state="normal", bg="dodger blue", command=lambda: self.Generator(30, x))

            # Labels

            cmenu.label_app.grid(row=0, column=2, sticky=E)
            cmenu.label_pw.grid_remove()

        def OpenCMenu_Auto3(x):

            # Entrys

            cmenu.entry_app.configure(justify="center")

            cmenu.entry_pw.configure(state="readonly", width=50, relief="flat", justify="center")
            cmenu.entry_app.grid(row=1, columnspan=2)
            cmenu.entry_pw.grid(row=2, columnspan=2, pady=10)

            # Buttons

            cmenu.shuffle_button.configure(state="normal", bg="dodger blue", command=lambda: self.Generator(50, x))

            # Labels

            cmenu.label_app.grid(row=0, column=2, sticky=E)
            cmenu.label_pw.grid_remove()

    # Dropdownmenu

        cmenu.menu = Menu(cmenu)
        cmenu.config(menu=cmenu.menu)

        cmenu.sub1 = Menu(cmenu.menu)

        cmenu.sub1.add_command(label="Instructions", command=self.instructions)
        cmenu.sub2 = Menu(cmenu.menu)

        cmenu.sub2.add_command(label="Manual", command=OpenCMenu_Standard)
        cmenu.sub2.add_separator()
        cmenu.sub2.add_command(label="Auto - Min. Security", command=lambda : OpenCMenu_Autol(cmenu.entry_pw))
        cmenu.sub2.add_command(label="Auto - Medium Strength", command=lambda : OpenCMenu_Auto2(cmenu.entry_pw))
        cmenu.sub2.add_command(label="Auto - Maximum Strength", command=lambda : OpenCMenu_Auto3(cmenu.entry_pw))

        cmenu.menu.add_cascade(label="Help", menu=cmenu.sub1)
        cmenu.menu.add_cascade(label="Generation Options", menu=cmenu.sub2)

    def OpenSMenu(self):

        smenu = Toplevel(self.master)
        self.smenu = smenu

        smenu.iconbitmap("_ico2.ico")
        smenu.title("Passcode Finder")
        smenu.wm_attributes("-topmost", 1)
        smenu.minsize(width=512, height=288)
        smenu.maxsize(width=512, height=288)

    # Frame

        smenu.frame_top = Frame(smenu)
        smenu.frame_middle = Frame(smenu)
        smenu.frame_bottom = Frame(smenu)

        smenu.frame_top.pack(side="top")
        smenu.frame_middle.pack()
        smenu.frame_bottom.pack(side="bottom")

    # Entry

        smenu_entry_app_out = StringVar()

        smenu.entry_app = Entry(smenu.frame_middle, relief="sunken", textvariable=smenu_entry_app_out, justify="center")

        smenu.entry_app.grid(row=1, pady=5, padx=10)

    # Outputs

        smenu_output_pw = Entry(smenu.frame_middle, bg="grey", relief="flat", font="Arial, 10", state="readonly", width= 70, justify="center")
        smenu_output_pw.grid(row=2, pady=5, padx=10)

    # Buttons

        smenu.search_button = Button(smenu.frame_bottom, bg="dodger blue", fg="white", relief="flat",
                                     font="Arial", width=10, height=1, text="Search", command=lambda : self.ReadFromSendTo(smenu_entry_app_out,
                                                                                                                           smenu_output_pw))
        smenu.quit_button = Button(smenu.frame_bottom, bg="dodger blue", fg="white", relief="flat", font="Arial",
                                   width=10, height=1, text="Exit", command=smenu.destroy)

        smenu.search_button.grid(row=1, pady=10, padx=15)
        smenu.quit_button.grid(row=1, column=1, pady=10, padx=15)

    # Labels

        smenu.label_top = Label(smenu.frame_top, image=self.scope)
        smenu.label_entry = Label(smenu.frame_top, font="Arial, 10", text="Enter Applications Name")

        smenu.label_top.grid(row=0, pady=20)
        smenu.label_entry.grid(row=1, padx=10)

    def instructions(self):

        messagebox.showinfo("Instructions","This is the Creation Menu, by clicking the 'Generation Options'-Tab in the "
                                        "menu you have the choice between four different modes of password creation."
                                        "The first one is the human one, very simple, you decide the password "
                                        "yourself, the second to fourth ones are going to automatically create a "
                                        "password for you. \n"
                                        "The Min.security option is going to create a password consisting "
                                        "out of 15 "
                                        "letters, upper- as well as lowercase, and Numbers. If needed or wanted "
                                        "you "
                                        "can also add extra characters yourself."
                                        "The Medium and Maximum strength will only bump up the amount of characters used for the created password.")

    def inform(self):

        messagebox.showinfo("Important information",
                            "" + self.version + "\n" + "This is an OpenSource Software developed by Timo Sturm, "
                                                       "http://GitHub.com/GBPierce \nInstructions: \nYou can click "
                                                       "the 'Create & Store' Button in the main menu to bind a "
                                                       "password to a predefined application.\nYou can use the "
                                                       "Password Finder button to automatically get the password "
                                                       "printed out by looking up the name of the Application it was "
                                                       "assigned to\nThe 'Open Storage' Button is only for manual "
                                                       "maintenance, notice that this Software is going to freeze "
                                                       "during the time you're messing with the storage!\nThis "
                                                       "Project is WIP. Planned features are:\n - Encryption for your "
                                                       "Passwords\n - Possibility to store Passwords online to use "
                                                       "the Software\n   everywhere\n - Automatic password generation "
                                                       "with a mix of up to 40\n   Letters and Numbers [Accomplished]")

    def CheckInput(self, x, y):

        Input_Name = x
        Input_PW = y

        if Input_Name.get() == "" or Input_PW.get() == "":
            messagebox.showerror(parent=self.cmenu, title="Error!",
                                 message="You must  provide a name as well as a Password.")
        elif (" " in Input_Name.get()) == True or (" " in Input_PW.get()):
            messagebox.showerror(parent=self.cmenu, title="Error!",
                                 message="You can't use spacing within Application name nor corresponding Password")
        else:
            str1 = "".join(Input_Name.get())
            str2 = "".join(Input_PW.get())
            ToStore = str1 + " " + str2 #+ "\n"
            self.WriteTo(ToStore)
            messagebox.showinfo(parent=self.cmenu, title="Success!",
                                message="You successfully saved a Password for " + str1 + ".")

    def WriteTo(self, y):

        with open("Storage.txt", "a") as input:
            input.write(y + "\n")

    def ReadFrom(self):

        with open("Storage.txt", "r") as f:
            f.read()

    def ReadFromSendTo(self, x, y):

        Input_Name = x
        str3 = "".join(Input_Name.get())
        Dic = {}
        with open("Storage.txt", "r") as searchfile:
            for line in searchfile:
                (key, val) = line.split()
                Dic[key] = val
                if str3 in Dic:
                    y.configure(state="normal")
                    y.delete(0, END)
                    y.insert(0, Dic[str3])
                    y.configure(state="readonly")

                elif str3 == "":
                    y.configure(state="normal")
                    y.delete(0, END)
                    y.insert(0, "You need to enter the name of previously assigned application to begin.")
                    y.configure(state="readonly")

                else:
                    y.configure(state="normal")
                    y.delete(0, END)
                    y.insert(0, "No password assigned to " + str3 + ".")
                    y.configure(state="readonly")


    def Generator(self, x, y):
        GenerationResult = []
        z = 0
        while z < x:
            v = random.choice(string.ascii_letters + string.digits)
            GenerationResult.append(v)
            z += 1

        str4 = "".join(map(str, GenerationResult))
        y.configure(state="normal")
        y.delete(0, END)
        y.insert(0, str4)

    def OpenStorage(self):

        os.system("Storage.txt")

Interface = GUI()
Interface.OpenMMenu(root)
root.mainloop()

