import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter.ttk import *
from ttkbootstrap.constants import *
import random
import os


import TestConnection 
import CreateDatabase
from CreateDatabase import *

exec(open('TestConnection.py').read())
exec(open('CreateDatabase.py').read())

#Szebb verzió, ha az exec nem működik:
#import os
#os.system('py CreateDatabase.py')
#os.system('py TestConnection.py')

cursor = CreateDatabase.cursor

def TicketCheck(price, ticket_2D, ticket_3D, ticket_2D_db, ticket_3D_db):
    price = int(price)
    ticket_2D_db = int(ticket_2D_db) 
    ticket_3D_db = int(ticket_3D_db)
    
    full_price = ((price*ticket_2D_db) + ((price+730)*ticket_3D_db))
    
    
    ticket_countErrorCheck = 0
        
    if ((ticket_2D != ('NONE')) and (ticket_2D_db == 0)) or ((ticket_3D != ('NONE')) and (ticket_3D_db == 0)):
        print("Helytelen - no count")
    else:
        ticket_countErrorCheck += 1
        
    if ((ticket_2D == ('NONE')) and (ticket_2D_db != 0)) or ((ticket_3D == ('NONE')) and (ticket_3D_db != 0)):
        print("Helytelen - no ticket type")
    else:
        ticket_countErrorCheck += 1
    
    if (ticket_2D == ('NONE')) and (ticket_3D == ('NONE')):
        print("Valamit kell választani")
    
    else:
        ticket_countErrorCheck += 1
        if ticket_2D == ('NONE'):
            print("Nem válaszott 2D filmet.")
        elif ticket_3D == ('NONE'):
            print("Nem válaszott 3D filmet.")
    
    if ticket_countErrorCheck == 3:
        os.system('py SignUp.py')
    

