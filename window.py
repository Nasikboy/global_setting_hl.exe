from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox as mb

class Winw(object):


 def window(self):
  self.root = Tk()
  self.root.title("Embodiment Half-life 1")
  self.root.geometry("400x300")


  path = Button(self.root,text = 'Путь к файлу к игре',command = windows_start.path_open).grid(row=1,column=0)
  Bunny_Hop = Checkbutton(self.root,text ='Подключить Bunny Hop')
  Bunny_Hop.grid(row=2,column=0)

  Jump_up = Checkbutton(self.root,text = 'Прыжок на колёсико вверх')
  Jump_up.grid(row=3, column=0)
  Jump_down = Checkbutton(self.root,text = 'Прыжок на колёсико вниз')
  Jump_down.grid(row=4, column=0)

  self.root.mainloop()


 def path_open(self):
    path = filedialog.askdirectory()
    path_hl = path + '/hl.exe'
    try:
        f = open(path_hl)
        f.close()
        path_label = Label(self.root,text = path).grid(row=1,column=1)
    except FileNotFoundError:
        mb.showerror("Внимание", "Вы указали неправильный путь к игре!")


#--- окно запуска
windows_start = Winw()




windows_start.window()