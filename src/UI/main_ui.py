import customtkinter

from src.UI.LeftFrame.LeftFrame import LeftFrame
from src.UI.RightFrame.RightFrame import RightFrame

class MainUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Estoque")
        self.geometry("920x600")

        customtkinter.set_appearance_mode("system")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = LeftFrame(self)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")

        self.right_frame = RightFrame(self)
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        
ui = MainUI()
ui.mainloop()