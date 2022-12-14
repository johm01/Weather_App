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
        # Weather information widgets 
        self.label_2 = Label(self.root,bg='yellow')
        self.label_2.place(x=115,y=50)
        self.label_3 = Label(self.root,bg='yellow')
        self.label_3.place(x=135,y=200)
        self.label_1 = Label(self.root,width=25,bg='yellow')
        self.label_1.place(x=65,y=150)
        self.label_4 = Label(self.root)
        self.label_4.place(x=65,y=300)
        self.label_5 = Label(self.root,bg='yellow')
        self.label_5.place(x=85,y=185)
        # Other widgets
        self.e_1 = Entry(self.root)
        self.e_1.place(x=65,y=300)
        Button(self.root,text='Enter',command=self.get_weather).place(x=200,y=300)
        Label(self.root, text='Weather App!',bg='grey').place(x=115,y=25)
        self.root.mainloop()
    
    # One function for all the Weather API stuff
    def get_weather(self):
        # Getting the areacode from the entry 
        self.areacode = self.e_1.get()
        # Making a request to the weather API 
        self.url = requests.get(f'http://api.weatherapi.com/v1/current.json?key=&q={self.areacode}&aqi=no')
        # Getting the weather API data
        self.data = self.url.json() 
        # Weather API data
        self.condition = self.data['current']['condition']['text']
        self.temp = str(self.data['current']['temp_f'])
        self.location = self.data['location']['name']
        self.region = self.data['location']['region']
        # Changing the Weather labels text
        self.label_1.config(text='Condition: '+self.condition)
        self.label_3.config(text='Tempature: '+self.temp)
        self.label_5.config(text='Location: '+self.location+', '+self.region)
        self.label_3.place(x=110,y=115)
        # Printing api data in console 
        print(self.data)
                                                                                                                                                                                
if __name__ == "__main__":
    app = App()
    app.get_weather()


