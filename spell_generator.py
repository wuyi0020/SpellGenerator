from cProfile import label
from genericpath import isfile
from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import os
import tkinter.font as Tkfont
from xml.etree.ElementTree import tostring




def load_spell_list(path):
    file = open(path, encoding="utf-8")
    word_list = []
    for line in file.readlines():
        line = line.replace('\n', '')
        word_list.append(line)
    file.close()
    return word_list

class Gui_helper_main:
    def __init__(self):
        self.root = Tk()
        self.frame = None
        self.frame_index = 0
        WinW = 800
        WinH = 800
        ScrW = (self.root.winfo_screenwidth()/2)-(WinW/2)
        ScrH = (self.root.winfo_screenheight()/2)-(WinH/2)
        
        
        
        self.root.geometry('%dx%d+%d+%d'%(WinW,WinH,ScrW,ScrH))
        self.root.title('Spell generator咒語生成器')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

        
        
        # maker info
        self.maker_name = Label(self.root, text="Maker : JingShing,UI : Wuyi0020")
        

        self.maker_name.grid(column=0, row=7, sticky=N+W)
        


        self.frames = [page_module(self)]
        self.switch_frame(0)
        
    def switch_frame(self, index):
        if self.frame is not None:
            self.frame.grid_forget()
        self.frame_index = index
        self.frame = self.frames[self.frame_index]
        self.frame.grid(column=0, row=0, sticky=N+W)

    def run(self):
        self.root.mainloop()

    def quit(self):
        if messagebox.askyesno('Confirm','Are you sure you want to quit?'):
            self.root.quit()

