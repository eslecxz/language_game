from tkinter import *


class GUI:
    def __init__(self):
        self.root = Tk()
        self.width = 1280
        self.height = 720
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.title('Game for learn language')

        self.meny = MyMeny(self)
        self.add = MyFrame(self)
        self.ru = MyRu(self)
        self.eng = MyEng(self)
        self.game = MyFrame(self)
        self.meny.frame.pack()

    def mainloop(self):
        self.root.mainloop()


class MyFrame:
    def __init__(self, gui: GUI):
        self.gui = gui
        self.frame = Frame(self.gui.root, width=self.gui.width, height=self.gui.height, background='red')
        self.button = Button(self.frame, text='закрыть', font=('Roboto', 20), bg='pink',
                             fg='black', command=self.button_click)
        self.button.place(x=1100, y=20)

    def open_words(self):
        self.ru_words = []
        self.eng_words = []
        file = open('/Users/ana/Desktop/language_game/words.txt', 'r', encoding='UTF-8')
        file_list = [line.strip() for line in file]
        for el in file_list:
            self.ru_words.append(el.split()[0])
            self.eng_words.append(el.split()[1])

    def pack_forget(self):
        self.frame.pack_forget()

    def button_click(self):
        self.frame.pack_forget()
        self.gui.ru.initial_constants()
        self.gui.meny.frame.pack()

    def open_words(self):
        self.ru_words = []
        self.eng_words = []
        file = open('/Users/ana/Desktop/language_game/words.txt', 'r', encoding='UTF-8')
        file_list = [line.strip() for line in file]
        for el in file_list:
            self.ru_words.append(el.split()[0])
            self.eng_words.append(el.split()[1])


class MyMeny(MyFrame):
    def __init__(self, gui:GUI):
        super().__init__(gui)

        self.btn_add = Button(self.frame, text='add', font=('Roboto', 20), bg='pink', fg='black', command=self.open_add)
        self.btn_add.place(x=20, y=10, width=1200, height=60)

        self.btn_ru = Button(self.frame, text='ru', font=('Roboto', 20), bg='pink', fg='black', command=self.open_ru)
        self.btn_ru.place(x=20, y=60,  width = 300, height=600)

        self.btn_eng = Button(self.frame, text='eng', font=('Roboto', 20), bg='pink', fg='black', command=self.open_eng)
        self.btn_eng.place(x=360, y=60,  width=300, height=600)

        self.btn_game = Button(self.frame, text='game', font=('Roboto', 20), bg='pink', fg='black', command=self.open_game)
        self.btn_game.place(x=740, y=60,  width=300, height=600)

    def open_add(self):
        self.gui.add.frame.pack()
        self.gui.add.open_words()
        self.gui.meny.pack_forget()

    def open_ru(self):
        self.gui.ru.frame.pack()
        self.gui.ru.open_words()
        self.gui.ru.initial_constants()
        self.gui.ru.label['text'] = self.gui.ru.ru_words[0]
        self.gui.meny.pack_forget()



    def open_eng(self):
        self.gui.game.frame.pack()
        self.gui.eng.open_words()
        self.gui.eng.initial_constants()
        self.gui.eng.label['text'] = self.gui.eng.ru_words[0]
        self.gui.meny.pack_forget()

    def open_game(self):
        self.gui.game.frame.pack()
        self.gui.game.open_words()
        self.gui.meny.pack_forget()

class MyRu(MyFrame):
    def __init__(self, gui:GUI):
        super().__init__(gui)

        self.label = Label(self.frame, text='', font=('Roboto', 50), bg='purple', fg='black')
        self.label.place(x=40, y=40, width=1000, height=100)

        self.entry = Entry(self.frame, font=('Roboto', 50), bg='pink', fg='black')
        self.entry.place(x=295, y=320)

        self.btn_ru_done = Button(self.frame, text='готовенько!', font=('Roboto', 70), bg='pink', fg='black', command=self.go)
        self.btn_ru_done.place(x=40, y=140, width=1000, height=180)

        self.label_otvet = Label(self.frame, text='ждем твой ответ:)', font=('Roboto', 48), bg='white', fg='black')
        self.label_otvet.place(x=40, y=400, width=1000, height=200)

        self.label_cnt = Label(self.frame, text='твой счет', font=('Roboto', 35), bg='purple', fg='black')
        self.label_cnt.place(x=40, y=320, width=255, height=80)


    def initial_constants(self):
        self.cnt_word = 0
        self.cnt_on_cnt = 0

    def go(self):
        self.go_2()
        if self.entry.get() == '':
            return

        self.entry.delete(0, END)
        self.cnt_word += 1
        self.label['text'] = self.ru_words[self.cnt_word % len(self.ru_words)]

    def go_2(self):
        if self.btn_ru_done['text'] == 'eng':
            self.list = self.ru_words
        else:
            self.list = self.eng_words
        if self.list[self.cnt_word % len(self.list)] == self.entry.get().lower():
            self.label_otvet['text'] = 'Молодец!Все верно!'
            self.cnt_on_cnt += 1
        elif self.entry.get() == '':
            self.label_otvet['text'] = 'Если не знаешь ответа, введи хоть что-нибудь'
        else:
            self.label_otvet['text'] = 'Подумай лучше, ты был не прав!'
            self.cnt_on_cnt -= 1
        self.cnt_print()

    def cnt_print(self):
        self.label_cnt['text'] = self.cnt_on_cnt


class MyEng(MyRu):
    def __init__(self, myru: MyRu):
        super().__init__(myru)



win_1 = GUI()
win_1.mainloop()