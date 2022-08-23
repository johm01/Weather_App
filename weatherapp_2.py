from multiprocessing import Condition
from tkinter import *
import requests
import json

class App:
    def __init__(self) -> None:
        # App settings 
        self.root = Tk()
        self.root.geometry("300x400")
        self.root.title("Weather App")
        self.root.configure(bg="yellow")
        self.root.resizable(False,False)
        # App Widgets 
        self.img_1 = PhotoImage(file='c:/gui/sun and cloud.png')
        self.img_2 = PhotoImage(file='c:/gui/sun and cloud.png')
        self.img_3 = PhotoImage(file='c:/gui/sun.png')
        self.label_2 = Label(self.root,bg='yellow')
        self.label_2.place(x=115,y=50)
        self.label_3 = Label(self.root,bg='yellow')
        self.label_3.place(x=135,y=200)
        self.label_1 = Label(self.root,width=25,bg='yellow')
        self.label_1.place(x=65,y=150)
        self.label_4 = Label(self.root)
        self.label_4.place(x=65,y=300)
        self.e_1 = Entry(self.root)
        self.e_1.place(x=65,y=300)
        self.b_1 = Button(self.root,text='Enter',command=self.get_weather)
        self.b_1.place(x=175,y=300)
        self.root.mainloop()
    
    # One function for all the Weather API stuff
    def get_weather(self):
        # Getting the areacode from the entry 
        self.areacode = self.e_1.get()
        # Making a request to the weather API 
        self.url = requests.get(f'http://api.weatherapi.com/v1/current.json?key=9882b06f04a14ed49fd02510222704&q={self.areacode}&aqi=no')
        # Getting the weather API data
        self.data = self.url.json() 
        self.label_1.config(text='Condition: '+self.data['current']['condition']['text'])
        self.label_3.config(text='Tempature: '+str(self.data['current']['temp_f']))
        # Checking weather condition
        if self.data['current']['condition']['text'] == 'Partly cloudy':
            self.label_2.config(image=self.img_1)
        elif self.data['current']['condition']['text'] == 'Cloudly':
            self.label_2.config(image=self.img_2)
        elif self.data['current']['condition']['text'] == 'Sunny':
            self.label_2.config(image=self.img_3)
        print(self.data)
                                                                                                                                                                                
if __name__ == "__main__":
    app = App()
    app.get_weather()


