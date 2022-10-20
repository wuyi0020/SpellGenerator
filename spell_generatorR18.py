from genericpath import isfile
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import os

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
        self.root.geometry('800x600')
        self.root.title('Spell generator咒語生成器')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        
        # maker info
        self.maker_name = Label(self.root, text="Maker : JingShing,UI : Wuyi0020")
        

        self.maker_name.grid(column=0, row=6, sticky=N+W)
        


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
        if os.path.isfile('R18word.txt'):
            self.data_list = load_spell_list('R18word.txt').copy()
        self.spell = ''
        self.spell2 = ''

        self.L1 = Label(self, text="英文")
        self.L2 = Label(self, text="中文")
        self.spawn_result = Text(self,width=50,  height=10)
        self.spawn_result2 = Text(self,width=50,  height=10)
        self.word_list = Listbox(self,  height=20)
        self.load_list()
        self.word_list.bind('<Double-1>', self.add_word)
        self.clear_button = Button(self, text='clear', command=self.clear_word)
        self.copy_button = Button(self, text='copy', command=self.copy_word)
        self.back_button = Button(self, text='backspace', command=self.back_word)
        self.import_button = Button(self, text='import', command=self.import_set)


        self.L1.grid(column=0, row=1, sticky=S+W+E,padx=20)
        self.L2.grid(column=1, row=1, sticky=S+W+E,padx=20)

        self.spawn_result.grid(column=0, row=2, sticky=N+W+E,padx=20,pady=10)
        self.spawn_result2.grid(column=1, row=2, sticky=N+W+E,padx=20,pady=10)
        
        self.clear_button.grid(column=0, row=3, sticky=N+W+E,padx=10)
        self.copy_button.grid(column=2, row=3, sticky=N+W+E,padx=10)
        self.back_button.grid(column=1, row=3, sticky=N+W+E,padx=10)

        self.word_list.grid(column=0, row=4,columnspan=3, sticky=N+W+E,padx=20,pady=10)

        self.import_button.grid(column=0, row=5,columnspan=3, sticky=N+W+E,padx=10)
        

    def add_word(self, event):
        if ':' in self.data_list[self.word_list.curselection()[0]]:
            if self.spell == '':
                self.spell += self.data_list[self.word_list.curselection()[0]].split(':')[-1]
                self.spell2 += self.data_list[self.word_list.curselection()[0]].split(':')[0]
            else:
                self.spell += ', ' + self.data_list[self.word_list.curselection()[0]].split(':')[-1]
                self.spell2 += ', ' + self.data_list[self.word_list.curselection()[0]].split(':')[0]
            self.spawn_result.delete(1.0, 'end')
            self.spawn_result.insert(END, self.spell)
            self.spawn_result2.delete(1.0, 'end')
            self.spawn_result2.insert(END, self.spell2)

    def clear_word(self):
        self.spell = ''
        self.spell2 = ''
        self.spawn_result.delete(1.0, 'end')
        self.spawn_result2.delete(1.0, 'end')

    def copy_word(self):
        self.clipboard_clear()
        self.clipboard_append(self.spawn_result.get(1.0, 'end-1c'))
        
    def back_word(self):
        lis = self.spell.split(', ')
        lis2 = self.spell2.split(', ')
        del lis[-1]
        del lis2[-1]
        self.spell = ", ".join(lis)
        self.spell2 = ", ".join(lis2)
        self.spawn_result.delete(1.0, 'end')
        self.spawn_result.insert(END, self.spell)
        self.spawn_result2.delete(1.0, 'end')
        self.spawn_result2.insert(END, self.spell2)
        

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