from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExcercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N/{round(location.longitude,4)}°E")

        home=pytz.timezone(result)
        local_t=datetime.now(home)
        current_t=local_t.strftime("%I:%M %p")
        clock.config(text=current_t)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=2ecac1a6964d5e97aa47b59f9ed2fb4a"

        json_data = requests.get(api).json()

        temp = json_data['main']['temp']
        visibility = json_data['visibility']
        condition = json_data['weather'][0]['main']
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']
        description = json_data['weather'][0]['description']

        t.config(text=(temp, "°C"))

        c.config(text=(condition, "|", "feels", "like ", visibility,"visibility"))


        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("WEATHER APP","INVALID ENTRY !! ")

#search box
search_img= PhotoImage(file="search.png")
myimg=Label(image=search_img)
myimg.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=17,font=("arial", 25 ,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icn=PhotoImage(file="search_icon.png")
myimg_icn=Button(image=search_icn,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimg_icn.place(x=400,y=34)

#logo
logo_img=PhotoImage(file="logo.png")
logo=Label(image=logo_img)
logo.place(x=150,y=100)

#bottom box
frame_img=PhotoImage(file="box.png")
frame_my=Label(image=frame_img)
frame_my.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font="arial 15 bold")
name.place(x=30,y=100)
clock=Label(root,font="Helvetica 20")
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label3.place(x=420,y=400)

label4=Label(root,text="PRESSURE",font="Helvetica 15 bold",fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font="arial 50 bold",fg="#ee666d")
t.place(x=400,y=170)
c=Label(font="arial 12 bold")
c.place(x=400,y=250)

w=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
h.place(x=250,y=430)

d=Label(text="...",font="arial 16 bold",bg="#1ab5ef")
d.place(x=420,y=430)

p=Label(text="...",font="arial 20 bold",bg="#1ab5ef")
p.place(x=650,y=430)

#timezone
timezone=Label(root,font="Helvetica 12", fg="white",bg="black")
timezone.place(x=500,y=50)

longlat = Label(root,text="longitude / latitude",font="arial 16 bold", fg="red")
longlat.place(x=500,y=10)
long_lat=Label(root,font="Helvetica 12", fg="white",bg="black")
long_lat.place(x=500,y=50)

root.mainloop()