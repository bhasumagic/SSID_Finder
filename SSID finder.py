from tkinter import *
import subprocess
from tkinter.ttk import Progressbar
import webbrowser

def find():   
    global text

    if bar['value'] > 0:
        bar['value'] -= bar['value']
        textbox.delete(1.0, END)
        stat.set('                                                      ') 
        win.update_idletasks()  

    ssids = subprocess.getoutput('netsh wlan show profiles').split('\n')
    ssids = [ a.replace('All User Profile     :', '').strip() for a in ssids if "All User Profile     :" in a ]
    text = ''
    passcount = 0

    for i in range(len(ssids)):
        passwrd = subprocess.getoutput('netsh wlan show profiles name="'+ssids[i]+'" key=clear').split("\n")
        pin = [ s for s in passwrd if "Key Content            :" in s ]
        if pin:
            pin = pin[0].replace("    Key Content            : " , "")
        else:
            passcount += 1
            pin = '( password is not available )'

        text = ssids[i] + ' - ' + pin + "\n"
        textbox.insert(INSERT, text)
        
        bar['value'] += 100/len(ssids)
        stat.set(str(i+1) +'/'+str(len(ssids))+' SSIDs were checked')
        
        win.update_idletasks()
    
    if passcount == 1:
        string = str(len(ssids)-1) + ' passwords were found. 1 password is not available.'
    elif passcount > 1:
        string = str(len(ssids)-passcount) + ' passwords were found. ' + str(passcount) + ' passwords are not available.'
    else:
        string = str(len(ssids)-passcount) + ' passwords were found.'
        
    pass_count = Label(win,text=string ,bg='#DDDDDD')
    pass_count.place(relx=0.02,rely=0.93)
  

def contact():
    webbrowser.open_new_tab('https://twitter.com/BhasuMagic?t=1QIGpUnQSBYds58jPHBbQ&s=09')
      
  

win = Tk()
win.title('Passwords of known WiFi Networks')
win.geometry('400x470')
win.config(background='#DDDDDD')
win.resizable(False , False)

topic = Label(win, text='[PIN]   Passwords of known WiFi Networks', font=('arial', '13' , 'bold'), bg='#DDDDDD', fg='#000000' )
topic.place(relx=0.05,rely=0.026)

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
find_btn.place(relx=0.025,rely=0.12)

bar = Progressbar(win, orient=HORIZONTAL , length=260)
bar.place(relx=0.3,rely=0.12)

stat =StringVar()

status = Label(win, textvariable=stat, bg='#DDDDDD', fg='#000000' )
status.place(relx=0.44,rely=0.17)

textbox = Text(win, width=47, height=18, font=('consolas' ,11))
textbox.place(relx=0.02,rely=0.23)

logo = Button(
            win,
            text = 'BHASU\nMAGIC',
            font=('dead kansas' , '8'),
            width=5,
            border=0,
            bg='#DDDDDD',
            fg='#000000',
            activebackground='#DDDDDD',
            activeforeground='#000000',
            command=contact
            )
logo.place(relx=0.88,rely=0.93)

win.mainloop()