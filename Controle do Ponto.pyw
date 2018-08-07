# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.stdfont = ("Arial", "10")
        self.Container01 = Frame(master)
        self.Container01["pady"] = 10
        self.Container01.pack()
  
        self.Container02 = Frame(master)
        self.Container02["padx"] = 20
        self.Container02.pack()
  
        self.Container03 = Frame(master)
        self.Container03["padx"] = 20
        self.Container03.pack()
  
        self.Container04 = Frame(master)
        self.Container04["pady"] = 20
        self.Container04.pack()

        self.Container05 = Frame(master)
        self.Container05["pady"] = 0
        self.Container05.pack()
  
        self.Title = Label(self.Container01, text="Controle do Ponto")
        self.Title["font"] = ("Arial", "10", "bold")
        self.Title.pack()
  
        self.EnterTimeLabel = Label(self.Container02,text="Hora de Entrada", font=self.stdfont)
        self.EnterTimeLabel.pack(side=LEFT, padx = (0,10))
  
        self.enterHour = Entry(self.Container02)
        self.enterHour["width"] = 2
        self.enterHour["font"] = self.stdfont
        self.enterHour.pack(side=LEFT, padx = 5)

        self.twodots = Label(self.Container02, text = ':')
        self.twodots.pack(side = LEFT)

        self.enterMinute = Entry(self.Container02)
        self.enterMinute["width"] = 2
        self.enterMinute["font"] = self.stdfont
        self.enterMinute.pack(side=LEFT, padx = 5)
  
        self.exitTimeLaber = Label(self.Container03, text="Hora de Saída   ", font=self.stdfont)
        self.exitTimeLaber.pack(side=LEFT, padx = (0,10))
  
        self.outHour = Entry(self.Container03)
        self.outHour["width"] = 2
        self.outHour["font"] = self.stdfont
        self.outHour.pack(side=LEFT, padx = 5, pady = 10)

        self.twodots = Label(self.Container03, text = ':')
        self.twodots.pack(side = LEFT)
  
        self.outMinute = Entry(self.Container03)
        self.outMinute["width"] = 2
        self.outMinute["font"] = self.stdfont
        self.outMinute.pack(side=LEFT, padx = 5, pady = 10)

        self.SendButtom = Button(self.Container04)
        self.SendButtom["text"] = "Ok"
        self.SendButtom["font"] = ("Calibri", "8")
        self.SendButtom["width"] = 12
        self.SendButtom["command"] = self.getOutTime
        self.SendButtom.pack(pady = (5,25))

        self.jobTimeLabel = Label(self.Container04, text = "Jornada", font = self.stdfont)
        self.jobTimeLabel.pack(side = LEFT, padx = (0,10))

        self.jobHour = Entry(self.Container04)
        self.jobHour["width"] = 2
        self.jobHour["font"] = self.stdfont
        self.jobHour.insert(END,"09")
        self.jobHour.pack(side = LEFT, padx = 5)

        self.twodots = Label(self.Container04, text = ':')
        self.twodots.pack(side = LEFT)
  
        self.jobMinute = Entry(self.Container04)
        self.jobMinute["width"] = 2
        self.jobMinute["font"] = self.stdfont
        self.jobMinute.insert(END,"30")
        self.jobMinute.pack(side=LEFT, padx = 5, pady = 10)

        self.errorMessage = Label(self.Container05, text = "")
        self.errorMessage.pack(side=LEFT)


        self.outHour.configure(state = 'disabled')
        self.outMinute.configure(state = 'disabled')

    #Método verificar outHour
    def getOutTime(self,*args):
        try:
            hour = int(self.enterHour.get())
            minute = int(self.enterMinute.get())
            duration = int(self.jobHour.get()) * 60 + int(self.jobMinute.get())
            self.Container05["pady"] = 0
            self.errorMessage["text"] = ""
        except:
            self.Container05["pady"] = 20
            self.errorMessage["text"] = "Erro: entrada inválida"
            return

        initTime = hour*60 + minute
        endTime = initTime + duration

        endMinute = endTime%60
        endHour = int(endTime/60) % 24

        self.outHour.configure(state = 'normal')
        self.outMinute.configure(state = 'normal')

        self.outHour.delete(0,END)
        self.outHour.insert(0, str(endHour))
        
        self.outMinute.delete(0,END)
        self.outMinute.insert(0, str(endMinute))
  
        self.outHour.configure(state = 'disabled')
        self.outMinute.configure(state = 'disabled')

root = Tk()
app = Application(root)
root.bind('<Return>', app.getOutTime)
root.title("Controle de Ponto")
try:
    root.call('wm', 'iconphoto', root._w, PhotoImage(file='favicon/time2.PNG'))
except:
    pass
root.minsize(250,250)
root.maxsize(250,300)
root.mainloop()
