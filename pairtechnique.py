# Longevity
# Demonstrates text and entry widgets, and the grid layout manager

from tkinter import *
import tkinter as tk
root = tk.Tk()
var = tk.StringVar(root)#create a conjuagated string
var2 = tk.StringVar(root)#creates a 2nd conjuagated string



class Application(Frame):
    def __init__(self, master):#initilzes the frame
        super(Application, self).__init__(master)#sets itself as the master frame
        self.grid()#creates a grid placing in the super frame
        self.create_widgets()#creates everything in the function of create widgets
        self.configure(bg='orange')

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.inst_lbl = Label(self,bg ='green', text = "Attacker")
        self.inst_lbl.grid(row = 0, column = 0, columnspan =1, sticky = W)
        #creates 2nd label
        self.inst_lbl = Label(self,bg ='green', text = "Defender")
        self.inst_lbl.grid(row = 0, column = 1, columnspan =1, sticky = W)
        #drop down menu
        choices = ['Attacker', 'Defender']
        self.option = tk.OptionMenu(root, var, *choices)
        
            
        self.option.grid(row = 11, column = 0)#uses grid system to place drop down menu

        choices2 = ['Attacker', 'Defender']
        self.option2 = tk.OptionMenu(root, var2, *choices2)#function which create dropdown menu
        self.option2.grid(row = 11, column = 1)#uses grid menu to place 2nd drop box


        #entry boxes for pair technique
        self.pw_ent2 = Entry(self)
        self.pw_ent2.grid(row = 2, column = 0, columnspan = 3, sticky = W)

        self.pw_ent3 = Entry(self)
        self.pw_ent3.grid(row = 3, column = 0, columnspan = 3, sticky = W)

        self.pw_ent4 = Entry(self)
        self.pw_ent4.grid(row = 4, column = 0, columnspan = 3, sticky = W)

        self.pw_ent5 = Entry(self)
        self.pw_ent5.grid(row = 5, column = 0, columnspan = 3, sticky = W)

        self.pw_ent6 = Entry(self)
        self.pw_ent6.grid(row = 6, column = 0, columnspan = 3, sticky = W)

        self.pw_ent7 = Entry(self)
        self.pw_ent7.grid(row = 7, column = 0, columnspan = 3, sticky = W)

        self.pw_ent8 = Entry(self)
        self.pw_ent8.grid(row = 8, column = 0, columnspan = 3, sticky = W)

        self.pw_ent9 = Entry(self)
        self.pw_ent9.grid(row = 9, column = 0, columnspan = 3, sticky = W)

        self.pw_ent10 = Entry(self)
        self.pw_ent10.grid(row = 10, column = 0, columnspan = 3, sticky = W)

        # create entry widget to accept password      
        self.pw_ent1 = Entry(self)
        self.pw_ent1.grid(row = 2, column = 1, columnspan = 3, sticky = W)

        self.pw_ent11 = Entry(self)
        self.pw_ent11.grid(row = 3, column = 1, columnspan = 3, sticky = W)

        self.pw_ent12 = Entry(self)
        self.pw_ent12.grid(row = 4, column = 1, columnspan = 3, sticky = W)


        self.pw_ent13 = Entry(self)
        self.pw_ent13.grid(row = 5, column = 1, columnspan = 3, sticky = W)

        self.pw_ent14 = Entry(self)
        self.pw_ent14.grid(row = 6, column = 1, columnspan = 3, sticky = W)

        self.pw_ent15 = Entry(self)
        self.pw_ent15.grid(row = 7, column = 1, columnspan = 3, sticky = W)

        self.pw_ent16 = Entry(self)
        self.pw_ent16.grid(row = 8, column = 1, columnspan = 3, sticky = W)

        self.pw_ent17 = Entry(self)
        self.pw_ent17.grid(row = 9, column = 1, columnspan = 3, sticky = W)

        self.pw_ent18 = Entry(self)
        self.pw_ent18.grid(row = 10, column = 1, columnspan = 3, sticky = W)

        # create submit button
        self.submit_bttn = Button(self,bg ='light blue',text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 18, column = 1, columnspan = 3, sticky = E)

        # create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 16, column = 0, columnspan = 2, sticky = S)
        message = "enter your pair technique into the textboxes,a move for each one"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

    def reveal(self):
       #gets all information from boxes
        contents1 = self.pw_ent1.get()
        contents2 = self.pw_ent2.get()
        contents3 = self.pw_ent3.get()
        contents4 = self.pw_ent4.get()
        contents5 = self.pw_ent5.get()
        contents6 = self.pw_ent6.get()
        contents7 = self.pw_ent7.get()
        contents8 = self.pw_ent8.get()
        contents9 = self.pw_ent9.get()
        contents10 = self.pw_ent10.get()
        contents11 = self.pw_ent11.get()
        contents12 = self.pw_ent12.get()
        contents13 = self.pw_ent13.get()
        contents14 = self.pw_ent14.get()
        contents15 = self.pw_ent15.get()
        contents16 = self.pw_ent16.get()
        contents17 = self.pw_ent17.get()
        contents18 = self.pw_ent18.get()
        
        color = var.get()#gets attacker or defender from drop down
        
        color2 = var2.get()
        
        #message based on pair technique
        if color=="Attacker" and color2=="Attacker":
            message1 = "sorry you cannot have two attackers to a pair technique only attacker and defender"
            self.secret_txt.delete(0.0, END)
            self.secret_txt.insert(0.0, message1)
        elif color=="Defender" and color=="Defender":
            message1 = "sorry you cannot have two defenders to a pair technique only attacker and defender"
            self.secret_txt.delete(0.0, END)
            self.secret_txt.insert(0.0, message1)
        else:
            message1 = "you have inserted your pair technique correctly"
            self.secret_txt.delete(0.0, END)
            self.secret_txt.insert(0.0, message1)
            print(color)
            print(color2)
        
        
        
        
    

# main

root.title("Pair Techniques")
root.configure(bg='orange')
root.geometry("300x600")

app = Application(root)

root.mainloop()
