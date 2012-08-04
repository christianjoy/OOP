import tkinter
class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.HelloButton=tkinter.Button()
        self.HelloButton["text"]="Click me"
        self.HelloButton["command"]=self.hello
        self.HelloButton.pack()
    def hello(self):
        print("I Love You\n    and\nI Miss You\n")

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
