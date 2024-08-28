from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("400x300")
        self.master.title("Assignment 12")
        self.grid()
        
        self.my_label = Label(self, text = "Enter your text: ", font = "Courier 10")
        self.my_label.grid(row=0, column=0)
        
        self.enter_text = Entry(self)
        self.enter_text.grid(row=0, column=1)
        
        self.submit_button = Button(self, text = "Submit", command= self.submit_button_text)
        self.submit_button.grid(row=0, column=2)
        
        self.default_text = StringVar()
        self.default_text.set("Sample Text")
        self.my_new_text = Label(self, text="Sample Text", font = "Courier 10")
        self.my_new_text.grid(row=1, column=0, columnspan=3, pady=5)
        
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 2, column = 0)
        
        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 2, column = 1)
        
        self.font_size = StringVar()
        self.font_size.set("10")
        self.font_size_10 = Radiobutton(self, text = "10 point",
                variable=self.font_size,  value = 10, command = self.set_font)
        self.font_size_10.grid(row = 3, column = 0)
        
        self.font_size_12 = Radiobutton(self, text = "12 point",
                variable=self.font_size,  value = 12, command = self.set_font)
        self.font_size_12.grid(row = 3, column = 1)
        
        self.font_size_14 = Radiobutton(self, text = "14 point",
                variable=self.font_size,  value = 14, command = self.set_font)
        self.font_size_14.grid(row = 3, column = 2)
        
    def submit_button_text(self):
        if self.enter_text.get() != "":
            self.my_new_text.config(text= self.enter_text.get())
            
    def set_font(self):
        new_font = "Courier"
        
        if self.font_size.get() == "10":
            new_font =  new_font + " 10"
        elif self.font_size.get() == "12":
            new_font =  new_font + " 12"
        else:
            new_font =  new_font + " 14"
        
        if self.bold_on.get() == 1:
            new_font = new_font + " bold"
        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
        
        self.my_new_text.config(font =  new_font)

draw_frame = MyFrame()
draw_frame.mainloop()
