from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city = city_name.get()
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=ed4c48a8554f2b2d10b2ba77b24ab3cb").json()
    wc_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    wp_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg = "lightblue")
win.geometry("500x550")

name_label = Label(win,text="Weather Application",font=("Time New Roman",30,"bold"))

name_label.place(x=25,y=50,height=50,width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather Application",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

wc_label = Label(win,text="Weather Climate",font=("Time New Roman",20,))
wc_label.place(x=25,y=260,height=50,width=210)

wc_label1 = Label(win,text="",font=("Time New Roman",20,))
wc_label1.place(x=250,y=260,height=50,width=210)

wd_label = Label(win,text="Weather Description",font=("Time New Roman",17,))
wd_label.place(x=25,y=320,height=50,width=210)

wd_label1 = Label(win,text="",font=("Time New Roman",17,))
wd_label1.place(x=250,y=320,height=50,width=210)

wt_label = Label(win,text="Weather Temperature",font=("Time New Roman",16,))
wt_label.place(x=25,y=380,height=50,width=210)

wt_label1 = Label(win,text="",font=("Time New Roman",16,))
wt_label1.place(x=250,y=380,height=50,width=210)

wp_label = Label(win,text="Weather Pressure",font=("Time New Roman",18,))
wp_label.place(x=25,y=450,height=50,width=210)

wp_label1 = Label(win,text="",font=("Time New Roman",18,))
wp_label1.place(x=250,y=450,height=50,width=210)

done_button=Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()