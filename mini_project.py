
# import modules 
from tkinter import *
from gnewsclient import gnewsclient 
  
# defined funtions 
def news(): 
    client = gnewsclient.NewsClient( 
        language=lang.get(), location=loc.get(), topic=top.get(), max_results=10) 
    news_list = client.get_news() 
    result_title.set(news_list[0]["title"] + "\n" +
                     news_list[1]["title"] + "\n" + news_list[2]["title"]) 
  
  
# tkinter object 
master = Tk() 
master.title("NEWS") 
  
# background set to grey 
master.configure(bg='light grey') 
  
# Variable Classes in tkinter 
result_title = StringVar() 
result_link = StringVar() 
  
# Creating label for each information 
# name using widget Label 
Label(master, text="Choose language :", bg="light grey").grid(row=0, sticky=W) 
Label(master, text="Choose Location :", bg="light grey").grid(row=1, sticky=W) 
Label(master, text="Choose Topic :", bg="light grey").grid(row=2, sticky=W) 
  
  
lang = Entry(master) 
lang.grid(row=0, column=1) 
  
loc = Entry(master) 
loc.grid(row=1, column=1) 
  
top = Entry(master) 
top.grid(row=2, column=1) 
  
  
# Creating lebel for class variable 
# name using widget Entry 
Label(master, text="", textvariable=result_title, 
      bg="light grey").grid(row=3, column=1, sticky=W) 
  
# creating a button using the widget 
# Button to call the submit function 
Button(master, text="SHOW", command=news, bg="white").grid(row=1, column=3) 
  
  
mainloop() 