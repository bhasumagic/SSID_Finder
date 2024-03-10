from tkinter import *
import subprocess
from tkinter.ttk import Progressbar
import time

def find():   
    global text
    
    ssids = subprocess.getoutput('netsh wlan show profiles').split('\n')
    ssids = [ a.replace('All User Profile     :', '').strip() for a in ssids if "All User Profile     :" in a ]
    text = ''
    passcount = 0

    if bar['value'] > 0:
        bar['value'] -= bar['value']

    for i in range(len(ssids)):
        command = 'netsh wlan show profiles name="'+ssids[i]+'" key=clear'
        passwrd = subprocess.getoutput(command).split("\n")
        pin = [ s for s in passwrd if "Key Content            :" in s ]
        if pin:
            pin = pin[0].replace("    Key Content            : " , "")
        else:
            passcount += 1
            pin = '( password not available )'

        if i == 0:
            text = ssids[i] + ' - ' + pin
        else:
            text = text + '\n' + ssids[i] + ' - ' + pin
        
        textbox.delete(1.0, END)
        textbox.insert(INSERT, text)
 
        bar['value'] += 100/len(ssids)        
        stat.set(str(i+1) +'/'+str(len(ssids))+'  SSIDs  were checked')
        win.update_idletasks()

    if passcount > 0:    
    	string = str(len(ssids)-passcount) + ' passwords were found. ' + str(passcount) + ' passwords are not available.'
    else:
    	string = str(len(ssids)-passcount) + ' passwords were found.'
    pass_count = Label(win,text=string ,bg='#DDDDDD')
    pass_count.place(relx=0.02,rely=0.93)
    
    
    
win = Tk()
win.title('WiFi Passwords')
win.geometry('400x450')
win.config(background='#DDDDDD')
win.resizable(False , False)

topic = Label(win, text='[      ]   Passwords of connected SSIDs', font=('arial', '14' , 'bold'), bg='#DDDDDD', fg='#000000' )
topic.place(relx=0.05,rely=0.025)

star = Label(win, text='***', font=('arial', '15' , 'bold'), bg='#DDDDDD', fg='#000000' )
star.place(relx=0.0725,rely=0.033)

find_btn = Button(
                win,
                text='Passwords',
                font=('Consolas' , 11, 'italic'),
                width=10,
                bg='#DDDDDD',
                fg='#000000',
                activebackground='#000000',
                activeforeground='#EEEEEE',
                command=find
                )
find_btn.place(relx=0.02,rely=0.12)

bar = Progressbar(win, orient=HORIZONTAL , length=260)
bar.place(relx=0.3,rely=0.12)

stat =StringVar()

status = Label(win, textvariable=stat, bg='#DDDDDD', fg='#000000' )
status.place(relx=0.44,rely=0.17)

textbox = Text(win, width=47, height=17, font=('consolas' ,11))
textbox.place(relx=0.02,rely=0.23)

logo = Label(win, text = 'BHASU\nMAGIC' , font=('dead kansas' , '8') , bg='#DDDDDD' , fg='#444444')
logo.place(relx=0.88,rely=0.925)

win.mainloop()