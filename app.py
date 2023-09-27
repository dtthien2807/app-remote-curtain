from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import BOLD, Font
import tkinter as tk
import requests
from urllib import request


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.get_ip()
        

    def create_widgets(self):

        self.bold12 = Font(self.master, size=12, weight=BOLD)
        self.hi_user = tk.Label(self)
        self.hi_user["text"] = "Xin chào user!"
        self.hi_user["font"] = ("Arial", 10)
        self.hi_user.grid(row = 0, column = 0, sticky = W, pady = 2)

        img= (Image.open("images/user.png"))
        resized_image= img.resize((30,30))
        new_image= ImageTk.PhotoImage(resized_image)

        self.image = new_image
        self.img = tk.Label(self)
        self.img["image"] = self.image
        self.img.grid(row = 0, column = 1, sticky = W, pady = 2)

        self.check = tk.Button(self)
        self.check["text"] = "Tình trạng"
        self.check["background"] = "lightgreen"
        self.check["font"] = ("Arial", 10)
        self.check.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 5)

        self.check = tk.Label(self)
        self.check["text"] = "Đóng"
        self.check["fg"] = "darkred"
        self.check.grid(row = 1, column = 1,  sticky = W, padx = 10, pady = 5)

        img_button_open= (Image.open("images/open.png"))
        resized_image_open= img_button_open.resize((150,110))
        new_image_open= ImageTk.PhotoImage(resized_image_open)

        self.photo_button = new_image_open
        self.open = tk.Button(self)
        self.open["image"] = self.photo_button
        self.open["borderwidth"] =2
        self.open["background"] = "gray"
        self.open["command"] = self.open_curtain
        self.open.grid(row = 2, column = 0,columnspan=2, sticky = W, padx = 10, pady = 5)

        self.text_open = tk.Label(self)
        self.text_open["text"] = "MỞ RÈM"
        self.text_open["font"] = self.bold12
        self.text_open.grid(row = 3, column = 0,columnspan=2, sticky = W, padx = 50, pady = 5)

        img_button_close= (Image.open("images/close.png"))
        resized_image_close= img_button_close.resize((150,110))
        new_image_close= ImageTk.PhotoImage(resized_image_close)
        self.photo_button_close = new_image_close
        self.close = tk.Button(self)
        self.close["image"] = self.photo_button_close
        self.close["borderwidth"] =2
        self.close["background"] = "gray"
        self.close["command"] = self.close_curtain
        self.close.grid(row = 4, column = 0, columnspan=2, sticky = W, padx = 10, pady = 5) 

        self.text_close = tk.Label(self)
        self.text_close["text"] = "ĐÓNG RÈM"
        self.text_close["font"] = self.bold12
        self.text_close.grid(row = 5, column = 0, columnspan=2, sticky = W, padx = 45, pady = 5)

        img_button_quit= (Image.open("images/quit.png"))
        resized_image_quit= img_button_quit.resize((50,40))
        new_image_quit= ImageTk.PhotoImage(resized_image_quit)
        self.photo_button_quit = new_image_quit
        self.quit = tk.Button(self, image=self.photo_button_quit, borderwidth=2, background="gray", command=root.destroy)
        self.quit.grid(row = 6, column = 0, columnspan=2, sticky = W, padx = 65, pady = 5)

        self.text_quit = tk.Label(self)
        self.text_quit["text"] = "QUIT"
        self.text_quit["font"] = self.bold12
        self.text_quit["fg"] = "red"
        self.text_quit.grid(row = 7, column = 0, columnspan=2, sticky = W, padx = 70, pady=0)

    def open_curtain(self):
        print(f"Mở rèm cửa")
    def close_curtain(self):
        print(f"Đóng rèm cửa")

    def error(self, error):
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, columnspan=2)
        self.text_error = tk.Label(self.frame)
        self.text_error["text"] = error
        self.text_error["width"] = 50
        self.text_error["height"]= 2
        self.text_error.grid(row = 0, column = 0, sticky = W, pady = 2, in_=self.frame)

        self.button_connect = tk.Button(self.frame, command=self.get_ip)
        self.button_connect["text"] = "Connect"
        self.button_connect["background"] = "darkgreen"
        self.button_connect.grid(row = 1, column = 0, sticky = W, pady = 2, padx=150, in_=self.frame)

    def get_ip(self):
        # Get the WiFi IP address
        try:
            request.urlopen('https://api.ipify.org', timeout=1)
            ip_address = requests.get('https://api.ipify.org').text
            self.create_widgets()
            try:
                check_frame = self.frame
            except AttributeError:
                check_frame = None 

            if check_frame is not None:
                check_frame.place(anchor="nw", x=0, y=0, width=0, height=0)
            # Print the IP address
            print(f"Your WiFi IP address is: {ip_address}")
        except request.URLError as err: 
            noti_error = "You must be connect to wifi!"
            self.error(error=noti_error)
            print(f"You must be connect to wifi!")


root = tk.Tk()
app = Application(master=root)
app.master.title("App điều khiển rèm")
# app.master.minsize(700,400)
root.configure(background="gray")
app.mainloop()