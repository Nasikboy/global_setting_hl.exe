from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox as mb
import wx

class Winw(object):


 def window(self):
  self.root = Tk()
  self.root.title("Embodiment Half-life 1")
  self.root.geometry("750x300")

  sq_fit_size = 300






  path = Button(self.root,text = 'Путь к файлу к игре',command = windows_start.path_open).grid(row=1,column=0)
  Bunny_Hop = Checkbutton(self.root,text ='Подключить Bunny Hop')
  Bunny_Hop.grid(row=2,column=0)

  Jump_up = Checkbutton(self.root,text = 'Прыжок на колёсико вверх')
  Jump_up.grid(row=3, column=0)
  Jump_down = Checkbutton(self.root,text = 'Прыжок на колёсико вниз')
  Jump_down.grid(row=4, column=0)
  speed = Checkbutton(self.root, text='Ускорение Фримена').grid(row=5,column=0)
  FPS = Checkbutton(self.root, text='Установка бинда на фпс = 20/100').grid(row=6, column=0)
  lbl_fps20 = Label(self.root,text = 'Кнопка для 20fps = ').grid(row=6,column = 1)
  lbl_fps100 = Label(self.root, text='Кнопка для 100fps = ').grid(row=6, column=3)
  FPS20 = Entry(self.root,width = 5).grid(row=6, column=2)
  FPS100 = Entry(self.root,width = 5).grid(row=6, column=4)
  FPS_show = Checkbutton(self.root, text='Установка счётчика ФПС').grid(row=7, column=0)
  game_player = Checkbutton(self.root, text='Отдаление экрана от рук персонажа').grid(row=7, column=0)
  Start_script = Button(self.root, text='Выполнение выбранных действий',width=55,height = 5,background = 'aqua',command = windows_start.joint).grid(row=8, column=0)
  self.root.mainloop()


 def path_open(self):
    self.path = filedialog.askdirectory()
    path_hl = self.path + '/hl.exe'
    try:
        f = open(path_hl)
        f.close()
        path_label = Label(self.root,text = self.path).grid(row=1,column=1)
    except FileNotFoundError:
        mb.showerror("Внимание", "Вы указали неправильный путь к игре!")
 def joint(self):
     try:
      self.pathcfg = str(self.path + "/valve/config.cfg")
      papa = self.path + "/valve/"
     except FileNotFoundError:
      mb.showerror("У вас нету файла с конфигурацией (в будущем добавим восстановление конфигурации)")
     os.rename(papa + 'config.cfg', papa + 'config.txt')
     ready = open(papa + 'config.txt',"w")

     for line in ready.readlines():
         print(line)






#--- окно запуска
windows_start = Winw()




windows_start.window()
