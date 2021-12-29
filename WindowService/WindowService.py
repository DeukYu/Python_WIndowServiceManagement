import tkinter

window=tkinter.Tk()
window.title("WIndowManagement")
window.geometry("640x400+100+100")
window.resizable(False, False)

def RegisterService():
    ButtonWindow=tkinter.Tk()
    ButtonWindow.title("Service Registration")

def ExcuteService():
    ButtonWindow=tkinter.Tk()
    ButtonWindow.title("Service Excute")
 
def StopService():
    ButtonWindow=tkinter.Tk()
    ButtonWindow.title("Service Excute")

RegisterButton = tkinter.Button(window,text="Service Registration", command=RegisterService)
RegisterButton.pack()

ExcuteButton = tkinter.Button(window, text="Service Excute", command=ExcuteService)
ExcuteButton.pack()

StopButton = tkinter.Button(window, text="Service Stop", command=StopService)
StopButton.pack()

window.mainloop()