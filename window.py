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



  var = IntVar()


  path = Button(self.root,text = 'Путь к файлу к игре',command = windows_start.path_open).grid(row=1,column=0)
  self.Bunny_Hop = Checkbutton(self.root,text ='Подключить Bunny Hop', variable=var)
  self.Bunny_Hop.grid(row=2,column=0)

  self.Jump_up = Checkbutton(self.root,text = 'Прыжок на колёсико вверх')
  self.Jump_up.grid(row=3, column=0)
  self.Jump_down = Checkbutton(self.root,text = 'Прыжок на колёсико вниз')
  self.Jump_down.grid(row=4, column=0)
  self.speed = Checkbutton(self.root, text='Ускорение Фримена').grid(row=5,column=0)
  self.FPS = Checkbutton(self.root, text='Установка бинда на фпс = 20/100').grid(row=6, column=0)
  lbl_fps20 = Label(self.root,text = 'Кнопка для 20fps = ').grid(row=6,column = 1)
  lbl_fps100 = Label(self.root, text='Кнопка для 100fps = ').grid(row=6, column=3)
  self.FPS20 = Entry(self.root,width = 5).grid(row=6, column=2)
  self.FPS100 = Entry(self.root,width = 5).grid(row=6, column=4)
  self.FPS_show = Checkbutton(self.root, text='Установка счётчика ФПС').grid(row=7, column=0)
  self.game_player = Checkbutton(self.root, text='Отдаление экрана от рук персонажа').grid(row=7, column=0)
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
     os.rename(papa + 'autoexec.cfg', papa + 'autoexec.txt')
     ready_autoexec = open(papa+'autoexec.txt',"r")
     ready_config = open(papa + 'config.txt',"r")
     bh_txt = 'alias "dj" "+jump;wait;-jump;wait;special"'

     if self.Bunny_Hop.select:

             str_abort = ""
             for line in ready_autoexec.readlines():
                 if bh_txt in line:
                     str_abort = "ok"
                 if str_abort == "":
                     with open(papa+'autoexec.txt', 'a', encoding='utf-8') as f:
                         f.write('alias "dj" "+jump;wait;-jump;wait;special"' + '\n')
                         f.write('alias "+dj" "alias _special dj; dj"'+ '\n')
                         f.write('alias "-dj" "alias _special"'+ '\n')
                         f.write('bind SPACE "+dj'+ '\n')
                     with open(papa + 'config.txt', 'a', encoding='utf-8') as f:
                         f.write('exec autoexec.cfg'+ '\n')
                     ready_autoexec.close()
                     ready_config.close()

     os.rename(papa + 'config.txt', papa + 'config.cfg')
     os.rename(papa + 'autoexec.txt', papa + 'autoexec.cfg')

#     for line in ready.readlines():
 #        print(line)







#--- окно запуска
windows_start = Winw()




windows_start.window()
