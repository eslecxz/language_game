import random
import time


def open_words():
    global ru_words, eng_words
    ru_words = []
    eng_words = []
    file = open('/Users/ana/Desktop/language_game/words.txt', 'r', encoding='UTF-8')
    file_list = [line.strip() for line in file]
    for el in file_list:
        ru_words.append(el.split()[0])
        eng_words.append(el.split()[1])


def close():
    frame_ru.pack_forget()
    frame_eng.pack_forget()
    frame_game.pack_forget()
    frame_add.pack_forget()
    frame_perevod.pack_forget()
    frame_menu.pack()


def btn_ru_open_click():
    frame_menu.pack_forget()
    frame_ru.pack()


def btn_eng_open_click():
    frame_menu.pack_forget()
    frame_eng.pack()


def btn_game_open_click():
    frame_menu.pack_forget()
    frame_game.pack()
    update_btns()


def btn_add_open_click():
    frame_menu.pack_forget()
    frame_add.pack()


# Frame Ru Fucntions Start
def word():
    global cnt
    open_words()
    otvet()
    if entry_ru.get() == '':
        return

    entry_ru.delete(0, END)
    cnt += 1
    label_ru['text'] = ru_words[cnt % len(ru_words)]


def otvet():
    open_words()
    global CntTrue
    if btn_ru_done['text'] == 'eng':
        local_list = ru_words
    else:
        local_list = eng_words
    if local_list[cnt % len(local_list)] == entry_ru.get().lower():
        label_ru_otvet['text'] = 'Молодец!Все верно!'
        CntTrue += 1
    elif entry_ru.get() == '':
        label_ru_otvet['text'] = 'Если не знаешь ответа, введи хоть что-нибудь'
    else:
        label_ru_otvet['text'] = 'Подумай лучше, ты был не прав!'
        CntTrue -= 1

    label_ru_cnt_click()


def label_ru_cnt_click():
    label_ru_cnt['text'] = CntTrue


# Frame Ru Fucntions End

# Frame Eng Fucntions Start
def word1():
    global cnt
    open_words()
    otvet1()
    if entry_eng.get() == '':
        return

    entry_eng.delete(0, END)
    cnt += 1
    label_eng['text'] = eng_words[cnt % len(ru_words)]


def otvet1():
    open_words()
    global CntTrue1
    if btn_eng_done['text'] == 'eng':
        local_list = eng_words
    else:
        local_list = ru_words
    if local_list[cnt % len(local_list)] == entry_eng.get().lower():
        label_eng_otvet['text'] = 'Молодец!Все верно!'
        CntTrue1 += 1
    elif entry_eng.get() == '':
        label_eng_otvet['text'] = 'Если не знаешь ответа, введи хоть что-нибудь'
    else:
        label_eng_otvet['text'] = 'Подумай лучше, ты был не прав!'
        CntTrue1 -= 1

    label_eng_cnt_click()


def label_eng_cnt_click():
    label_eng_cnt['text'] = CntTrue1


# Frame End Fucntions End


# Frame Add Fucntions Start
def btn_add():
    if entry_add_2.get() == '' or entry_add_1.get() == '':
        return

    open_words()
    file = open('words.txt', 'a', encoding='UTF-8')
    file.write(entry_add_1.get() + ' ' + entry_add_2.get() + '\n')
    file.close()
    entry_add_1.delete(0, END)
    entry_add_2.delete(0, END)


# Frame Add Fucntions End

# Frame Game Fucntions Start
click = 0
cnt_letter = 0
prav = True


