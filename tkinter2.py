import tkinter
     
class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()

        self.Morningbutton= tkinter.Button()
        self.Morningbutton["text"]="GoodMorning"
        self.Morningbutton["command"]=self.morning
        self.Morningbutton.pack()

        self.Afternoonbutton= tkinter.Button()
        self.Afternoonbutton["text"]="GoodAfternoon"
        self.Afternoonbutton["command"]=self.afternoon
        self.Afternoonbutton.pack()

        self.Eveningbutton= tkinter.Button()
        self.Eveningbutton["text"]="GoodEvening"
        self.Eveningbutton["command"]=self.evening
        self.Eveningtbutton.pack()

        self.Quibutton= tkinter.Button()
        self.Quibutton["text"]="Quit"
        self.Quibutton["command"]=self.quit
        self.Quitbutton.pack()
 

    def Morning("GoodMorning"):
        print("self.morning")
    def afternoon("GoodAfternoon"):
        print("self.afternoon")
    def evening("GoodEvening"):
        print("self.evening")
    def "quit"("goodbye"):
        print("self.quit")
 

 
    
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
     

