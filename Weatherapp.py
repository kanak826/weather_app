from tkinter import*
from tkinter import ttk
import requests
import os


API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def data_get():
  city = city_name.get()
#   if not API_KEY:

  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid="+API_KEY).json()
  
#    weather_label1.config(text="Missing API key")
#    return
#   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#   data = requests.get(url).json() #

  weather_label1.config(text=data["weather"][0]["main"])

  wd_label1.config(text=data["weather"][0]["description"])
  temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
  Pres_label1.config(text=data["main"]["pressure"])

# city_name="Bhopal"
# print(data)



win =Tk()
win.title("Today's Weather")
win.config(bg="sky blue")
win.geometry("500x570")

name_label = Label(win,text="Today's Weather App",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Delhi (NCT)",
    "Jammu & Kashmir",
    "Ladakh",
    "Puducherry",
    "Chandigarh",
    "Andaman & Nicobar Islands",
    "Dadra & Nagar Haveli and Daman & Diu",
    "Lakshadweep"
]

box = ttk.Combobox(win,text="Today's Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
box.place(x=25,y=120,height=50,width=450)


weather_label=Label(win,text="Weather Climate",
                    font=("Time New Roman",15))
weather_label.place(x=25,y=260,height=50,width=210)

weather_label1=Label(win,text="",
                    font=("Time New Roman",15))
weather_label1.place(x=250,y=260,height=50,width=210)


wd_label=Label(win,text="Weather Description",
                    font=("Time New Roman",15))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label1=Label(win,text="",
                    font=("Time New Roman",15))
wd_label1.place(x=250,y=330,height=50,width=210)


temp_label=Label(win,text="Temperature",
                    font=("Time New Roman",15))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1=Label(win,text="",
                    font=("Time New Roman",15))
temp_label1.place(x=250,y=400,height=50,width=210)


Pres_label=Label(win,text="Pressure",
                    font=("Time New Roman",15))
Pres_label.place(x=25,y=470,height=50,width=210)


Pres_label1=Label(win,text="",
                    font=("Time New Roman",15))
Pres_label1.place(x=250,y=470,height=50,width=210)


Done_button = Button(win,text="Done",
                     font=("Time New Roman",20,"bold"),command=data_get)
Done_button.place(x=200,y=190,height=50,width=100)



win.mainloop()