def btn_click(button: Button):
    cnt_letter = 0
    prav = True
    global click, original_word, cnt_word
    print('вы нажали на кнопку', button['text'])
    if button['text'] == original_word[cnt_letter]:
        button.place(x=(WIDTH - (len(eng_words[cnt_word]) * 50))//2 + 50*cnt_letter, y=300)
        cnt_letter += 1
        click += 1
    else:
        prav = False
        button['background'] = 'red'
        root.update()
        time.sleep(0.5)
        button['background'] = 'pink'
        root.update()
        time.sleep(0.5)
        button['background'] = 'red'
        root.update()
        time.sleep(0.5)
        button['background'] = 'pink'
        root.update()
        time.sleep(0.5)
    if len(original_word) - 1 == cnt_letter - 1:
        cnt_word += 1
        perevorot()


def perevorot():
    global eng_word_1, original_word, cnt_game, btn
    label_game_btn_perevod['text'] = ru_words[cnt_word]
    original_word = eng_words[cnt_word]
    shuffle_word(original_word)
    update_btns()


    cnt_letter = 0


def update_btns():
    global eng_word_1, cnt_game, btns, cnt_letter
    for i in btns:
        i.destroy()
    cnt_letter = 0
    for i in range(len(eng_word_1)):
        btn = Button(frame_game, text=eng_word_1[i], font=('Roboto', 20), bg='pink', fg='black')
        btn.place(x=(WIDTH - (len(eng_words[cnt_word]) * 50))//2 + 50*cnt_letter, y=500, width=50, height=50)
        btn.configure(command=lambda btn=btn: btn_click(btn))
        btns.append(btn)
        cnt_game += 1
        cnt_letter += 1


def shuffle_word(word: str) -> str:
    list_word = list(word)
    random.shuffle(list_word)
    word = ''.join(list_word)
    return word


# Frame Game Fucntions End

# Постоянные величины
WIDTH = 1080
HEIGHT = 720
config = {
    "font": ('Roboto', 60),
    "fg": 'black',
}
pc = '#F07DE2'
blc = '#0300F0'
fic = '#E5C8EA'
fic_2 = '#BC1AEB'
cnt = 0
CntTrue = 0
ru_words = []
eng_words = []
CntTrue1 = 0
# Создаем основное окно
root = Tk()
root.title('Приложение для изучения слов')
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

# Создаем дополнительные фреймы
frame_menu = Frame(root, width=WIDTH, height=HEIGHT, background=fic_2)
frame_ru = Frame(root, width=WIDTH, height=HEIGHT, background=fic_2)
frame_eng = Frame(root, width=WIDTH, height=HEIGHT, background=fic_2)
frame_game = Frame(root, width=WIDTH, height=HEIGHT, background=fic_2)
frame_add = Frame(root, width=WIDTH, height=HEIGHT, background=fic_2)
frame_perevod = Frame(frame_game, width=WIDTH, height=HEIGHT, background=fic_2)

# frame_menu start
frame_game.pack()
btn_ru_open = Button(frame_menu, text='ru', cnf=config, command=btn_ru_open_click)
btn_ru_open.place(x=20, y=60, width=300, height=600)

btn_eng_open = Button(frame_menu, text='eng', cnf=config, command=btn_eng_open_click)
btn_eng_open.place(x=380, y=60, width=300, height=600)

btn_game_open = Button(frame_menu, text='game', cnf=config, command=btn_game_open_click)
btn_game_open.place(x=740, y=60, width=300, height=600)

btn_add_open = Button(frame_menu, text='add', cnf=config, command=btn_add_open_click)
btn_add_open.place(x=20, y=10, width=1020, height=60)

# frame_menu end
btn_ru_close = Button(frame_ru, text='назад', font=('Roboto', 10), cnf=config, command=close)
btn_ru_close.place(x=1040, y=0, width=40, height=40)

btn_eng_close = Button(frame_eng, text='назад', font=('Roboto', 10), cnf=config, command=close)
btn_eng_close.place(x=1040, y=0, width=40, height=40)

btn_game_close = Button(frame_game, text='назад', font=('Roboto', 10), cnf=config, command=close)
btn_game_close.place(x=1040, y=0, width=40, height=40)

btn_add_close = Button(frame_add, text='назад', font=('Roboto', 10), cnf=config, command=close)
btn_add_close.place(x=1040, y=0, width=40, height=40)

btn_perevod_close = Button(frame_perevod, text='назад', font=('Roboto', 10), cnf=config, command=close)
btn_perevod_close.place(x=1040, y=0, width=40, height=40)

# Frame Ru Start
open_words()
label_ru = Label(frame_ru, text=ru_words[cnt % len(ru_words)], font=('Roboto', 50), bg=pc, fg='black')
label_ru.place(x=40, y=40, width=1000, height=100)

entry_ru = Entry(frame_ru, font=('Roboto', 50), bg=fic, fg='black')
entry_ru.place(x=295, y=320)

btn_ru_done = Button(frame_ru, text='готовенько!', font=('Roboto', 70), bg=fic, fg='black', command=word)
btn_ru_done.place(x=40, y=140, width=1000, height=180)

label_ru_otvet = Label(frame_ru, text='ждем твой ответ:)', font=('Roboto', 48), bg='white', fg='black')
label_ru_otvet.place(x=40, y=400, width=1000, height=300)

label_ru_cnt = Label(frame_ru, text='твой счет', font=('Roboto', 35), bg=pc, fg='black')
label_ru_cnt.place(x=40, y=320, width=255, height=80)
# Frame Ru End

# Frame Eng Start
label_eng = Label(frame_eng, text=eng_words[cnt % len(eng_words)], font=('Roboto', 50), bg=pc, fg='black')
label_eng.place(x=40, y=40, width=1000, height=100)

entry_eng = Entry(frame_eng, font=('Roboto', 50), bg=fic, fg='black')
entry_eng.place(x=295, y=320)

btn_eng_done = Button(frame_eng, text='готовенько!', font=('Roboto', 70), bg=fic, fg='black', command=word1)
btn_eng_done.place(x=40, y=140, width=1000, height=180)

label_eng_otvet = Label(frame_eng, text='ждем твой ответ:)', font=('Roboto', 48), bg='white', fg='black')
label_eng_otvet.place(x=40, y=400, width=1000, height=300)

label_eng_cnt = Label(frame_eng, text='твой счет', font=('Roboto', 35), bg=pc, fg='black')
label_eng_cnt.place(x=40, y=320, width=255, height=80)
# Frame Eng End

# Frame Add Start
label_add = Label(frame_add, text='Введи в первую строку русское слово, а во вторую английское', font=('Roboto', 30),
                  bg=pc, fg='black')
label_add.place(x=40, y=40, width=1000, height=100)

label_add_1 = Label(frame_add, text='1.', font=('Roboto', 50), bg=pc, fg='black')
label_add_1.place(x=170, y=315, width=100, height=80)

label_add_2 = Label(frame_add, text='2.', font=('Roboto', 50), bg=pc, fg='black')
label_add_2.place(x=170, y=415, width=100, height=80)

entry_add_1 = Entry(frame_add, font=('Roboto', 50), bg=pc, fg='black')
entry_add_1.place(x=295, y=320)

entry_add_2 = Entry(frame_add, font=('Roboto', 50), bg=pc, fg='black')
entry_add_2.place(x=300, y=420)

btn_add_done = Button(frame_add, text='готовенько!', font=('Roboto', 70), bg=fic, fg='black', command=btn_add)
btn_add_done.place(x=40, y=530, width=1000, height=140)
# Frame Add Rnd

# Frame Game Fucntions Start
cnt_game = 1
open_words()
cnt_word = 0
original_word = eng_words[cnt_word]
eng_word_1 = shuffle_word(original_word)

btns = []

label_game_cnt = Label(frame_game, text='твой счет правильных ответов', font=('Roboto', 40), bg='pink', fg='black')
label_game_cnt.place(x=130, y=150, width=700, height=100)

btn_game = Button(frame_game, text='подсказка', font=('Roboto', 8), cnf=config, bg='yellow')
btn_game.place(x=0, y=0, width=60, height=60)

label_game_btn_perevod = Label(frame_game, text=ru_words[cnt_word], font=('Roboto', 30), bg='pink', fg='black')
label_game_btn_perevod.place(x=650, y=550, width=300, height=50)
open_words()

# Frame  Game Fucntions End

root.mainloop()








from tkinter import *


def delet_bnt1():
    frame_meny.pack_forget()
    frame_ru_eng.pack()

def delet_bnt2():
    frame_meny.pack_forget()
    frame_eng_ru.pack()

def delet_bnt3():
    frame_meny.pack_forget()
    frame_game.pack()

def delet_btn10():
    frame_meny.pack_forget()
    frame_dobav.pack()

def perehod_btn4():
    frame_game.pack_forget()
    frame_meny. pack()

def perehod_btn5():
    frame_eng_ru.pack_forget()
    frame_meny. pack()


def perehod_btn6():
    frame_ru_eng.pack_forget()
    frame_meny. pack()

def perehod_btn11():
    frame_dobav.pack_forget()
    frame_meny. pack()



def word():
    open_words()
    global cnt
    otvet()
    TextInput.delete(0, END)
    cnt += 1
    SomeLabel['text'] = slovo[cnt%len(slovo)]


def word1():
    open_words()
    global cnt
    otvet1()
    TextInput1.delete(0, END)
    cnt += 1
    SomeLabel1['text'] = perevod[cnt%len(slovo)]



def otvet():
    open_words()
    global CntTrue
    if btn8['text'] == 'eng':
        local_list = slovo
    else:
        local_list = perevod
    if local_list[cnt%len(local_list)] == TextInput.get().lower():
            otvetka['text'] = 'Молодец!Все верно!'
            CntTrue += 1
    else:
            otvetka['text'] = 'Подумай лучше, ты был не прав!'
            CntTrue -= 1

    cnt3()


def otvet1():
    open_words()
    global CntTrue1
    if btn9['text'] == 'eng':
        local_list = perevod
    else:
        local_list = slovo
    if local_list[cnt%len(local_list)] == TextInput1.get().lower():
            otvetka1['text'] = 'Молодец!Все верно!'
            CntTrue1 += 1
    else:
            otvetka1['text'] = 'Подумай лучше, ты был не прав!'
            CntTrue1 -= 1


    cnt3_1()

def cnt3_1():
    cnt_true1['text'] = CntTrue1

def cnt3():
    cnt_true['text'] = CntTrue


def del_btn_12():
    if TextInput3.get() or TextInput2.get() == '':
        print('error')

    open_words()
    file = open('/Users/ana/Desktop/language_game/words.txt', 'a', encoding='UTF-8')
    file.write(TextInput2.get() + ' ' + TextInput3.get() + '\n')
    file.close()
    TextInput2.delete(0, END)
    TextInput3.delete(0, END)




pc = '#F07DE2'
blc = '#0300F0'
fic ='#E5C8EA'
fic_2 = '#BC1AEB'
cnt = 0
cnt_2 = 1
CntTrue = 0
CntTrue1 = 0

slovo = []
perevod = []

def open_words():
    global slovo, perevod
    slovo = []
    perevod = []
    file = open('/Users/ana/Desktop/language_game/words.txt', 'r', encoding ='UTF-8')
    file_list = [line.strip() for line in file]
    for el in file_list:
        print(el.split())
        slovo.append(el.split()[0])
        perevod.append(el.split()[1])


root = Tk()
root.title('Приложение для изучения слов')
root.geometry('1080x720')






frame_meny = Frame(root,width=1080, height=720, background='red')
frame_dobav = Frame(root,width=1080, height=720, background='brown')
frame_game = Frame(root, width=1080, height=720, background='blue')
frame_eng_ru = Frame(root, width=1080, height=720, background='purple')
frame_ru_eng = Frame(root, width=1080, height=720, background='pink')



frame_meny. pack()


btn1 = Button(frame_meny, text = 'вывод русских слов', font=('Roboto', 25), fg='black', command=delet_bnt1)
btn1.place(x=20, y=60, width=300, height=600)

btn2 = Button(frame_meny, text = 'вывод английских слов', font=('Roboto', 25), fg='black', command=delet_bnt2)
btn2.place(x=380, y=60, width=300, height=600)

btn3 = Button(frame_meny, text = 'игра составь слово', font=('Roboto',25), fg='black', command=delet_bnt3)
btn3.place(x=740, y=60, width=300, height=600)

btn4 = Button(frame_game, text = 'назад', font=('Roboto', 10), fg='black', command=perehod_btn4)
btn4.place(x=1040, y=0, width=40, height=40)

btn5 = Button(frame_eng_ru, text = 'назад', font=('Roboto', 10), fg='black', command=perehod_btn5)
btn5.place(x=1040, y=0, width=40, height=40)

btn6 = Button(frame_ru_eng, text = 'назад', font=('Roboto', 10), fg='black', command=perehod_btn6)
btn6.place(x=1040, y=0, width=40, height=40)



SomeLabel = Label(frame_ru_eng, open_words(), text=slovo[cnt%len(slovo)], font=('Roboto', 50),  bg=pc, fg=blc)
SomeLabel.place(x=40, y=40, width=1000, height=100)


TextInput = Entry(frame_ru_eng, font=('Roboto', 50),  bg=pc, fg=blc)
TextInput.place(x=295, y=320)


btn8 = Button(frame_ru_eng, text = 'готовенько!', font=('Roboto', 20), bg=fic, fg=fic_2, command=word)
btn8.place(x=40, y=140, width=1000, height=180)

otvetka = Label(frame_ru_eng, text='ждем твой ответ:)', font=('Roboto', 48), bg=fic, fg=fic_2)
otvetka.place(x=40, y=400, width=1000, height=300)

cnt_true = Label(frame_ru_eng, text='твой счет', font=('Roboto', 35), bg='#C2F0B3', fg=fic_2)
cnt_true.place(x=40, y=320, width=255, height=80)




##абракадабра



SomeLabel1 = Label(frame_eng_ru, text=perevod[cnt%len(perevod)], font=('Roboto', 50),  bg=pc, fg=blc)
SomeLabel1.place(x=40, y=40, width=1000, height=100)


TextInput1 = Entry(frame_eng_ru, font=('Roboto', 50),  bg=pc, fg=blc)
TextInput1.place(x=295, y=320)


btn9 = Button(frame_eng_ru, text = 'готовенько!', font=('Roboto', 20), bg=fic, fg=fic_2, command=word1)
btn9.place(x=40, y=140, width=1000, height=180)

otvetka1 = Label(frame_eng_ru, text='ждем твой ответ:)', font=('Roboto', 48), bg=fic, fg=fic_2)
otvetka1.place(x=40, y=400, width=1000, height=300)

cnt_true1 = Label(frame_eng_ru, text='твой счет', font=('Roboto', 35), bg='#C2F0B3', fg=fic_2)
cnt_true1.place(x=40, y=320, width=255, height=80)

btn10 = Button(frame_meny, text = 'добавить свои слова', font=('Roboto', 25), fg='black', command=delet_btn10)
btn10.place(x=20, y=10, width=1020, height=60)

btn11 = Button(frame_dobav, text = 'назад', font=('Roboto', 10), fg='black', command=perehod_btn11)
btn11.place(x=1040, y=0, width=40, height=40)

SomeLabel2 = Label(frame_dobav, text='Введи в первую строку русское слово, а во вторую английское', font=('Roboto', 30),  bg=pc, fg=blc)
SomeLabel2.place(x=40, y=40, width=1000, height=100)

SomeLabel3 = Label(frame_dobav, text='1.', font=('Roboto', 100),  bg=pc, fg=blc)
SomeLabel3.place(x=170, y=315, width=100, height=80)

SomeLabel4 = Label(frame_dobav, text='2.', font=('Roboto', 100),  bg=pc, fg=blc)
SomeLabel4.place(x=170, y=415, width=100, height=80)

TextInput2 = Entry(frame_dobav, font=('Roboto', 50),  bg=pc, fg=blc)
TextInput2.place(x=295, y=320)

TextInput3 = Entry(frame_dobav, font=('Roboto', 50),  bg=pc, fg=blc)
TextInput3.place(x=300, y=420)

btn12 = Button(frame_dobav, text = 'готовенько!', font=('Roboto', 40), bg=fic, fg=fic_2, command=del_btn_12)
btn12.place(x=40, y=530, width=1000, height=140)

root.mainloop()


pc = '#F07DE2'
blc = '#0300F0'
fic ='#E5C8EA'
fic_2 = '#BC1AEB'
cnt = 0
cnt_2 = 1
slovo = []
perevod = []
CntTrue = 0

file = open('words.txt.txt', 'r', encoding ='UTF-8')
file_list = [line.strip() for line in file]
for el in file_list:
    print(el.split())
    slovo.append(el.split()[0])
    perevod.append(el.split()[1])





def delet():
    StartBtn.place_forget()



def word():
    global cnt
    otvet()
    TextInput.delete(0, END)
    cnt += 1
    if btn3['text'] == 'eng':
        SomeLabel['text'] = perevod[cnt%len(slovo)]
    else:
        SomeLabel['text'] = slovo[cnt%len(slovo)]


def otvet():
    global CntTrue
    if btn3['text'] == 'eng':
        local_list = slovo
    else:
        local_list = perevod
    if local_list[cnt%len(local_list)] == TextInput.get().lower():
            otvetka['text'] = 'Молодец!Все верно!'
            CntTrue += 1
    else:
            otvetka['text'] = 'Подумай лучше, ты был не прав!'
            CntTrue -= 1



    cnt3()

def cnt3():
    cnt_true['text'] = CntTrue

def btn3_l():
    if btn3['text'] == 'ru':
        btn3['text'] = 'eng'
    else:
        btn3['text'] = 'ru'







root = Tk()
root.title('Приложение для изучения слов')
root.geometry('1080x720')
root. resizable(False, False)

btn3 = Button(root, text = 'ru', font=('Roboto', 10), bg='red', fg='black', command=btn3_l)
btn3.place(x=1040, y=0, width=40, height=40)

SomeLabel = Label(root, text=perevod[cnt%len(perevod)], font=('Roboto', 50),  bg=pc, fg=blc)
SomeLabel.place(x=40, y=40, width=1000, height=100)


TextInput = Entry(root, font=('Roboto', 50),  bg=pc, fg=blc)
TextInput.place(x=295, y=320)


Btn2 = Button(root, text = 'готовенько!', font=('Roboto', 20), bg=fic, fg=fic_2, command=word)
Btn2.place(x=40, y=140, width=1000, height=180)

otvetka = Label(root, text='ждем твой ответ:)', font=('Roboto', 48), bg=fic, fg=fic_2)
otvetka.place(x=40, y=400, width=1000, height=300)

cnt_true = Label(root, text='твой счет', font=('Roboto', 35), bg='#C2F0B3', fg=fic_2)
cnt_true.place(x=40, y=320, width=255, height=80)

StartBtn = Button(root, text ='нажми для начала' , font=('Roboto', 50), bg=fic, fg=fic_2, command=delet)
StartBtn.place(x=0, y=0, width=1080, height=720)


root.mainloop()