def Foglal(price):
    root_foglal = tk.Tk()
    style = ttk.Style('vapor')
    root_foglal.resizable(False, False)
    root_foglal.eval('tk::PlaceWindow . center')
    root_foglal.title('Cinema')

    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
       
    
    lb_title = tk.Label(root_foglal, text="JEGYEK KIVÁLASZTÁSA", justify=CENTER, anchor=CENTER)
    lb_text00 = tk.Label(root_foglal, text="IDŐPONT", justify=CENTER, anchor=CENTER)
    lb_text01 = tk.Label(root_foglal, text="TÍPUS", justify=CENTER, anchor=CENTER)
    lb_text02 = tk.Label(root_foglal, text="ÁR/DB", justify=CENTER, anchor=CENTER)
    lb_text03 = tk.Label(root_foglal, text="DARAB", justify=CENTER, anchor=CENTER)
    lb_text04 = tk.Label(root_foglal, text="JEGY KATEGÓRIA", justify=CENTER, anchor=CENTER)
    lb_time3D = tk.Label(root_foglal, text="14:05", justify=CENTER, anchor=CENTER)
    lb_time2D = tk.Label(root_foglal, text="18:00", justify=CENTER, anchor=CENTER)
    
    lb_3D = tk.Label(root_foglal, text="3D", justify=CENTER, anchor=CENTER)
    lb_2D = tk.Label(root_foglal, text="2D", justify=CENTER, anchor=CENTER)
    lb_price2D = tk.Label(root_foglal, text=f"{price}", justify=CENTER, anchor=CENTER)
    lb_price3D = tk.Label(root_foglal, text=f"{(int(price)+730)}", justify=CENTER, anchor=CENTER)
    
    
    menu3D_C = tk.StringVar(root_foglal)
    menu3D_C.set("NONE")
    drop3D_C = tk.OptionMenu(root_foglal, menu3D_C, "NONE", "Junior", "Senior", "Felnőtt", "Kedvezményezett")
    drop3D_C.config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    drop3D_C["menu"].config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    
    menu2D_C = tk.StringVar(root_foglal)
    menu2D_C.set("NONE")
    drop2D_C = tk.OptionMenu(root_foglal, menu2D_C, "NONE", "Junior", "Senior", "Felnőtt", "Kedvezményezett")
    drop2D_C.config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    drop2D_C["menu"].config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")

    
    menu2D_DB = tk.StringVar(root_foglal)
    menu2D_DB.set("0")    
    drop2D_DB = tk.OptionMenu(root_foglal, menu2D_DB, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop2D_DB.config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    drop2D_DB["menu"].config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    
    menu3D_DB = tk.StringVar(root_foglal)
    menu3D_DB.set("0")    
    drop3D_DB = tk.OptionMenu(root_foglal, menu3D_DB, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    drop3D_DB.config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    drop3D_DB["menu"].config(bg="#1A0933", fg="#32FBE2",
                activebackground="#30125F", activeforeground="#32FBE2")
    
    
    done_ticket = tk.Button(root_foglal, text="JEGY LEFOGLALÁSA", anchor=CENTER, command=lambda:TicketCheck(price, (menu2D_C.get()), (menu3D_C.get()), (menu2D_DB.get()), (menu3D_DB.get())))
    
    lb_title.grid(row=0, column=0, columnspan=6, sticky=EW, ipadx=5, ipady=5, padx=10, pady=(10, 25))
    lb_text00.grid(row=1, column=0, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=(5, 25))
    lb_text01.grid(row=1, column=2, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=(5, 25))
    lb_text02.grid(row=1, column=3, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=(5, 25))
    lb_text03.grid(row=1, column=4, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=(5, 25))
    lb_text04.grid(row=1, column=5, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=(5, 25))

    lb_time3D.grid(row=2, column=0, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    lb_time2D.grid(row=3, column=0, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    lb_3D.grid(row=2, column=2, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    lb_2D.grid(row=3, column=2, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    lb_price3D.grid(row=2, column=3, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    lb_price2D.grid(row=3, column=3, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    drop3D_C.grid(row=2, column=5, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    drop2D_C.grid(row=3, column=5, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    drop3D_DB.grid(row=2, column=4, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    drop2D_DB.grid(row=3, column=4, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    done_ticket.grid(row=4, column=0, columnspan=6, sticky=NSEW, ipadx=5, ipady=5, padx=10, pady=10)
    
    
    
    

def Info(terem, film, maxh, lp_ye, lp_ca, lp_pl, price, lp_id, lp_age):
    terem = int(terem)
    maxh = int(maxh)
    lp_ye = int(lp_ye)
    lp_pl = int(lp_pl)
    
    
    root_info = tk.Tk()
    style_info = ttk.Style('vapor')
    root_info.resizable(False, False)
    root_info.eval('tk::PlaceWindow . center')
    root_info.title('FilmInfo')
    
    betelt = random.randint(0, maxh)
    date = lp_ye
    category = lp_ca
    time = lp_pl
    age = lp_age

    with open('txt/filminfok.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip('\n') for line in f]


    film_lb = tk.Label(root_info, text=f"{film}", background='#1A0933', foreground='#F8F9FA')
    film_date = tk.Label(root_info, text=f"{date}", background='#1A0933', foreground='#F8F9FA')
    film_desc_TXT = tk.Text(root_info, background='#1A0933', foreground='#F8F9FA')
    film_desc_TXT.insert(INSERT, f"{lines[lp_id]}")
    
    lb_TXT = film_desc_TXT.get("1.0", END)
    film_desc = Label(root_info, text=lb_TXT, background='#1A0933', foreground='#F8F9FA', wraplength=330)
    
    
    film_age = tk.Label(root_info, text=f"{age}",background='#1A0933', foreground='#F8F9FA')

    low_prio_lb = tk.Label(root_info, text=f"{category} | {time}perc", background='#1A0933', foreground='#F8F9FA')
    
    
    maxhely_lb = tk.Label(root_info, text=f"Összes ülőhelyek száma: {maxh}", background='#1A0933', foreground='#F8F9FA')
    szabad_lb = tk.Label(root_info, text=f"Szabad ülőhelyek száma: {maxh-betelt}", background='#1A0933', foreground='#F8F9FA')
    teremszam_lb = tk.Label(root_info, text=f"Teremszám: {terem}", background='#1A0933', foreground='#F8F9FA')

    btn = tk.Button(root_info, text="Jegyfoglalás", bg='#1A0933', command=lambda:Foglal(price) )

    

    film_lb.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    film_date.grid(row=0, column=1, sticky=W, padx=5, pady=5)
    film_desc.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)
    low_prio_lb.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    film_age.grid(row=2, column=1, sticky=W, padx=5, pady=5)
    #maxhely_lb.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    #szabad_lb.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    #teremszam_lb.grid(row=4, column=0, sticky=W, padx=5, pady=5)
    
    btn.grid(row=3, column=0, sticky=W, padx=5, pady=5)


# ---------/SQL---------

root = tk.Tk()
style = ttk.Style('vapor')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('Cinema')

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)



select = cursor.execute(
    "SELECT termek.TEREM_SZAM, termek.TEREM_FILM, termek.TEREM_MAXHELY, low_prio.YEAR, low_prio.CATEGORY, low_prio.PLAYTIME, low_prio.PRICE, low_prio.LP_ID, low_prio.AGE FROM termek INNER JOIN low_prio ON termek.LOW_PRIO = low_prio.LP_ID")

teremszam_lst = []
film_lst = []
maxhely_lst = []
LP_year_lst = []
LP_category_lst = []
LP_playtime_lst = []
LP_price_lst = []
LP_age_lst = []
LP_ID = []

for data in (cursor.fetchall()):
    teremszam_lst.append(data[0])
    film_lst.append(data[1])
    maxhely_lst.append(data[2])
    LP_year_lst.append(data[3])
    LP_category_lst.append(data[4])
    LP_playtime_lst.append(data[5])
    LP_price_lst.append(data[6])
    LP_ID.append(data[7])
    LP_age_lst.append(data[8])


btn01 = Button(root, text=film_lst[0], style=LIGHT, command=lambda: Info(
    teremszam_lst[0], film_lst[0], maxhely_lst[0], LP_year_lst[0], LP_category_lst[0], LP_playtime_lst[0], LP_price_lst[0], LP_ID[0], LP_age_lst[0]))

btn02 = Button(root, text=film_lst[1], style=LIGHT, command=lambda: Info(
    teremszam_lst[1], film_lst[1], maxhely_lst[1], LP_year_lst[1], LP_category_lst[1], LP_playtime_lst[1], LP_price_lst[1], LP_ID[1], LP_age_lst[1]))

btn03 = Button(root, text=film_lst[2], style=LIGHT, command=lambda: Info(
    teremszam_lst[2], film_lst[2], maxhely_lst[2], LP_year_lst[2], LP_category_lst[2], LP_playtime_lst[2], LP_price_lst[2], LP_ID[2], LP_age_lst[2]))

btn04 = Button(root, text=film_lst[3], style=LIGHT, command=lambda: Info(
    teremszam_lst[3], film_lst[3], maxhely_lst[3], LP_year_lst[3], LP_category_lst[3], LP_playtime_lst[3], LP_price_lst[3], LP_ID[3], LP_age_lst[3]))

btn05 = Button(root, text=film_lst[4], style=LIGHT, command=lambda: Info(
    teremszam_lst[4], film_lst[4], maxhely_lst[4], LP_year_lst[4], LP_category_lst[4], LP_playtime_lst[4], LP_price_lst[4], LP_ID[4], LP_age_lst[4]))

btn06 = Button(root, text=film_lst[5], style=LIGHT, command=lambda: Info(
    teremszam_lst[5], film_lst[5], maxhely_lst[5], LP_year_lst[5], LP_category_lst[5], LP_playtime_lst[5], LP_price_lst[5], LP_ID[5], LP_age_lst[5]))


btn01.grid(row=0, column=0, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn02.grid(row=0, column=1, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn03.grid(row=0, column=2, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn04.grid(row=1, column=0, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn05.grid(row=1, column=1, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)
btn06.grid(row=1, column=2, sticky=NSEW, ipadx=20, ipady=25, padx=10, pady=10)




root.mainloop()
