import customtkinter
import os
import sys
from PIL import Image, ImageTk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        image_path = resource_path("src/assets/np_logo.png")
        self.logo_image = Image.open(image_path)
        self.logo_image = self.logo_image.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = customtkinter.CTkLabel(self, image=self.logo_photo, text="")
        self.logo_label.pack(side="top", pady=20, padx=0)

        self.button = customtkinter.CTkButton(self, text="Sair", command=self.button_callback, fg_color='red')
        self.button.pack(side='bottom', pady=20, padx=20)

    def button_callback(self):
        self.master.quit()