class page_module(Frame):
    def __init__(self, master):
        Frame.__init__(self, master = master.root)
        self.main = master
        self.master = master.root
        self.data_list = []
        if os.path.isfile('word.txt'):
            self.data_list = load_spell_list('word.txt').copy()
        self.spellEn = ''
        self.spellCh = ''
        self.spellTuple = []
        self.TextEnList =[]

        self.spellEnList = []
        self.spellChList = []
        for i in self.data_list:
            
            self.spellChList.append(i.split(':')[0]) 
            self.spellEnList.append(i.split(':')[-1])

            


        dfont = Tkfont.nametofont("TkDefaultFont")
        default_font2 =Tkfont.nametofont("TkTextFont")
        default_font3 =Tkfont.nametofont("TkFixedFont")
        dfont.configure(size=16)
        default_font2.configure(size=16)
        default_font3.configure(size=16)
        #self.L1 = Button(self, text="英文",command=self.CheckChange)
        self.L1 = Label(self, text="英文")
        self.L2 = Label(self, text="中文")
        
        
        
        
        self.spawn_result = Listbox(self,width=30,  height=10,font=dfont)
        self.spawn_result.bind('<Double-1>',self.del_word)
        self.spawn_result2 = Listbox(self,width=30,  height=10,font=dfont)
        self.spawn_result2.bind('<Double-1>',self.del_wordCH)
        #self.change_button=Button(self,text="->\n更改\n<-",command=self.CheckChange)
        #self.change_button.grid(column=1,row=2)
        
        

        self.word_list = Listbox(self,  height=10)
        self.load_list()
        self.word_list.bind('<Double-1>', self.add_word)
        self.clear_button = Button(self, text='clear', command=self.clear_word)
        self.copy_button = Button(self, text='copy', command=self.copy_word)
        
        self.back_button = Button(self, text='backspace', command=self.back_word)
        self.import_button = Button(self, text='import', command=self.import_set)


        self.L1.grid(column=0, row=1, padx=20)
        self.L2.grid(column=1, row=1, padx=20)
        #self.L2.grid(column=2, row=1, padx=20)

        self.spawn_result.grid(column=0, row=2, padx=10,pady=10)
        self.spawn_result2.grid(column=1, row=2, padx=10,pady=10)
        #self.spawn_result2.grid(column=2, row=2, padx=10,pady=10)
        
        self.clear_button.grid(column=0, row=3, sticky=W+E,padx=10)
        self.back_button.grid(column=1, row=3, sticky=W+E,padx=10)
        
        self.copy_button.grid(column=0, row=4,columnspan=2, sticky=W+E,padx=10)

        self.word_list.grid(column=0, row=5,columnspan=2, sticky=N+W+E,padx=20,pady=10)

        self.import_button.grid(column=0, row=6,columnspan=2, sticky=N+W+E,padx=10)
        

    def add_word(self, event):
        #self.CheckChange()
        _newselect=self.word_list.curselection()[0]
        if ':' in self.data_list[_newselect]:
            self.spellTuple.append(_newselect)
            self.TextEnList.append(self.data_list[_newselect].split(':')[0])
            print(self.data_list[_newselect])
            
            
            if self.spellEn == '':
                print('新增單字%s'%self.data_list[_newselect].split(':')[-1])
                self.spawn_result.insert(END,"%s, "%self.data_list[_newselect].split(':')[-1])
                self.spawn_result2.insert(END,"%s, "%self.data_list[_newselect].split(':')[0])
                #self.spellEn += self.data_list[_newselect].split(':')[-1]
                #self.spellCh += self.data_list[_newselect].split(':')[0]
            else:
                print('新增單字%s'%self.data_list[_newselect].split(':')[-1])
                self.spawn_result.insert(END,"%s, "%self.data_list[_newselect].split(':')[-1])
                self.spawn_result2.insert(END,"%s, "%self.data_list[_newselect].split(':')[0])
                #self.spellEn += ', ' + self.data_list[_newselect].split(':')[-1]
                #self.spellCh += ', ' + self.data_list[_newselect].split(':')[0]
                

            #print(self.spellTuple)
            #print(self.spellList)
            print("新字串:%s\n"%self.spellEn)
            #self.spawn_result.delete(1.0, 'end')
            #self.spawn_result.insert(END, self.spellEn)
            #self.spawn_result2.delete(1.0, 'end')
            #self.spawn_result2.insert(END, self.spellCh)

    def del_word(self,event):
        delword = self.spawn_result.curselection()[0]
        s=self.spawn_result.get(delword)
        print('刪除字串:%s'%s)
        self.spawn_result.delete(delword)
        self.spawn_result2.delete(delword)

    def del_wordCH(self,event):
        delword = self.spawn_result2.curselection()[0]
        s=self.spawn_result2.get(delword)
        print('刪除字串:%s'%s)
        self.spawn_result.delete(delword)
        self.spawn_result2.delete(delword)
        

    def CheckChange(self):
        TextNow=self.spawn_result.get(1.0, 'end-1c')
        TextNowList=TextNow.split(', ')
        print("現在文字:%s"%TextNowList)
        EnList=self.spellEn.split(', ')
        print("原字串:%s"%EnList)
        
        J=0
        changepoint=[]
        if  EnList != TextNowList:
            
            print("英文有變動\n")
            for i in EnList:
                if i != TextNowList[J]:
                    print('變動位置%s'%J)
                J=J+1
            
        else:
            print("英文沒變動\n")
        #if changepoint != 9999:
            #print(self.spellTuple)
            #print(self.spellTuple[changepoint])

            
        

    def clear_word(self):
        self.spellEn = ''
        self.spellCh = ''
        self.spawn_result.delete(0,END)
        self.spawn_result2.delete(0,END)

    def copy_word(self):
        self.clipboard_clear()
        s=self.spawn_result.get(0,END)
        K=''.join(s)
        self.clipboard_append(K)
        
    def back_word(self):
        lis = self.spellEn.split(', ')
        lis2 = self.spellCh.split(', ')
        del lis[-1]
        del lis2[-1]
        self.spellEn = ", ".join(lis)
        self.spellCh = ", ".join(lis2)
        self.spawn_result.delete(1.0, 'end')
        self.spawn_result.insert(END, self.spellEn)
        self.spawn_result2.delete(1.0, 'end')
        self.spawn_result2.insert(END, self.spellCh)
        

    def import_set(self):
        set_path = filedialog.askopenfilename()
        if set_path:
            print('導入')
            self.word_list.delete(0, END)
            self.data_list.clear()
            self.data_list = load_spell_list(set_path).copy()
            self.load_list()

    def load_list(self):
        for word in self.data_list:
            self.word_list.insert(END, word)

main = Gui_helper_main()
main.run()