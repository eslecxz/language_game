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
    global cnt
    otvet()
    TextInput.delete(0, END)
    cnt += 1
    SomeLabel['text'] = slovo[cnt%len(slovo)]


def word1():
    global cnt
    otvet1()
    TextInput1.delete(0, END)
    cnt += 1
    SomeLabel1['text'] = perevod[cnt%len(slovo)]



def otvet():
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
    TextInput2.delete(0, END)
    TextInput3.delete(0, END)




pc = '#F07DE2'
blc = '#0300F0'
fic ='#E5C8EA'
fic_2 = '#BC1AEB'
cnt = 0
cnt_2 = 1
slovo = []
perevod = []
CntTrue = 0
CntTrue1 = 0


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



SomeLabel = Label(frame_ru_eng, text=slovo[cnt%len(slovo)], font=('Roboto', 50),  bg=pc, fg=blc)
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

'''
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
'''