import tkinter
class Application(tkinter.Frame):
    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.points=0
        

        self.askquestion1button= tkinter.Button()
        self.askquestion1button["text"]=" askquestion1"
        self.askquestion1button["command"]=self.askquestion1
        self.askquestion1button.pack()

        self.askquestion2button= tkinter.Button()
        self.askquestion2button["text"]="askquestion2"
        self.askquestion2button["command"]=self.question2
        self.askquestion2button.pack()

        self.askquestion3button= tkinter.Button()
        self.askquestion3button["text"]="askquestion3"
        self.question3button["command"]=self.question3
        self.question3button.pack()

        self.pointbutton= tkinter.Button()
        self.pointbutton["text"]="point"
        self.pointbutton["command"]=self.point
        self.pointbutton.pack()

        self.exitbutton= tkinter.Button()
        self.exitbutton["text"]="Point"
        self.exitbutton["command"]=self.DisplayPoints
        self.exitbutton.pack()
 



    def askquestion1(self):
        response=tkinter.messagebox.askyesno("question1","Answer:Yes")
        if(response==True):
            points+=1
    def question2(self):
       response=tkinter.messagebox.askyesno("question1","Answer:No")
        if(response==false):
            points+=1
    def question3(self):
        response=tkinter.messagebox.askyesno("question1","Answer:No")
        if(response==True):
            points+=1
   tkinter.message.box
                                             
root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()    
