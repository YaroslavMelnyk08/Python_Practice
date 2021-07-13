import http.client
import json
from tkinter import *
import tkinter as tk


root = Tk()
root.title("Ситуація COVID-19")
root.geometry('300x800')
root['bg']='#C0C0C0'

n=8 

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "d32be4ed28msh025131881b867f7p1c4399jsn7ee02bc339de",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/australia", headers=headers)

res = conn.getresponse()
data = res.read()
All_Info = data.decode("utf-8")
json = json.loads(All_Info)

frametop=Frame(root)
framebot=Frame(root)
frametop.pack()
framebot.pack()

def Ref():
    import json
    TextBox.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/australia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    TextBox.insert('1.0', '\n')
    
    for i in range(n):
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', '\n')

def Search():
    j=0
    for i in range(n):
        InputedCountry = EntryCountry.get()
        GetCountry = json[i].get('Country')
        if InputedCountry == GetCountry:
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalRecovered'))
                TextBox.insert('1.0', 'TotalRecovered : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalDeaths'))
                TextBox.insert('1.0', 'TotalDeaths : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalCases'))
                TextBox.insert('1.0', 'TotalCases : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Continent'))
                TextBox.insert('1.0', 'Continent : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Country'))
                TextBox.insert('1.0', 'Country : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '*' * 30)
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '         We found!')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '*' * 30)
        else : j+=1
        if j==8:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '          We didnt found')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)

Refbutton = Button(frametop, text="Оновлення",command=Ref)
Refbutton['bg']='#C0C0C0'
Refbutton['fg']='#800000'
Refbutton.pack(side=LEFT)

TextBox = Text(framebot,width=500, height=500)
TextBox['bg']='#FFFFFF'
TextBox['fg']='#000000'
TextBox.pack()

Ref()
root.mainloop()
