#Passwordmanager
from tkinter import *
from tkinter import messagebox
import os


class GUI:
    
    version = "v1.1_1"
    
    def __init__(self, master):

        #Initialization

        self.master = master
        master.title("Passwordmanagement Utility, PSMU")
        master.minsize(width = 900, height = 600)
        master.maxsize(width = 900, height = 600)

        #Images

        logo = PhotoImage(file = "logo.png")
        self.logo = logo
        keys = PhotoImage(file = "keys.png")
        self.keys = keys
        scope = PhotoImage(file = "scope.png")
        self.scope = scope

        #Frames       

        self.frame_top = Frame(master, height = 640, width = 640)
        self.frame_top.pack(side = "top")
        self.frame_middle = Frame(master)
        self.frame_middle.pack()
        self.frame_bottom = Frame(master)
        self.frame_bottom.pack(side = "bottom")

        #Buttons

        self.quit_button = Button(self.frame_middle, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Exit", command = master.destroy)
        self.quit_button.grid(row = 1, column = 5, padx = 20, pady = 20)
        self.info_button = Button(self.frame_middle, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Info", command = self.inform)
        self.info_button.grid(row = 1, column = 1, padx = 20, pady = 20)
        self.new_button = Button(self.frame_middle, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 15, height = 1, text = "Create & Store", command = self.OpenCMenu)
        self.new_button.grid(row = 1, column = 4, padx = 20, pady = 20)
        self.opnstorage_button = Button(self.frame_middle, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 15, height = 1, text = "Open Storage", command = self.OpenStorage)
        self.opnstorage_button.grid(row = 1, column = 2, padx = 20, pady = 20)
        self.smenu_button = Button(self.frame_middle, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 15, height = 1, text = "Password Finder", command = self.OpenSMenu)
        self.smenu_button.grid(row = 1, column = 3, padx = 20, pady = 20)
        
        #Labels

        self.label_top = Label(self.frame_top, image = self.logo)
        self.label_top.pack()
        self.label_bottom = Label(self.frame_bottom, text = self.version, font = ("Arial", 7), fg = "grey")
        self.label_bottom.pack(side = "bottom")

    #Commands

    def test(self):

        pass
            
    def OpenCMenu(self):

        #Base

        new = Toplevel(self.master)
        self.new = new
        new.title("Creation Menu")
        new.wm_attributes("-topmost", 1)
        new.minsize(width = 512, height = 288)
        new.maxsize(width = 512, height = 288)

        #Frames

        new_frame_top = Frame(new)
        new_frame_top.pack(side = "top")
        new_frame_middle = Frame(new)
        new_frame_middle.pack()
        new_frame_bottom = Frame(new)
        new_frame_bottom.pack(side = "bottom")

        #Labels

        new_label_top = Label(new_frame_top, image = self.keys)
        new_label_top.grid(row = 0, pady = 20)

        new_label_game = Label(new_frame_middle, text = "Enter Applic.-name")
        new_label_game.grid(row = 0, column = 1, sticky = W, padx = 10)
        new_label_pw = Label(new_frame_middle, text = "Insert Password")
        new_label_pw.grid(row = 1, column = 1, sticky = W, padx = 10, pady = 10)

        #Widgets

        self.new_entry_game_out = StringVar()
        self.new_entry_game = Entry(new_frame_middle, textvariable = self.new_entry_game_out)
        self.new_entry_game.grid(row = 0, column = 2)

        self.new_entry_pw_out = StringVar()
        self.new_entry_pw = Entry(new_frame_middle, textvariable = self.new_entry_pw_out)
        self.new_entry_pw.grid(row = 1, column = 2)

        self.new_entry_submit = Button(new_frame_bottom, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Submit", command = self.CheckInput)
        self.new_entry_submit.grid(row = 0, pady = 10, padx = 15)
        new_quit_button = Button(new_frame_bottom, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Exit", command = new.destroy)
        new_quit_button.grid(row = 0, column = 1, pady = 10, padx = 15)
    
    def OpenSMenu(self):

        #Base

        smenu = Toplevel(self.master)
        self.smenu = smenu
        smenu.title("Passcode Finder")
        smenu.wm_attributes("-topmost", 1)
        smenu.minsize(width = 512, height = 288)
        smenu.maxsize(width = 512, height = 288)

        #Frame

        smenu_frame_top = Frame(smenu)
        smenu_frame_top.pack(side = "top")
        smenu_frame_middle = Frame(smenu)
        smenu_frame_middle.pack()
        smenu_frame_bottom = Frame(smenu)
        smenu_frame_bottom.pack(side = "bottom")

        #Labels

        smenu_label_top = Label(smenu_frame_top, image = self.scope)
        smenu_label_top.grid(row = 0 , pady = 20)
        smenu_label_smenu_entry = Label(smenu_frame_top, text = "Enter Applications Name")
        smenu_label_smenu_entry.grid(row = 1, padx = 10)
        
        #Widgets
        
        self.smenu_entry_name_out = StringVar()
        smenu_entry_name = Entry(smenu_frame_middle, textvariable = self.smenu_entry_name_out)
        smenu_entry_name.grid(row = 1, pady = 5, padx = 10)

        self.smenu_output = Entry(smenu_frame_middle, bg = "grey", relief = "flat", state = "readonly")
        self.smenu_output.grid(row = 2, pady = 5, padx = 10)

        smenu_entry_search_button = Button(smenu_frame_bottom, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Search", command = self.ReadFromSendTo)
        smenu_entry_search_button.grid(row = 1, pady = 10, padx = 15)

        smenu_quit_button = Button(smenu_frame_bottom, bg = "dodger blue", fg = "white", relief = "flat", font = "Arial", width = 10, height = 1, text = "Exit", command = smenu.destroy)
        smenu_quit_button.grid(row = 1, column = 1, pady = 10, padx = 15)
               
                                                                                                                            
    def inform(self):

        messagebox.showinfo("Important information", "" + self.version + "\n" + "This is an OpenSource Software developed by Timo Sturm, http://GitHub.com/GBPierce \nInstructions: \nYou can click the 'Create & Store' Button in the main menu to bind a password to a predefined application.\nYou can use the Password Finder button, to autmatically get the password printed out by looking up the name of the Application it was assigned to\nThe 'Open Storage' Button is only for manual maintenance, notice that this Software is going to freeze during the time you're messing with the storage!\nThis Project is WIP. Planned features are:\n - Encryption for your Passwords\n - Possibility to store Passwords online to use the Software\n   everywhere\n - Automatic password generation with a mix of up to 40\n   Symbols, Letters and Numbers")
        
    def CheckInput(self):

        Input_Name = self.new_entry_game_out
        Input_PW = self.new_entry_pw_out

        if Input_Name.get() == "" or Input_PW.get() == "":
            messagebox.showerror(parent = self.new, title = "Error!", message = "You must  provide a name aswell as a Password.") 

        else:
            str1 = "".join(Input_Name.get())
            str2 = "".join(Input_PW.get())
            ToStore = str1 + ", " + str2
            self.WriteTo(ToStore)
            messagebox.showinfo(parent = self.new, title = "Success!", message = "You succesfully saved a Password for " + str1 + ".")
            
    def WriteTo(self, y):

        with open("Storage.txt", "a") as x:
            x.write(y + "\n")

    def ReadFrom(self):
 
        with open("Storage.txt", "r") as f:
            f.read()

    def ReadFromSendTo(self):

        Input_Name = self.smenu_entry_name_out
        str3 = "".join(Input_Name.get())

        with open("Storage.txt", "r") as searchfile:
            for line in searchfile:
                if str3 in line:
                    self.smenu_output.configure(state = "normal")
                    self.smenu_output.delete(0, END)
                    self.smenu_output.insert(0, line[len(str3) + 2: len(line)])
                    self.smenu_output.configure(state = "readonly")
                    print("GppD")
                else:
                    print("Fuck")

    def OpenStorage(self):

        os.system("Storage.txt")
                         
root = Tk()
Interface = GUI(root)
root.mainloop()
