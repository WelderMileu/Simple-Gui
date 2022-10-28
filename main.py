#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import requests

def main():
    wordlist = []
    try:
        root = Tk()
        root.title("Ghid Brute Force")
        frm  = ttk.Frame(root, padding=20)
        frm.grid()

        def brute(domain):
            try: 
                url   = str(domain)
                r     = requests.get(url)
                code  = r.status_code

                send     = []                

                if code == 200:
                    pb1['value'] = 0

                    calc = (150 / len(wordlist))

                    for i in wordlist:
                        url2  = "{}/{}".format(url, i)
                        print(url2)
                        r2    = requests.get(url2)
                        code2 = r2.status_code
                        
                        root.update_idletasks()
                        pb1['value'] += calc

                        if code2 == 200:
                            send.append(url2)
                            print(url2)

                    for i in send:
                        result['text'] = result['text'] + i + '\n'

                else:
                    result['text'] = ''
                    result['text'] = 'domain if not exists or error in request'
            
            except Exception as err:
                    result['text'] = ''
                    result['text'] = 'domain if not exists'

        def submit():
            r = msgboox_var.get()
            result['text'] = ''
            brute(str(r))

        def open_f():
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            f = filedialog.askopenfile(
                title='open file',
                initialdir='/home/kali/Desktop/lab/',
                filetypes=filetypes
            )

            insert = f.readlines()
            wordlist.clear()

            for i in insert:
                wordlist.append(i.replace("\n", ""))    
    
        pb1 = Progressbar(
                frm,
                orient="horizontal",
                length=150,
                mode='determinate'
        )
    
        pb1.grid(column=0, row=5, columnspan=2)

        msgboox_var = StringVar()

        result  = Label(frm, text="", justify=LEFT)
        result.grid(column=0, row=3, sticky='w')

        info    = Label(frm, text="INSERT TO URL", font=('Arial', 10, 'bold'))
        info.grid(column=0, row=0, columnspan=2)
        
        msgboox = Entry(frm, textvariable = msgboox_var)
        msgboox.grid(column=0, row=1, columnspan=2, pady=10)

        submit_button = Button(frm, text="run atack", command=submit)
        submit_button.grid(column=0, row=2, pady=10)
        
        dialog_file = Button(frm, text="open wordlist", command=open_f)
        dialog_file.grid(column=1, row=2, pady=10, padx=5)
        
        root.mainloop()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
